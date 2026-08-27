INTERNSHIP AND CAMPUS HIRING PLATFORM
PROJECT REVIEW
The Internship and Campus Hiring Platform is a Python-based web application designed to connect students with internship opportunities and help recruiters manage internship applications
The system provides multi-user login with different roles such as Student, Recruiter, and Admin. Each user gets access to features according to their role.
OBJECTIVES
Provide a simple platform for students to find internships.
Allow students to apply for available internships
Allow recruiters to post internship opportunities
Allow recruiters to view applicants
Provide secure user registration and login
Store user, internship, and application information in a database
USER ROLES
Student
Register and login
View available internships
Apply for internships
View application status
Recruiter
Register and login
Add internship opportunities
View applicants
Admin
Login
View/manage registered users
TECHNOLOGIES USED
Python
NiceGUI – Frontend and web interface
SQLite – Database
VS Code – Development environment
GitHub – Version control
The project is developed using Python and NiceGUI without separate HTML files.
PROJECT STRUCTURE
Internship-And-Campus-Hiring-Platform/
│
├── app.py
├── auth.py
├── database.py
├── students.py
├── recruiter.py
├── requirements.txt
├── internship.db
│
└── diagrams/
    ├── ER_Diagram.drawio
    ├── System_Diagram.drawio
    └── Architecture_Diagram.drawio
MAIN MODULES
File
Description
app.py
Main application and user interface
auth.py
Registration and login
database.py
Database connection and tables
students.py
Student internship and application functions
recruiter.py
Internship posting and applicant functions
internship.db
SQLite database
DATABASE
The application uses SQLite to store:
Users
Internships
Applications
The main relationships are:
Users
  │
  ├── Internships
  │
  └── Applications
          │
          └── Internships
HOW TO RUN
1. Install Python
Make sure Python is installed on your computer.
2. Open the project in VS Code
Open the project folder in VS Code
3. Install the required library
Open the VS Code terminal and run:
python -m pip install -r requirements.txt
4. Run the application
python app.py
5. Open the website
Open the local address shown in the terminal, for example:
http://127.0.0.1:8080
   SYSTEM OVERFLOW
User
  ↓
Register / Login
  ↓
Select User Role
  ↓
Student / Recruiter / Admin
  ↓
Role-Based Features
  ↓
SQLite Database
   PROJECT DIAGRAMS
The project includes:
ER Diagram – Represents the database entities and relationships
System Diagram – Represents interaction between users and the platform
Architecture Diagram – Represents the structure of the Python modules and database
   FUTURE ENHANCEMENT
Resume upload and management
Internship search and filtering
Email notifications
Recruiter approval system
Student profile management
Application deadline notifications
Improved admin dashboard
 CONCLUSION
The Internship and Campus Hiring Platform provides a simple and organized solution for managing internship opportunities and applications. The modular Python structure makes the project easy to understand, maintain, and extend
