import smtplib
from email.message import EmailMessage

# ----------------------------------------------------------
# Function :        Marvellous_send_mail
# Description:      Sends email using Gmail SMTP server
# ----------------------------------------------------------
def send_mail(sender, app_password, receiver, subject, body):
    # Step 1 : Create Email Object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password
    smtp.login(sender, app_password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close connection manually
    smtp.quit()

# ----------------------------------------------------------
# Function :        main
# Description :     Driver code 
# ----------------------------------------------------------
def main():

    # Always use separate temporary/testing account
    sender_email = "aniketdhole.test@gmail.com"

    # App password generated from Google account
    app_password = "zsxdkkbrmszoytnh"

    # Your second email for testing
    receiver_email = "aniketdhole1004@gmail.com"

    subject = "Test mail from python script"

    body = """Jay Ganesh,
    This is a test email sent using Marvellous Python.

    Regards,
    Marvellous Infosystems
    """

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Marvellous mail sent successfully")

# ----------------------------------------------------------
# Program entry point
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
