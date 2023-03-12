from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/callback", methods=['POST'])
def callback():
    # 取得 Line 的 HTTP 請求
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        # 解析 Line 的 HTTP 請求，並處理訊息事件
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回應使用者傳送的訊息
    reply_message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, reply_message)


