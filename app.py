from nicegui import ui, app
users = {
    "admin@campushire.com": {
        "name": "Admin",
        "password": "admin123",
        "role": "Admin"
    },
    "recruiter@campushire.com": {
        "name": "Recruiter",
        "password": "recruiter123",
        "role": "Recruiter"
    }
}
jobs = [
    {
        "company": "TCS",
        "title": "Python Developer Intern",
        "location": "Chennai",
        "skills": "Python, SQL"
    },
    {
        "company": "Infosys",
        "title": "Data Science Intern",
        "location": "Bangalore",
        "skills": "Python, Machine Learning"
    },
    {
        "company": "Zoho",
        "title": "AI Intern",
        "location": "Coimbatore",
        "skills": "Python, AI"
    }
]
applications = []
def logout():
    app.storage.user.clear()
    ui.navigate.reload()
def login(email, password):
    email_text = email.value.strip()
    password_text = password.value
    if email_text in users:
        user = users[email_text]
        if user["password"] == password_text:
            app.storage.user["email"] = email_text
            app.storage.user["name"] = user["name"]
            app.storage.user["role"] = user["role"]
            ui.notify("Login successful", type="positive")
            ui.navigate.reload()
            return
    ui.notify("Invalid email or password", type="negative")
def register(name, email, password, role):
    name_text = name.value.strip()
    email_text = email.value.strip()
    password_text = password.value
    if not name_text or not email_text or not password_text:
        ui.notify("Please fill all fields", type="warning")
        return
    if email_text in users:
        ui.notify("Email already registered", type="negative")
        return
    users[email_text] = {
        "name": name_text,
        "password": password_text,
        "role": role.value
    }
    ui.notify("Registration successful", type="positive")
def apply_job(job):
    student = app.storage.user.get("email")
    for application in applications:
        if (
            application["student"] == student
            and application["job"] == job["title"]
        ):
            ui.notify("Already applied", type="warning")
            return
    applications.append({
        "student": student,
        "job": job["title"],
        "company": job["company"],
        "status": "Applied"
    })
    ui.notify(
        "Application submitted successfully",
        type="positive"
    )
def add_job(company, title, location, skills):
    if (
        not company.value.strip()
        or not title.value.strip()
        or not location.value.strip()
        or not skills.value.strip()
    ):
        ui.notify(
            "Please fill all job fields",
            type="warning"
        )
        return
    jobs.append({
        "company": company.value.strip(),
        "title": title.value.strip(),
        "location": location.value.strip(),
        "skills": skills.value.strip()
    })
    ui.notify(
        "Internship posted successfully",
        type="positive"
    )
    ui.navigate.reload()
def show_jobs():
    ui.label("Available Internships").classes(
        "text-2xl font-bold"
    )
    for job in jobs:
        with ui.card().classes("w-96"):
            ui.label(job["company"]).classes(
                "text-xl font-bold"
            )
            ui.label(
                "Position: " + job["title"]
            )
            ui.label(
                "Location: " + job["location"]
            )
            ui.label(
                "Skills: " + job["skills"]
            )
            ui.button(
                "Apply",
                on_click=lambda j=job: apply_job(j)
            )
def student_page():
    with ui.column().classes(
        "w-full items-center"
    ):
        ui.label("CampusHire").classes(
            "text-4xl font-bold"
        )
        ui.label("Student Dashboard").classes(
            "text-2xl font-bold"
        )
        ui.label(
            "Welcome, "
            + app.storage.user.get("name", "Student")
        )
        ui.button(
            "Logout",
            on_click=logout
        )
        show_jobs()
def recruiter_page():
    with ui.column().classes(
        "w-full items-center"
    ):
        ui.label("CampusHire").classes(
            "text-4xl font-bold"
        )
        ui.label("Recruiter Dashboard").classes(
            "text-2xl font-bold"
        )
        ui.label(
            "Welcome, "
            + app.storage.user.get("name", "Recruiter")
        )
        ui.button(
            "Logout",
            on_click=logout
        )
        ui.label("Post New Internship").classes(
            "text-xl font-bold"
        )
        company = ui.input(
            "Company Name"
        ).classes("w-80")
        title = ui.input(
            "Job Title"
        ).classes("w-80")
        location = ui.input(
            "Location"
        ).classes("w-80")
        skills = ui.input(
            "Required Skills"
        ).classes("w-80")
        ui.button(
            "Post Internship",
            on_click=lambda: add_job(
                company,
                title,
                location,
                skills
            )
        )
def admin_page():
    with ui.column().classes(
        "w-full items-center"
    ):
        ui.label("CampusHire").classes(
            "text-4xl font-bold"
        )
        ui.label("Admin Dashboard").classes(
            "text-2xl font-bold"
        )
        ui.label(
            "Welcome, "
            + app.storage.user.get("name", "Admin")
        )
        ui.button(
            "Logout",
            on_click=logout
        )
        ui.label("Registered Users").classes(
            "text-xl font-bold"
        )
        for email, user in users.items():
            ui.label(
                user["name"]
                + " | "
                + email
                + " | "
                + user["role"]
            )
        ui.label("Internships").classes(
            "text-xl font-bold"
        )
        for job in jobs:
            ui.label(
                job["company"]
                + " | "
                + job["title"]
                + " | "
                + job["location"]
            )
        ui.label("Applications").classes(
            "text-xl font-bold"
        )
        if not applications:
            ui.label("No applications yet")
        for application in applications:
            ui.label(
                application["student"]
                + " | "
                + application["company"]
                + " | "
                + application["job"]
                + " | "
                + application["status"]
            )
def login_page():
    with ui.column().classes(
        "w-full items-center"
    ):
        ui.label("CampusHire").classes(
            "text-4xl font-bold"
        )
        ui.label(
            "Internship and Campus Hiring Platform"
        ).classes("text-lg")
        ui.label("Login").classes(
            "text-2xl font-bold"
        )
        email = ui.input(
            "Email"
        ).classes("w-80")
        password = ui.input(
            "Password",
            password=True
        ).classes("w-80")
        ui.button(
            "Login",
            on_click=lambda: login(
                email,
                password
            )
        )
        ui.separator()
        ui.label(
            "New User Registration"
        ).classes("text-xl font-bold")
        name = ui.input(
            "Name"
        ).classes("w-80")
        register_email = ui.input(
            "Email"
        ).classes("w-80")
        register_password = ui.input(
            "Password",
            password=True
        ).classes("w-80")
        role = ui.select(
            ["Student", "Recruiter"],
            value="Student",
            label="Role"
        ).classes("w-80")
        ui.button(
            "Register",
            on_click=lambda: register(
                name,
                register_email,
                register_password,
                role
            )
        )
        ui.separator()
        ui.label(
            "Admin Login: admin@campushire.com / admin123"
        )
        ui.label(
            "Recruiter Login: recruiter@campushire.com / recruiter123"
        )
@ui.page("/")
def main_page():
    email = app.storage.user.get("email")
    if not email:
        login_page()
        return
    role = app.storage.user.get("role")
    if role == "Student":
        student_page()
    elif role == "Recruiter":
        recruiter_page()
    elif role == "Admin":
        admin_page()
    else:
        login_page()
ui.run(
    host="127.0.0.1",
    port=8765,
    title="CampusHire",
    storage_secret="campushire_secret_2026",
    reload=False
)
