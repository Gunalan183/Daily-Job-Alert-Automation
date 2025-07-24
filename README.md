# 📬 Daily Job Alert Automation

This Python script automates the process of searching for relevant job listings based on your LinkedIn summary and delivers them to your inbox every morning at **9:00 AM**.

---

## 🚀 Features

- ⏰ Scheduled daily job alerts
- 🔍 Extracts keywords from your LinkedIn summary using NLP
- 🔎 Searches jobs using the **CareerJet API** (via [RapidAPI](https://rapidapi.com/letscrape-6bRBa3QguO5/api/careerjet))
- 📧 Sends job results directly to your email using **Gmail SMTP**
- 🔒 Secure and customizable

---

## 📁 File Structure

```
.
├── daily_job_alert.py   # Main automation script
├── README.md            # Project documentation
```

---

## 🛠️ Requirements

- Python 3.7+
- RapidAPI Account (Free)
- Gmail Account (App password enabled)
- Python Packages:
  - `requests`
  - `schedule`
  - `scikit-learn`

---

## 📦 Installation

1. **Clone this repository or download the script**

2. **Install dependencies**
   ```bash
   pip install requests schedule scikit-learn
   ```

3. **Create a [RapidAPI](https://rapidapi.com/) account**

   - Subscribe to [CareerJet API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/careerjet)
   - Copy your API key

4. **Enable App Password in Gmail** (if 2-Step Verification is on)
   - Visit: https://myaccount.google.com/apppasswords
   - Generate and use this app password in the script

---

## ⚙️ Configuration

Edit the following in `daily_job_alert.py`:

```python
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"
SENDER_EMAIL = "your.email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECEIVER_EMAIL = "your.email@gmail.com"
LINKEDIN_SUMMARY = """Your full LinkedIn summary here"""
```

---

## ▶️ Usage

Run the script from terminal:

```bash
python daily_job_alert.py
```

It will run continuously and send you an email with relevant job listings every day at **9:00 AM**.

---

## 📧 Example Email Output

```
Frontend Developer at Tech Innovators - https://careerjet.com/job1
React Developer at CodeHub - https://careerjet.com/job2
UI Engineer at StartupX - https://careerjet.com/job3
...
```

---

## 🚨 Notes

- **Do not share** your Gmail credentials or API key publicly.
- You can customize the time by modifying:  
  ```python
  schedule.every().day.at("09:00").do(daily_job_alert)
  ```
- Works best when run continuously (on your computer, a VPS, or cloud service like PythonAnywhere or Replit).

---

## 📌 To-Do / Ideas

- [ ] Add Telegram Bot integration
- [ ] Filter by company or salary
- [ ] Save jobs to Google Sheets or CSV
- [ ] Web GUI version (Flask)

---

## 👨‍💻 Author

**Gunalan A**  
Inspired by real job search struggles 😅
