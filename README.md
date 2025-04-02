Overview

The Email-Task Automator is a Python script designed to automatically extract and categorize tasks
from unread email messages. It leverages AI-powered natural language processing (NLP) using the
spaCy library to identify task categories from email content, such as meetings, urgent actions, and
follow-ups.
Features
- Automated Email Parsing: Connects securely to your Gmail inbox to fetch unread emails.
- Task Extraction: Identifies key phrases and keywords to categorize tasks (Meeting, Urgent,
Follow-up).
- NLP Integration: Uses spaCy's NLP model to enhance text processing and categorize content
accurately.
- CSV Output: Saves extracted tasks, including subject, category, and a snippet of the content, to a
CSV file.
- Secure Login: Uses environment variables to manage email credentials securely.

Features

- Automated Email Parsing: Connects securely to your Gmail inbox to fetch unread emails.
- Task Extraction: Identifies key phrases and keywords to categorize tasks (Meeting, Urgent,
Follow-up).
- NLP Integration: Uses spaCy's NLP model to enhance text processing and categorize content
accurately.
- CSV Output: Saves extracted tasks, including subject, category, and a snippet of the content, to a
CSV file.
- Secure Login: Uses environment variables to manage email credentials securely.

Requirements

- Python 3.x
- Libraries: imaplib, email, spacy, pandas, os
- spaCy model: en_core_web_sm

Setup Instructions

1. Environment Setup:
 - Set up your environment variables for email credentials:
 export EMAIL_USER="your_email@example.com"
 export EMAIL_PASS="your_password"
2. Install Required Libraries:
 pip install spacy pandas
 python -m spacy download en_core_web_sm
3. Run the Script:
 python automator.py
4. Output:
 - A CSV file named tasks.csv will be generated containing extracted tasks.

How It Works

1. Connects to your Gmail inbox and fetches unread emails.
2. Extracts the subject and content of each email.
3. Uses NLP to detect keywords and phrases indicating task categories.
4. Saves the categorized tasks into a structured CSV file for easy reference.

Potential Use Cases

- Personal Task Management: Automatically sorts incoming tasks from your inbox.
- Team Coordination: Quickly categorize tasks from team emails for better productivity.
- Email Prioritization: Identifies urgent messages that need immediate attention.
Contact
For any questions or improvements, feel free to reach out!
