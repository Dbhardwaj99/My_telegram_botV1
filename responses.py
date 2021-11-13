from datetime import datetime
import json

f = open("database.json", "r")
s = f.read()
info = json.loads(s)

def sample_response(input_text):
    user_message = str(input_text).lower()

    space_index = user_message.index(' ')
    username = user_message[0:space_index]
    password = user_message[space_index + 1:]
    # print(username)
    # print(password)

    if username in info.keys():
        if password == info[username]["Password"]:
            return str(info[username])
        else:
            return "Wrong Password"

    if user_message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "Invalid Username."
