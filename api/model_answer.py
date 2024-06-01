import requests
import json
from vector_db import Database
import configparser


catalog_id = ""
api_key = ""


def context_generating(query: str, database, model, table_name="test", n=3):
    ct, sources = database.db_search(query, model, table_name=table_name, n=n)
    context = " ".join(ct)
    return context, sources

def llm_answer(query: str, database, model, table_name="test", n=3):
    context, sources = context_generating(query, database, model, table_name=table_name, n=n)
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    prompt = f"""Ты - виртуальный помощник крупного банка "Тинькофф", отвечающий на вопросы, связанные с работой банка с бизнесом.\n
        Твоя задача - ответить на запрос пользователя, исходя из контекста так, как ответил бы виртуальный помощник.\n
        Контекст содержит несколько вопросов, твоя задача выбрать наиболее подходящий, на твой взгляд, под поставленный вопрос и основываясь в большей степени на нем, строить свой ответ.\n
        Если ответ на вопрос пользователя не содержится в контексте, ты не должен на него отвечать.
        Контекст: {context}"""

    payload = json.dumps({
        "modelUri": f"gpt://{catalog_id}/yandexgpt/latest",
        "completionOptions": {
            "stream": False, 
            "temperature": 0.6, 
            "maxTokens": 2000,
        },
        "messages": [
            {"role": "system", "text": prompt},
            {"role": "user", "text": query}
        ],
    })

    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return {
        "text": json.loads(response.text)["result"]["alternatives"][0]["message"][
            "text"
        ],
        "sources": sources,
    }
