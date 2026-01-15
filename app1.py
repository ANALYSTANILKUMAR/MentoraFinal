from flask import Flask, render_template, request, flash, redirect, url_for
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

app = Flask(__name__)
app.secret_key = "mentora_secret_key"

# ============================
# 🔧 CONFIGURATION
# ============================
SENDER_EMAIL = "anilkumar22.analyst@gmail.com"   # Replace with your Gmail
SENDER_PASSWORD = "wwfi hdbz zwvi vpbi"          # Use Gmail App Password
ADMIN_EMAIL = "h.anilkumar2212@gmail.com"           # Same or different email to receive alerts

# ============================
# 🌐 ROUTES
# ============================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        course = request.form.get('course')
        message = request.form.get('message')

        try:
            # Send confirmation to student
            send_email_to_applicant(name, email, course)

            # Send notification to admin
            send_email_to_admin(name, email, phone, course, message)

            flash(f"Thank you {name}! We’ve received your enquiry for {course}.", "success")
        except Exception as e:
            flash(f"Error sending email: {e}", "danger")

        return redirect(url_for('enquiry'))

    return render_template('contact.html')


# ============================
# 📧 EMAIL FUNCTIONS
# ============================

def send_email_to_applicant(name, email, course):
    subject = f"Your Enquiry Confirmation – {course}"
    body = f"""
    <html>
    <body style="font-family: Arial; color:#333;">
        <h3 style="color:#1a237e;">Hi {name},</h3>
        <p>Thank you for showing interest in our <strong>{course}</strong> course!</p>
        <p>Our team will reach out to you shortly with complete details and schedules.</p>
        <br>
        <p>Warm regards,</p>
        <p><strong>Mentora Team</strong><br>
        📞 +91-XXXXXXXXXX<br>
        🌐 <a href="https://mentora.com">www.mentora.com</a></p>
    </body>
    </html>
    """
    send_email(email, subject, body, html=True)

def send_email_to_admin(name, email, phone, course, message):
    subject = f"New Course Enquiry: {course}"
    body = f"""
    <html>
    <body style="font-family: Arial; color:#333;">
        <h2 style="color:#ff6d00;">New Enquiry Received</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Course:</strong> {course}</p>
        <p><strong>Message:</strong> {message}</p>
        <br>
        <p>📩 Please follow up soon.</p>
    </body>
    </html>
    """
    send_email(ADMIN_EMAIL, subject, body, html=True)

def send_email(receiver_email, subject, body, html=False):
    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject

    mime_body = MIMEText(body, "html" if html else "plain")
    msg.attach(mime_body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

# ============================
# 🚀 RUN SERVER
# ============================
if __name__ == '__main__':
    app.run(debug=True)
