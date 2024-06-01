from sentence_transformers import SentenceTransformer
from vector_db import Database
from model_answer import llm_answer
import configparser
from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread



config = configparser.ConfigParser()
config.read('settings.ini')


dbname = ""
dbhost = ""
dbuser = ""
dbpassword = ""
dbport = ""
table_name = "test"

db = Database(dbname, dbhost, dbuser, dbpassword, dbport)
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

def create_response(query):
  answer = llm_answer(query, db, model, table_name=table_name)
  text = answer['text']
  links = answer['sources']
  return {
      "text": text,
      "links" : links
    }

app = Flask(__name__)
CORS(app)

@app.route('/assist', methods=['POST'])
def assist():
    # Extract the request data
    req_data = request.get_json()

    # Check if the required 'query' field is present in the request
    if not req_data or 'query' not in req_data:
        return jsonify({
            "detail": [
                {
                    "loc": ["body", "query"],
                    "msg": "field required",
                    "type": "value_error.missing"
                }
            ]
        }), 422

    # Example response
    response = create_response(req_data['query'])
    return jsonify(response), 200


def run_flask():
    app.run()


# Using a thread to run Flask so the executing cell doesn't block
thread = Thread(target=run_flask)
thread.start()