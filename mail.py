import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email(url, subject, sender, to, body, server):    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nThis message is regarding server:\n" + url +  "\n" + body
    html = """\
    <html>
    <head></head>
    <body>
    <p>Hi!<br>
       How are you?<br>
       This message is regarding server <a href=""" + url + """>link</a><br>""" + body + """
    </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP(server)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(sender, to, msg.as_string())
    s.quit()