import re
import smtplib
from email.message import EmailMessage
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import PyPDF2


def read_pdf(filename):
    with open(filename, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
    return text.strip()


essay = read_pdf("sample_essay.pdf")

if len(essay.split()) > 500:
    essay = " ".join(essay.split()[:500])

def save_pdf(filename, content):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    doc.build([Paragraph(content, styles["Normal"])])

save_pdf("essay.pdf", essay)


verbs = re.findall(r'\b\w+(?:ed|ing|s)\b', essay)
nouns = re.findall(r'\b[A-Z]?[a-z]+\b', essay)
prepositions = re.findall(r'\b(?:in|on|at|by|for|with|about|against|between|into|through|during|before|after|above|below|to|from|up|down|over|under|again|further|then|once)\b', essay)
pronouns = re.findall(r'\b(?:I|you|he|she|it|we|they|me|him|her|us|them|my|your|his|its|our|their|mine|yours|hers|ours|theirs)\b', essay)


save_pdf("verbs.pdf", " ".join(verbs))
save_pdf("nouns.pdf", " ".join(nouns))
save_pdf("prepositions.pdf", " ".join(prepositions))
save_pdf("pronouns.pdf", " ".join(pronouns))


sender = "dharshanprogrammerprogress@gmail.com"
password = "kbhi zfvr jtwv thwv"
receiver = "dharshanprogrammerprogress@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Essay and Word Category Files"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Attached are the essay and word category files.")

for file in ["essay.pdf", "verbs.pdf", "nouns.pdf", "prepositions.pdf", "pronouns.pdf"]:
    with open(file, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=file)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent successfully!")
