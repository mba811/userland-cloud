import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app
from app import Q


@Q.job(timeout=60000)
def send_confirm_email(email_address, token_url):
    smtp_username = current_app.config["MAIL_USERNAME"]
    smtp_password = current_app.config["MAIL_PASSWORD"]
    host = current_app.config["MAIL_SERVER"]
    port = current_app.config["MAIL_PORT"]
    tls = current_app.config["MAIL_USE_TLS"]
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Account Email Verification"
    msg["From"] = email.utils.formataddr(("Holepunch NOREPLY", "noreply@holepunch.io"))
    msg["To"] = email_address

    body_text = "Click this link to register your account: " + token_url
    body_html = f"""
<html>
<head></head>
<body>
 <h1>Holepunch email confirmation</h1>
    <p>Visit <a href="{token_url}">{token_url}</a> to register your account.</p>
    </body>
</html>
"""
    part1 = MIMEText(body_text, "plain")
    part2 = MIMEText(body_html, "html")
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(host, port)
        if tls:
            server.ehlo()
            server.starttls()
            server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail("noreply@holepunch.io", email_address, msg.as_string())
        server.close()
    except Exception as e:
        raise (e)