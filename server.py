import io
from flask import Flask, send_file
from wxpy import Bot
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/newbot")
def newBot():
    bot = Bot(qr_path = 'static/qr.png',qr_callback=qr_callback)
    with open("static/qr.png", 'rb') as bites:
        return send_file(
            io.BytesIO(bites.read()),
            attachment_filename='logo.jpeg',
            mimetype='image/jpg'
        )

def qr_callback(uuid, status, qrcode):
    # with open("static/qr.png", 'rb') as bites:
    #     return send_file(
    #         io.BytesIO(bites.read()),
    #         attachment_filename='logo.jpeg',
    #         mimetype='image/jpg'
    #     )
    return send_file(
            io.BytesIO(qrcode),
             attachment_filename='logo.jpeg',
             mimetype='image/jpg'
         )


if __name__ == '__main__':
    app.run()