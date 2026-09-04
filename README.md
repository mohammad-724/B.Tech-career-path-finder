live url: https://b-tech-career-path-finder.onrender.com 

github deploy link:  https://mohammad-724.github.io/B.Tech-career-path-finder/

B.Tech Career Path Finder

A professional Flask-based web application that helps B.Tech students explore career options based on their engineering branch. The application provides a simple step-by-step interface to select a branch, explore suitable career paths, and view career details.

✨ Features
Branch-based career exploration
Supports ECE, CSE, EEE and MECH
Separate page/interface for every step
Career cards with detailed information
Browser Back button support
Built-in Back navigation buttons
Responsive and professional UI
Hover effects and smooth transitions
Breadcrumb navigation
404 error page
Flask-based routing
Deployed as a live web application
🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Jinja2 Templates
Deployment
Git
GitHub
Render
Gunicorn
Development Tools
Visual Studio Code
Command Prompt / PowerShell
Web Browser
📁 Project Structure
BTech-Career-Path-Finder/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── branch.html
│   ├── careers.html
│   ├── career.html
│   └── 404.html
│
└── static/
    ├── style.css
    └── script.js
⚙️ How It Works
Home Page
    ↓
Select Engineering Branch
    ↓
View Career Options
    ↓
Select Career
    ↓
View Career Details

The application uses Flask routes to dynamically display branch and career information while Jinja2 is used for rendering HTML templates.

💻 Run Locally
1. Clone the repository
git clone https://github.com/yourusername/BTech-Career-Path-Finder.git
cd BTech-Career-Path-Finder
2. Install dependencies
py -m pip install -r requirements.txt
3. Run the Flask application
py app.py

Open:

http://127.0.0.1:5000
📦 Requirements
Flask>=3.0,<4.0
gunicorn
🌐 Deployment

This project was deployed using Render Web Service.

Deployment configuration

Build Command

pip install -r requirements.txt

Start Command

gunicorn app:app

The project was first pushed to GitHub and then connected to Render for deployment.

🔄 Deployment Workflow
Develop in VS Code
       ↓
Test Flask App Locally
       ↓
Push Project to GitHub
       ↓
Connect GitHub Repository to Render
       ↓
Render Installs Dependencies
       ↓
Gunicorn Starts Flask App
       ↓
Live Website
🎯 Purpose

The project is designed to help B.Tech students quickly understand career opportunities available after graduation and explore possible career paths according to their engineering specialization.

🔮 Future Improvements
Add more engineering branches
Add more career roles
Search and filter functionality
Career skill requirements
Salary and job-market information
Personalized career recommendations
Database integration
User login and saved career paths
👨‍💻 Author

Mohammad Azmath Ali

⭐ Project Highlights

Python + Flask | HTML | CSS | JavaScript | Jinja2 | Git | GitHub | Gunicorn | Render | Responsive UI | Multi-page Navigation | Live Deployment
