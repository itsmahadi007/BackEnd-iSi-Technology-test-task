import requests
from django.conf import settings
from django.core.mail import send_mail


def sent_mail(subject, message, to_email, from_email=None):
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = to_email
    try:
        a = send_mail(subject, message, email_from, recipient_list)
        print(a)
        return True
    except Exception as e:
        print(e)
        return False


def send_sms(phone: str, message: str):
    try:
        username = "Test"
        password = "Test"
        to_number = phone
        caller_id = "Test"
        my_message = message

        # Send SMS
        sms_url = "Test"
        sms_params = {
            "username": username,
            "password": password,
            "number": to_number,
            "callerid": caller_id,
            "message": my_message,
        }
        sms_response = requests.post(sms_url, data=sms_params)
        sms_info = sms_response.text
        print(sms_response.status_code)
        print(sms_response.text)
        return sms_info
    except Exception as e:
        print(e)
        return True
