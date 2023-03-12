import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)




@app.route("/")
def hello():
    return "Hello World!"





if __name__ == "__main__":
    app.run()    
