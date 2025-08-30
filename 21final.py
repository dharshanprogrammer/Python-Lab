import re
import smtplib
from email.message import EmailMessage

def tokenize_c_program(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        tokens = re.findall(r'\w+|[{}();=,+*/-]', code)
        rows = [tokens[i:i+5] for i in range(0, len(tokens), 5)]
        return rows
    except Exception as e:
        
        print("Error reading or tokenizing file:", e)
        return []

def send_email(body, to_email):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = 'C Program Tokens'
        msg['From'] = 'dharshan.dev@gmail.com'
        msg['To'] = to_email

     
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('dharshanprogrammerprogress@gmail.com', 'kbhi zfvr jtwv thwv')  
            server.send_message(msg)

        print("Email sent to", to_email)
    except Exception as e:
        print(" Failed to send email:", e)


tokens = tokenize_c_program('sample.c')
if tokens:
    token_text = "\n".join(["\t".join(row) for row in tokens])
    send_email(token_text, 'dharshanprogrammerprogress@gmail.com')  
else:
    print("No tokens generated from the file.")