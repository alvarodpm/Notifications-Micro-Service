from kafka import KafkaConsumer
import smtplib
import ssl
import json
from email.message import EmailMessage

# Configurar el consumidor Kafka
consumer = KafkaConsumer('my-topic', bootstrap_servers=['localhost:9093'])

def send_email(receiver, score):
    subject = 'Resultado del Examen'
    body = f'Tu puntuación en el examen es: {score}'
    email_sender = 'alvarodplata3@gmail.com'
    email_receiver = receiver
    email_password = 'XXXXXXXXXXXXXXXXXXXX'
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

for message in consumer:
    event = json.loads(message.value.decode('utf-8'))  # Suponiendo que los eventos están codificados en utf-8
    print(event)
    if event['event_type'] == "testEvaluated":
        print('voy a intentar enviar un correo')
        contact = event['contact']
        score = event['score']
        send_email(contact, score)
