from datetime import datetime


def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey, How are you doing?"

    if user_message in ("who are you?", "who are you"):
        return "I am divyansh!!"

    if user_message in ("time", "what's the time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if user_message in ("who am i?", "hi bot"):
        return "Hello, kaisi ho mummy?"

    if user_message in "hello, hi, kaise ho?":
        return "Hello sona!!"

    return "I don't understand what you want to say."
