import os
from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials from Railway variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Image options
images = {
    "1": "https://demo.twilio.com/owl.png",
    "2": "https://images.unsplash.com/photo-1517849845537-4d257902454a",
    "3": "https://images.unsplash.com/photo-1546182990-dffeafbe841d"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():

    phones = request.form["phones"]
    selected_image = request.form["image"]

    image_url = images[selected_image]

    phone_list = phones.split(",")

    for phone in phone_list:

        client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio Sandbox
            body="Image from UI",
            media_url=[image_url],
            to='whatsapp:' + phone.strip()
        )

    return "Messages Sent Successfully!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
