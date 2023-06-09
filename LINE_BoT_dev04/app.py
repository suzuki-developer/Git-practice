########################################################################
# Flask、LINE Messaging APIで必要なライブラリやクラスや例外処理のインポート
########################################################################
from flask import Flask, request, abort
import datetime

from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)


###########################
# Flaskのインスタンスを作成
###########################
app = Flask(__name__)


#############################################################
# チャンネルアクセストークンとチャンネルシークレットを変数に格納
#############################################################
ACSESS_TOKEN = "JLEy41olssea4IohuFlB1rJ9KtXGFWGfh5hSU6ryiyhiUc3Uhx1JqME5SooFDiYbEdT5yikDsennsUIRR5bis1VuSRNZAFWINxuN790IJN8ob62EPIocIa8cgaoPJFsir+BDIEfXa0uv7Ray5YpJNAdB04t89/1O/w1cDnyilFU="
SECRET = "65fc96661dd15193727ad755a07c45b1"

line_bot_api = LineBotApi(ACSESS_TOKEN)
handler = WebhookHandler(SECRET)


###########################################################################
# /callbackエンドポイントで受信したPOSTリクエストを処理するcallback関数を定義
###########################################################################
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True) 
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)                     
    except InvalidSignatureError:
        print("Invslid signature. Please check your channel access token/channel secret.")
        abort(400)
    
    return 'OK'  

################################################
# テキストメッセージを受け取った際に実行される関数
################################################
# 第一引数は固定
# 第二引数は返信するメッセージを指定

