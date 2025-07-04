# Gmail Email Automation

This project allows you to send emails using Gmail via Python.

## Setup

1. Copy `.env.example` to `.env` and fill in your credentials.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python src/send_email.py
   ```

## Environment Variables

- `GMAIL_USER`: Your Gmail address
- `GMAIL_PASSWORD`: Your Gmail App Password (not your regular password)
- `RECIPIENT_EMAIL`: The recipient's email address

## Notes

- Use an App Password if you have 2FA enabled on your Gmail account.
- Do not share your `.env` file or credentials.
