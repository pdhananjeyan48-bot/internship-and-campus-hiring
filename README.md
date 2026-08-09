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
from flask import Flask, request, redirect
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
applications = []
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
            <a href="/apply/{job['id']}">
                <button>Apply Now</button>
            </a>
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
@app.route("/apply/<int:job_id>", methods=["GET", "POST"])
def apply(job_id):
    job = next(
        (job for job in internships if job["id"] == job_id),
        None
    )
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        college = request.form["college"]
        applications.append({
            "name": name,
            "email": email,
            "college": college,
            "company": job["company"],
            "role": job["role"],
            "status": "Applied"
        })
        return redirect("/applications")
    return f"""
    <html>
    <head>
        <title>Apply for Internship</title>
    </head>
    <body>
        <h1>Internship Application</h1>
        <p>Company: {job['company']}</p>
        <p>Role: {job['role']}</p>
        <form method="POST">
            <label>Name</label><br>
            <input type="text" name="name" required>
            <br><br>
            <label>Email</label><br>
            <input type="email" name="email" required>
            <br><br>
            <label>College</label><br>
            <input type="text" name="college" required>
            <br><br>
            <button type="submit">Submit Application</button>
        </form>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)
