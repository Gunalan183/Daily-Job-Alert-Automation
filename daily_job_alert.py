
import requests
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from sklearn.feature_extraction.text import CountVectorizer

# === CONFIGURATION ===

LINKEDIN_SUMMARY = """
Motivated Front-End Developer with experience in React.js, Node.js, HTML, CSS, JavaScript.
Passionate about building user-friendly, responsive applications.
"""

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"  # <-- Replace with your RapidAPI CareerJet key
LOCATION = "India"  # Change to your preferred location
NUM_KEYWORDS = 8

SENDER_EMAIL = "your.email@gmail.com"  # <-- Replace with your Gmail address
SENDER_PASSWORD = "your-app-password"  # <-- App password, NOT regular Gmail password
RECEIVER_EMAIL = "your.email@gmail.com"  # <-- You can send to self or another email

# === FUNCTION: Extract Keywords ===
def extract_keywords(summary, num_keywords=10):
    vectorizer = CountVectorizer(stop_words='english', max_features=num_keywords)
    X = vectorizer.fit_transform([summary])
    return vectorizer.get_feature_names_out()

# === FUNCTION: Get Jobs from CareerJet ===
def get_jobs(keyword, location="India"):
    url = "https://careerjet.p.rapidapi.com/job-search"
    querystring = {"keywords": keyword, "location": location, "page": "1", "affid": "rapidapi"}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "careerjet.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        jobs = response.json().get("jobs", [])
        return jobs[:5]
    except Exception as e:
        print(f"Error fetching jobs for keyword '{keyword}': {e}")
        return []

# === FUNCTION: Format and Send Email ===
def send_email(body, sender_email, sender_password, receiver_email):
    msg = MIMEText(body, "plain")
    msg["Subject"] = "🔔 Your Daily Job Alerts"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"Email failed: {e}")

# === FUNCTION: Main Daily Job Alert ===
def daily_job_alert():
    keywords = extract_keywords(LINKEDIN_SUMMARY, NUM_KEYWORDS)
    all_jobs = []

    for keyword in keywords:
        jobs = get_jobs(keyword, LOCATION)
        for job in jobs:
            all_jobs.append(f"{job['title']} at {job['company']} - {job['url']}\n")

    if all_jobs:
        job_message = "\n".join(all_jobs)
    else:
        job_message = "No jobs found today for your profile."

    send_email(job_message, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)

# === SCHEDULE ===
schedule.every().day.at("09:00").do(daily_job_alert)

print("⏳ Job alert service started... (will run at 09:00 AM daily)")
while True:
    schedule.run_pending()
    time.sleep(60)
