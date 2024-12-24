import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Email Account Credentials
EMAIL_ADDRESS = 'sonipriyanshi.ps99@gmail.com'
EMAIL_PASSWORD = 'txfg vjge grxh fyxh'  # Replace with your App Password

# Create and Send Email
def send_email(subject, body, to_emails):
    # Create message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(to_emails)  # Multiple recipients
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.ehlo()  # Identify with the server
            smtp.starttls()  # Encrypt the connection
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login
            smtp.sendmail(EMAIL_ADDRESS, to_emails, msg.as_string())  # Send email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage
send_email(
    subject="Python Notification",
    body="Hi there! This is a test email sent from Python.",
    to_emails=["rhpsoni@gmail.com"]
)
