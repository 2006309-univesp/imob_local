from twilio.rest import Client


TWILIO_ACCOUNT_SID = 'Coloque_aqui_sua_SID_do_Twilio'
TWILIO_AUTH_TOKEN = 'Coloque_Seu_AuthToken_aqui'
TWILIO_WHATSAPP_NUMBER = 'Coloque_aqui_o_whatsapp_do_twilio'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to, body):
    message = client.messages.create(
        body=body,
        from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
        to=f'whatsapp:{to}'
    )
    return message.sid

def handle_incoming_message(request_data):
    from_number = request_data.get('From')
    message_body = request_data.get('Body')

    # Processa a mensagem (exemplo básico de resposta)
    response_text = f"Você disse: {message_body}"

    # Envia a resposta de volta ao usuário
    send_whatsapp_message(from_number, response_text)
