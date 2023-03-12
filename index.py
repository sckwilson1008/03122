import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

CHANNEL_SECRET = "405c12ebd48d02117433cde09f727044"
CHANNEL_ACCESS_TOKEN = "kwZ6RMTHwbtWUgP/pBUlDI8RJYgidnH1Zjj6EQllHDSz3yY4CUBboNpv9e4JjyojM047SNVapVg1utpll2vut6rdREiJvGGcHnGXrVNSPIji51UHILc2rUOXmlNCJEg7Sm8/2/8xzQOlBB0eWJFQ6gdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/")
def hello():
    return "Hello, World!"
