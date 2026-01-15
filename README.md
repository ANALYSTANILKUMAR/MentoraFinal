# Mentora Institute – Professional Tech Training Website

This is a **Flask-based web application** for Mentora Institute.  
It provides course details, sample videos, and an enquiry form that sends emails to both the applicant and the admin.

---

## 🚀 Features

- Home page with CTA ("Get Started Today")
- Courses page showcasing available programs
- Videos page with sample sessions
- Enquiry form with:
  - Name, Email, Phone, Course, Message
  - Sends confirmation email to student
  - Sends notification email to admin
- Fully responsive layout using CSS Grid & Flexbox
- Flash messages for form submission feedback

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Flask**
- **HTML5 / CSS3**
- **Jinja2 Templates**
- **SMTP (smtplib)** for sending emails

---

## ⚙️ Setup & Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mentora-flask.git
   cd mentora-flask
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

---

## ☁️ Deploy on Render

1. Push your project to a GitHub repository.
2. Go to [Render.com](https://render.com) → Create a **New Web Service**.
3. Connect your GitHub repo.
4. Select **Python** as the environment.
5. Render automatically installs from `requirements.txt`.
6. Add a **Start Command**:
   ```
   gunicorn app:app
   ```
7. Add environment variables:
   - `SENDER_EMAIL`
   - `SENDER_PASSWORD`
   - `ADMIN_EMAIL`

8. Click **Deploy** — your site will go live!

---

## 📄 Environment Variables Example

In Render → **Environment Settings**, set these:

```
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
ADMIN_EMAIL=your_email@gmail.com
```

*(These are kept private and not committed to GitHub.)*

---

## 🏁 Author

**Anil Kumar**  
Lead Data Analyst | Python Developer | Mentor  
📧 info@mentora.com  
🌐 [www.mentora.com](https://mentora.com)
