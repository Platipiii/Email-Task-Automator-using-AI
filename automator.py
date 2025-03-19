import imaplib
import email
import spacy
import pandas as pd
from email.header import decode_header
import os

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Get email credentials securely from environment variables
EMAIL_USER = os.getenv("EMAIL_USER")  # Store your email in an environment variable
EMAIL_PASS = os.getenv("EMAIL_PASS")  # Store your password in an environment variable

# Ensure credentials are available
if not EMAIL_USER or not EMAIL_PASS:
    raise ValueError("Please set the EMAIL_USER and EMAIL_PASS environment variables.")

# Connect to email server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL_USER, EMAIL_PASS)
mail.select("inbox")

# Fetch emails
status, messages = mail.search(None, "UNSEEN")
email_ids = messages[0].split()

extracted_tasks = []

for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            subject = subject.decode(encoding) if encoding else subject
            
            # Extract email content
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if "plain" in content_type:
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()
            
            # NLP processing to categorize task
            doc = nlp(body)
            categories = []
            if "meeting" in body.lower():
                categories.append("Meeting")
            if "urgent" in body.lower() or any(token.text.lower() in ["asap", "immediately"] for token in doc):
                categories.append("Urgent")
            if "follow up" in body.lower():
                categories.append("Follow-up")
            
            extracted_tasks.append({"Subject": subject, "Category": ", ".join(categories), "Content": body[:100]})

# Save tasks to a CSV file
df = pd.DataFrame(extracted_tasks)
df.to_csv("tasks.csv", index=False)

print("Tasks extracted and saved!")

