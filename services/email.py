from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi import BackgroundTasks, UploadFile, File
from pydantic import EmailStr, BaseModel
from typing import List, Dict, Any
from config import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_TLS = settings.MAIL_TLS,
    MAIL_SSL = settings.MAIL_SSL,
    MAIL_FROM_NAME = settings.MAIL_FROM_NAME,
)

fm = FastMail(conf)

class Mail(BaseModel):
    email: List[EmailStr]
    content: Dict[str, Any]

async def simple_send(mail: Mail, template):
    message = MessageSchema(subject=mail.content.get('subject'), recipients=mail.email, body=template.format(**mail.content), subtype="html")
    await fm.send_message(message)

async def background_send(background_tasks:BackgroundTasks, mail: Mail, template):
    message = MessageSchema(subject=mail.content.get('subject'), recipients=mail.email, body=template.format(**mail.content), subtype="html")
    background_tasks.add_task(fm.send_message, message)

async def send_file(background_tasks:BackgroundTasks, mail:Mail, template, files:List[UploadFile]=File(...)):
    message = MessageSchema(subject=mail.content.get('subject'), recipients=mail.email, body=template.format(**mail.content), attachments=files)
    background_tasks.add_task(fm.send_message, message)