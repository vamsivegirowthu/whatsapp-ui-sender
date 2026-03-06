import os
from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

images = {
    "1": "https://demo.twilio.com/owl.png",
    "2": "https://images.unsplash.com/photo-1517849845537-4d257902454a",
    "3": "https://images.unsplash.com/photo-1546182990-dffeafbe841d"
}

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Template Error: {str(e)}"


@app.route("/send", methods=["POST"])
def send():
    try:

        phones = request.form.get("phones")
        selected_image = request.form.get("image")

        if not phones or not selected_image:
            return "Please enter phone numbers and select image."

        image_url = images[selected_image]

        phone_list = phones.split(",")

        for phone in phone_list:

            phone = phone.strip()

            client.messages.create(
                from_="whatsapp:+14155238886",
                body="Image from UI",
                media_url=[image_url],
                to="whatsapp:" + phone
            )

        return "Messages Sent Successfully!"

    except Exception as e:
        return f"ERROR: {str(e)}"