# # オウム返しを行う
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(                  # line_bot_apiから.reply_message()を呼ぶことでメッセージの返信を行う
#         event.reply_token,
#         TextSendMessage(text=event.message.text) # event.message.text ⇒ ユーザーが送信したメッセージ
#     )

# # 画像をリプライする（ユーザーが何を発言してもルフィの画像が返ってくる）
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(                  
#         event.reply_token,
#         ImageSendMessage(
#         original_content_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
#         preview_image_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
#         )
#     )

# 今何時と聞くと現在時刻を答えてくれる
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in ["今何時", "時間", "現在時刻"]:
        reply_message = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%Sです")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )
    elif event.message.text in ["ルフィ", "海賊王", "ゴム人間"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
            preview_image_url='https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png',
        )
    )
    elif event.message.text in ["ゾロ", "剣豪", "大剣豪"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-rzRcgoXDqEg/YAOTCKoCpPI/AAAAAAABdOI/5Bl3_zhOxm07TUGzW8_83cXMOT9yy1VJwCNcBGAsYHQ/s1041/onepiece02_zoro_bandana.png',
            preview_image_url='https://1.bp.blogspot.com/-rzRcgoXDqEg/YAOTCKoCpPI/AAAAAAABdOI/5Bl3_zhOxm07TUGzW8_83cXMOT9yy1VJwCNcBGAsYHQ/s1041/onepiece02_zoro_bandana.png',
        )
    )
    elif event.message.text in ["ナミ", "みかん", "美女", "航海士"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-2ut_UQv3iss/X-Fcs_0oAII/AAAAAAABdD8/jrCZTd_xK-Y6CP1KwOtT_LpEpjp-1nvxgCNcBGAsYHQ/s1055/onepiece03_nami.png',
            preview_image_url='https://1.bp.blogspot.com/-2ut_UQv3iss/X-Fcs_0oAII/AAAAAAABdD8/jrCZTd_xK-Y6CP1KwOtT_LpEpjp-1nvxgCNcBGAsYHQ/s1055/onepiece03_nami.png',
        )
    )
    elif event.message.text in ["ウソップ", "そげキング", "狙撃手"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-mZpzgXC1Sxk/YAOTCAKwWTI/AAAAAAABdOM/5B4hXli0KLU5N-BySHgjVbhZscKLSE-bQCNcBGAsYHQ/s1025/onepiece04_usopp_sogeking.png',
            preview_image_url='https://1.bp.blogspot.com/-mZpzgXC1Sxk/YAOTCAKwWTI/AAAAAAABdOM/5B4hXli0KLU5N-BySHgjVbhZscKLSE-bQCNcBGAsYHQ/s1025/onepiece04_usopp_sogeking.png',
        )
    )
    elif event.message.text in ["サンジ", "たらし", "鼻血", "コック"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-HPG_x7XPky8/X-FctLTLkKI/AAAAAAABdEE/xs4T8m0FiBAFptXHGQhQ2c9ZmVWtaeQSgCNcBGAsYHQ/s1028/onepiece05_sanji.png',
            preview_image_url='https://1.bp.blogspot.com/-HPG_x7XPky8/X-FctLTLkKI/AAAAAAABdEE/xs4T8m0FiBAFptXHGQhQ2c9ZmVWtaeQSgCNcBGAsYHQ/s1028/onepiece05_sanji.png',
        )
    )
    elif event.message.text in ["チョッパー", "船医", "医者", "トナカイ"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/--9Rl2O4BBN0/X-Fct8K5mqI/AAAAAAABdEI/yLOziAqJO34fwn73AolVP0e42A2h-ql1QCNcBGAsYHQ/s992/onepiece06_chopper.png',
            preview_image_url='https://1.bp.blogspot.com/--9Rl2O4BBN0/X-Fct8K5mqI/AAAAAAABdEI/yLOziAqJO34fwn73AolVP0e42A2h-ql1QCNcBGAsYHQ/s992/onepiece06_chopper.png',
        )
    )
    elif event.message.text in ["ロビン", "ニコロビン", "超絶美女", "考古学者"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-JiNpsjnPn7g/X-FcuWcU37I/AAAAAAABdEQ/P5r3wBMTRegjl7njCk4zWBkdoay44-T2gCNcBGAsYHQ/s1151/onepiece07_robin.png',
            preview_image_url='https://1.bp.blogspot.com/-JiNpsjnPn7g/X-FcuWcU37I/AAAAAAABdEQ/P5r3wBMTRegjl7njCk4zWBkdoay44-T2gCNcBGAsYHQ/s1151/onepiece07_robin.png',
        )
    )
    elif event.message.text in ["フランキー", "サイボーグ", "変態", "船大工"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-H8YBA_SpxGs/X-Fcu75hh_I/AAAAAAABdEU/WRKUa03ypYor3TwvhziHAnSEcTN4Noq0gCNcBGAsYHQ/s1148/onepiece08_franky.png',
            preview_image_url='https://1.bp.blogspot.com/-H8YBA_SpxGs/X-Fcu75hh_I/AAAAAAABdEU/WRKUa03ypYor3TwvhziHAnSEcTN4Noq0gCNcBGAsYHQ/s1148/onepiece08_franky.png',
        )
    )
    elif event.message.text in ["ブルック", "骨", "音楽家"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-KZ0MJgiPJHo/X__CLeY-zVI/AAAAAAABdNM/HnFYqUe0VQEzCWCqyMggibpk4kBRtFCpQCNcBGAsYHQ/s1102/onepiece09_brook.png',
            preview_image_url='https://1.bp.blogspot.com/-KZ0MJgiPJHo/X__CLeY-zVI/AAAAAAABdNM/HnFYqUe0VQEzCWCqyMggibpk4kBRtFCpQCNcBGAsYHQ/s1102/onepiece09_brook.png',
        )
    ) 
    elif event.message.text in ["ジンベエ", "操舵手", "任侠"]:
        line_bot_api.reply_message(                  
            event.reply_token,
            ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-vIXZ3_KMn9g/X-FcvVKPQSI/AAAAAAABdEc/i8oJKU0UDMM2uQfzemn6oOmJLICo4VcVgCNcBGAsYHQ/s1185/onepiece10_jinbe.png',
            preview_image_url='https://1.bp.blogspot.com/-vIXZ3_KMn9g/X-FcvVKPQSI/AAAAAAABdEc/i8oJKU0UDMM2uQfzemn6oOmJLICo4VcVgCNcBGAsYHQ/s1185/onepiece10_jinbe.png',
        )
    ) 
    else:
        line_bot_api.reply_message(                  
            event.reply_token,
            TextSendMessage("ワンピースのキャラクター名か現在時刻を入力して下さい！！") 
        )         


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     if event.message.text == '現在時刻':
#         reply_message = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%Sです')
#     # else:
#     #     reply_message = "「現在時刻」と送信してください。"
#     line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=reply_message))

#######################################################
# アプリケーションをテストするためのローカルサーバーを開始
#######################################################
if __name__ == "__main__":
    app.run(host="localhost", port=8000)