import smtplib
from email.mime.text import MIMEText
import time

data_table = {}

with open("email.txt") as email, open("professor_list.txt") as professors, open("login_info.txt") as login_info:
    data_table["email"] = email.read()
    prof_list = []
    for prof in professors.read().splitlines():
        prof_list.append((prof.split(",")[0], prof.split(",")[1]))
    data_table["professors"] = prof_list
    [username, password] = login_info.read().splitlines()
    data_table["username"] = username
    data_table["password"] = password

def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(data_table["username"], data_table["password"])
       for (p_email, name) in data_table["professors"]:
            msg = MIMEText(data_table["email"].format(name))
            msg['Subject'] = "Research"
            msg['From'] = data_table["username"]
            msg['To'] = p_email
            smtp_server.sendmail(data_table["username"], p_email, msg.as_string())

    print("emails sent")

# Fix LOGIN: https://www.google.com/settings/security/lesssecureapps 
send_email()