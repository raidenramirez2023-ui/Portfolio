from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymysql
from datetime import datetime

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',  # Default XAMPP password is empty
        database='portfolio_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
@app.route('/home')
def home():
    context = {
        'name': 'Ramirez',
        'role': 'Junior Web and Mobile Developer',
        'tagline': 'Building digital experiences.',
        'description': (
            'A Junior Web Developer and Mobile IT Student passionate about '
            'Python, MySQL, UI/UX, and clean code. I transform ideas into '
            'seamless, modern web applications.'
        ),
        'available_for_hire': True
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    context = {
        'name': 'Ramirez',
        'role': 'Junior Web and Mobile Developer',
        'intro': (
            'I am a passionate IT student nearing the end of my degree, '
            'with a strong foundation in modern web technologies. '
            'I love building clean, user-friendly interfaces and believe '
            'that good design is as important as good code.'
        ),
        'career_objective': (
            'Seeking a Junior Web Developer / IT Support role where I can apply '
            'my knowledge in Python, Flask, MySQL, and server management. '
            'I am eager to learn from experienced professionals, contribute '
            'to the team, and steadily grow my skills while helping deliver '
            'reliable and efficient technical solutions.'
        ),
        'tech_stack': ['HTML5', 'CSS', 'JavaScript', 'Dart', 'PHP'],
        'education': 'Bachelor of Science in Information Technology',
        'university': 'Laguna University - Santa Cruz, Laguna',
        'period': '2022 - Present'
    }
    return render_template('about.html', **context)


@app.route('/skills')
def skills():
    context = {
        'skill_categories': {
            'Frontend': ['HTML', 'CSS', 'JavaScript', 'Tailwind CSS', 'Bootstrap'],
            'Backend': ['Python', 'PHP', 'MySQL', 'Dart', 'Firebase'],
            'Mobile': ['Flutter', 'Responsive Design'],
            'Tools & Others': ['GitHub', 'VS Code', 'Figma']
        }
    }
    return render_template('skills.html', **context)


@app.route('/projects')
def projects():
    context = {
        'projects': [
            {
                'title': 'Web & Mobile E-Commerce Platform',
                'description': (
                    'A full-stack online shopping platform with user authentication, '
                    'product management, and cart functionality.'
                ),
                'technologies': ['Flutter', 'Dart', 'MySQL'],
                'demo': 'https://food-app-ruby-kappa.vercel.app/'
            },
        ]
    }
    return render_template('projects.html', **context)


@app.route('/experience')
def experience():
    context = {
        'education': {  
            'degree': 'Bachelor of Science in Information Technology',
            'university': 'Laguna University, Santa Cruz, Laguna',
            'period': '2022 - Present',
            'description': (
                'Currently pursuing a degree in IT with focus on web & mobile '
                'development and database management. Maintaining a strong '
                'academic record while actively engaging in programming projects.'
            )
        },
        'seeking': {
            'position': 'Seeking OJT Position',
            'role': 'Junior Web Development / IT Support',
            'year': '2025',
            'description': (
                'Looking for On-the-Job Training opportunities in web development '
                'to apply academic knowledge in a professional setting, '
                'contribute to real-world projects, and learn industry best practices.'
            )
        },
        'certifications': [
            {
                'title': 'Operating System Basics',
                'provider': 'Cisco Networking Academy',
                'date': 'October 2025'
            },
            {
                'title': 'Linux Essentials',
                'provider': 'Cisco Networking Academy',
                'date': 'December 2025'
            }
        ]
    }
    return render_template('experience.html', **context)


@app.route('/contact')
def contact():
    context = {
        'name': 'Raiden',
        'intro': (
            "I'm currently seeking OJT opportunities and open to discussing "
            "how I can contribute to your team. Feel free to reach out!"
        ),
        'email': 'ramirezraiden213@gmail.com',
        'github': 'https://github.com/raiden213',
        'linkedin': 'https://linkedin.com/in/raiden213'
    }
    return render_template('contact.html', **context)


@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Save to database
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO contact_message (name, email, message) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, message))
            connection.commit()

        # Email configuration
        sender_email = "ramirezraiden213@gmail.com"
        sender_password = "rmhj iuaq gipk thyp"
        receiver_email = "ramirezraiden213@gmail.com"

        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Contact Form Message from {name}"

        body = f"""
New message from your portfolio contact form:

Name: {name}
Email: {email}

Message:
{message}

---
Sent from Portfolio Contact Form
        """

        msg.attach(MIMEText(body, 'plain'))

        # Send email via Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        return jsonify({'success': True, 'message': 'Message sent successfully!'})

    except Exception as e:
        print(f"Error sending email: {str(e)}")  # For debugging
        return jsonify({'success': False, 'error': str(e)}), 500


# Optional: View all messages
@app.route('/admin/messages')
def view_messages():
    try:
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM contact_message ORDER BY created_at DESC")
                messages = cursor.fetchall()
        
        # Simple HTML display
        html = "<h1>Contact Messages</h1><table border='1'><tr><th>ID</th><th>Name</th><th>Email</th><th>Message</th><th>Date</th></tr>"
        for msg in messages:
            html += f"<tr><td>{msg['id']}</td><td>{msg['name']}</td><td>{msg['email']}</td><td>{msg['message']}</td><td>{msg['created_at']}</td></tr>"
        html += "</table>"
        return html
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)