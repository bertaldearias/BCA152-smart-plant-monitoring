
import os
import smtplib
import ssl
from email.message import EmailMessage

# Load local .env file
with open(".env", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ[key] = value.strip()

smtp_host = os.environ["SMTP_HOST"]
smtp_port = int(os.environ["SMTP_PORT"])
smtp_email = os.environ["SMTP_EMAIL"]
smtp_password = os.environ["SMTP_APP_PASSWORD"].replace(" ", "")

# Sample plant monitoring notification
message = EmailMessage()
message["From"] = smtp_email
message["To"] = smtp_email
message["Subject"] = "BCA152 Smart Plant Monitoring Test"

message.set_content(
    "Smart Plant Monitoring System\n"
    "Plant ID: PLANT_01\n"
    "Temperature: 29 C\n"
    "Humidity: 65%\n"
    "Soil Moisture: DRY\n"
    "Reason: Soil moisture below threshold\n"
    "Status: TEST NOTIFICATION\n"
    "\n"
    "This message uses simulated sensor readings."
)

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(
        smtp_host, smtp_port, context=context, timeout=15
    ) as server:
        server.login(smtp_email, smtp_password)
        server.send_message(message)

    print("SUCCESS: Gmail SMTP test email sent!")

except (OSError, smtplib.SMTPException) as error:
    print(f"FAILED: {type(error).__name__}")
    print("Check SMTP settings, credentials, and connection.")
