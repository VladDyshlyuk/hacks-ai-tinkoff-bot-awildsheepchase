const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbox");
const chatbotToggler = document.querySelector(".chatbot-toggler");
const chatbotCloseBtn = document.querySelector(".close-btn");

let userMessage;
const API_URL = "<API_ENDPOINT>";
const inputInitHeight = chatInput.scrollHeight;

const proccessPipeline = s => 
   s.replace(/\*{1,2}(.*?)\*{1,2}/g, '<strong>$1</strong>')
    .replace(/`(.*?)`/g, '<code>$1</code>');

const createChatLi = (message, className, links) => {
    const chatLi = document.createElement("Li");
    chatLi.classList.add("chat", className);
    if (className === 'outgoing') {
        let chatContent = `<div class="message-container user"><p></p></div>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = message;
        return chatLi;
    }
    else {
        let chatContent =  `<span class="material-symbols-outlined">tag</span><div class="message-container bot"><p></p></div>`;
        chatLi.innerHTML = chatContent;
        const letters = message.split('')
        const markedMessage = proccessPipeline(message)
        let counter = 0
        let item = ''
        const interval = setInterval(() => {
            if (counter < letters.length) {
                if (letters[counter] != '*') {
                    item += letters[counter]
                    chatLi.querySelector("p").textContent = item;
                }
                ++counter
            } else {
                let sum = links.reduce((accum, current) => {
                    let linkElem = CreateButton(current).outerHTML
                    return accum + linkElem
                }, '')
                let chatContent =  `<span class="material-symbols-outlined">tag</span><div class="message-container bot"><p>${markedMessage}</p>${sum}</div>`;
                chatLi.innerHTML = chatContent;
                clearInterval(interval)
            }
        }, 10)
        return chatLi;
    }
}

const createElement = (typeElement, content) => {
    const chatElement = document.createElement('Li')
    chatElement.classList.add("chat", "incoming")
    const chatElementContent = `<span class="material-symbols-outlined">tag</span><div class="message-container ${typeElement}"><p>${content}</p></div>`
    chatElement.innerHTML = chatElementContent
    if (typeElement === 'bot') {
        let counterDot = 0
        let itemDot = 'Загрузка'

        const intervalDot = setInterval(() => {
            if (counterDot < 3) {
                itemDot += '.'
                chatElement.querySelector("p").textContent = itemDot;
                ++counterDot
            } else {
                itemDot = itemDot.replace(/\./gi,'')
                counterDot = 0
            }
        }, 500)

        setTimeout(() => clearInterval(intervalDot), 10000);

        return chatElement
    } else {
        return chatElement
    }
}

const CreateButton = (link) => {
    const linkButton = document.createElement("a");
    linkButton.classList.add("btn-link")
    const url = new URL(link)
    linkButton.textContent = url.hostname
    linkButton.href = link
    return linkButton
}

const generateResponse = (question) => {
    sendChatBtn.classList.add('disabled')
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
    query: question
    });

    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };

    let loading = chatbox.appendChild(createElement("bot", "Загрузка"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    fetch(API_URL, requestOptions)
    .then((response) => response.json())
    .then((result) => {
        loading.remove()
        chatbox.appendChild(createChatLi(`${result.text} \n`, "incoming", result.links));
        chatbox.scrollTo(0, chatbox.scrollHeight);
    })
    .catch(() => {
        loading.remove()
        chatbox.appendChild(createElement("error", "Что-то пошло не так, попробуйте позже :("));
        chatbox.scrollTo(0, chatbox.scrollHeight);
    })
    .finally(() => {
        sendChatBtn.classList.remove('disabled')
        console.log('request -> response luck')
    });
}



const handleChat = () => {
    userMessage = chatInput.value.trim();
    if(!userMessage) return;
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    chatbox.appendChild(createChatLi(userMessage, "outgoing", undefined));
    chatbox.scrollTo(0, chatbox.scrollHeight);

    generateResponse(userMessage);
}

chatInput.addEventListener("input", () => {
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
})

chatInput.addEventListener("keydown", (e) => {
    if(e.key === "Enter" && !sendChatBtn.classList.value === 'material-symbols-outlined disabled' && !e.shiftkey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
})

sendChatBtn.addEventListener("click", handleChat);
chatbotCloseBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));

