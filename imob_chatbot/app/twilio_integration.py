from twilio.rest import Client

# Configurações da conta Twilio
#TWILIO_ACCOUNT_SID = 'AC864dce0a919bfcfcbe9d3e3ef5fc2734'
#TWILIO_AUTH_TOKEN = '05e92ede08f26e401a4dec99c6c0cc6b'
TWILIO_ACCOUNT_SID = 'AC61af2b33254e2f65fca4d50d50176711'
TWILIO_AUTH_TOKEN = '586041219c9aec5db3b8e2f5a6f87ce1'
TWILIO_WHATSAPP_NUMBER = '+14155238886'

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
