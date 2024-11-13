from flask import request, Blueprint
from twilio.twiml.messaging_response import MessagingResponse
import requests
from config import config
from app.bot import get_access_token

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/chat', methods=['POST'])
def chat():
    incoming_msg = request.values.get('Body')
    sender_id = request.values.get('From')

    # Obtenha o token de acesso do Dialogflow
    access_token = get_access_token()

    # URL do Dialogflow
    session_id = sender_id
    dialogflow_url = f"https://dialogflow.googleapis.com/v2/projects/{config.PROJECT_ID}/agent/sessions/{session_id}:detectIntent"
    
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "query_input": {
            "text": {
                "text": incoming_msg,
                "language_code": "pt-BR"
            }
        }
    }

    response = requests.post(dialogflow_url, headers=headers, json=data)
    dialogflow_response = response.json()
    response_text = dialogflow_response.get("queryResult", {}).get("fulfillmentText", "Desculpe, não entendi.")

    twilio_response = MessagingResponse()
    twilio_response.message(response_text)

    return str(twilio_response)
