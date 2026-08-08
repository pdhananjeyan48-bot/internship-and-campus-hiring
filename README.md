# internship-and-campus-hiring
from flask import Flask
app = Flask(__name__)
internships = [
    {
        "id": 1,
        "company": "Tech Solutions",
        "role": "Python Intern",
        "location": "Chennai",
        "duration": "3 Months"
    },
    {
        "id": 2,
        "company": "Data Works",
        "role": "Data Science Intern",
        "location": "Bangalore",
        "duration": "6 Months"
    },
    {
        "id": 3,
        "company": "Web Systems",
        "role": "Web Development Intern",
        "location": "Coimbatore",
        "duration": "3 Months"
    }
]
@app.route("/")
def home():
    internship_list = ""
    for job in internships:
        internship_list += f"""
        <div>
            <h2>{job['role']}</h2>
            <p>Company: {job['company']}</p>
            <p>Location: {job['location']}</p>
            <p>Duration: {job['duration']}</p>
            <hr>
        </div>
        """
    return f"""
    <html>
    <head>
        <title>Internship Campus Hiring Platform</title>
    </head>
    <body>
        <h1>Internship Campus Hiring Platform</h1>
        <h3>Available Internships</h3>
        {internship_list}
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
