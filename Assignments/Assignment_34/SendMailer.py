import smtplib
from email.message import EmailMessage
import mimetypes
import os

# ----------------------------------------------------------
# Function :        Marvellous_send_mail
# Description:      Sends email using Gmail SMTP server
# ----------------------------------------------------------
def send_mail(sender, app_password, receiver, subject, body, file_attachments = None):
    try:
        # Step 1 : Create Email Object
        msg = EmailMessage()

        # Step 2 : Set mail headers
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Step 3 : Add mail body
        msg.set_content(body)

        if file_attachments is not None and len(file_attachments) > 0:
            for attachment in file_attachments:
                mimetype, _ = mimetypes.guess_type(attachment)
                mime_subtype = ""
                if mimetype is None:
                    mimetype = "application/octet-stream"

                mimetype, mime_subtype = mimetype.split("/")
                fobj = open(attachment, "rb")
                file_data = fobj.read()
                msg.add_attachment(file_data,maintype=mimetype,subtype=mime_subtype,
                    filename=os.path.basename(attachment))
                fobj.close()

        # Step 4 : Create SMTP SSL connection manually
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        # Step 5 : Login using Gmail + App password
        smtp.login(sender, app_password)

        # Step 6 : Send the email
        smtp.send_message(msg)

        # Step 7 : Close connection manually
        smtp.quit()
    except Exception as eobj:
        print(str(eobj))
