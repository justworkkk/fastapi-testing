import smtplib
from celery import Celery
from src.config import SMTP_PASSWORD, SMTP_USER
from email.message import EmailMessage
import logging

log = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery("tasks", broker="redis://localhost:6379")


def get_email(username: str):
    email = EmailMessage()
    email["Subject"] = "TradingApp"
    email["From"] = SMTP_USER
    email["To"] = SMTP_USER

    email.set_content(
        f"<div><h1>Hello, {username}, it's test email message!</h1></div>",
        subtype="html",
    )
    return email


@celery.task
def send_email(username: str):
    email = get_email(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
