from nicegui import ui
from database import create_database, connect
from auth import register_user, login_user
from students import (
    get_internships,
    apply_internship,
    get_applications
)
from recruiter import (
    add_internship,
    get_applicants
)
create_database()
current_user = None
content = ui.column().classes("w-full items-center")
def clear_page():
    content.clear()
def logout():
    global current_user
    current_user = None
    login_page()
def login_page():
    clear_page()
    with content:
        ui.label(
            "Internship and Campus Hiring Platform"
        ).classes("text-3xl font-bold")
        ui.label(
            "Login"
        ).classes("text-2xl")
        email = ui.input(
            "Email"
        ).classes("w-80")
        password = ui.input(
            "Password",
            password=True
        ).classes("w-80")def login():
            global current_user
            user = login_user(
                email.value,
                password.value
            )
            if user:
                current_user = user
                if user[3] == "Student":
                    student_page()
                elif user[3] == "Recruiter":
                    recruiter_page()
                else:
                    admin_page()
            else:
                ui.notify(
                    "Invalid email or password",
                    type="negative"
                )
        ui.button(
            "Login",
            on_click=login
        )
        ui.button(
            "Create New Account",
            on_click=register_page
        )
        def register_page():
    clear_page()
    with content:
        ui.label(
            "Create Account"
        ).classes("text-3xl font-bold")
        name = ui.input(
            "Full Name"
        ).classes("w-80")
        email = ui.input(
            "Email"
        ).classes("w-80")
        password = ui.input(
            "Password",
            password=True
        ).classes("w-80")
        role = ui.select(
            ["Student", "Recruiter"],
            value="Student",
            label="Account Type"
        ).classes("w-80")
def register():
            if not name.value or not email.value or not password.value:
                ui.notify(
                    "Please fill all fields",
                    type="negative"
                )
                return
            result = register_user(
                name.value,
                email.value,
                password.value,
                role.value
            )
            if result:
                ui.notify(
                    "Registration successful"
                )
                login_page()
            else:
                ui.notify(
                    "Email already registered",
                    type="negative"
                )
        ui.button(
            "Register",
            on_click=register
        )
        ui.button(
            "Back to Login",
            on_click=login_page
        )
def student_page():
    clear_page()
    with content:
        ui.label(
            "Student Dashboard"
        ).classes("text-3xl font-bold")
        ui.label(
            "Welcome, " + current_user[1]
        ).classes("text-xl")
        ui.button(
            "Logout",
            on_click=logout
        )
        ui.separator()
        ui.label(
            "Available Internships"
        ).classes("text-2xl font-bold")
        internships = get_internships()
        if not internships:
            ui.label(
                "No internships available"
            )
            for internship in internships:
            with ui.card().classes("w-96"):
                ui.label(
                    internship[2]
                ).classes("text-xl font-bold")
                ui.label(
                    "Company: " + internship[1]
                )
                ui.label(
                    "Location: " + internship[3]
                )
                ui.label(
                    "Duration: " + internship[4]
                )
                ui.label(
                    "Skills: " + internship[5]
                )
                def apply(i=internship[0]):
                    result = apply_internship(
                        current_user[0],
                        i
                    )
                    if result:
                        ui.notify(
                            "Application submitted successfully"
                        )
                    else:
                        ui.notify(
                            "You already applied",
                            type="warning"
                        )
                ui.button(
                    "Apply Now",
                    on_click=apply
                )
                ui.separator()
        ui.label(
            "My Applications"
        ).classes("text-2xl font-bold")
        applications = get_applications(
            current_user[0]
        )
        if not applications:
            ui.label(
                "No applications yet"
            )
        for application in applications:
            with ui.card().classes("w-96"):
                ui.label(
                    "Company: " + application[0]
                )
                ui.label(
                    "Role: " + application[1]
                )
                ui.label(
                    "Location: " + application[2]
                )
                ui.label(
                    "Status: " + application[3]
                )
                def recruiter_page():
    clear_page()
    with content:
        ui.label(
            "Recruiter Dashboard"
        ).classes("text-3xl font-bold")
        ui.label(
            "Welcome, " + current_user[1]
        ).classes("text-xl")
        ui.button(
            "Logout",
            on_click=logout
        )
        ui.separator()
        ui.label(
            "Post Internship"
        ).classes("text-2xl font-bold")
        company = ui.input(
            "Company Name"
        ).classes("w-80")
        role = ui.input(
            "Job Role"
        ).classes("w-80")
        location = ui.input(
            "Location"
        ).classes("w-80")
        duration = ui.input(
            "Duration"
        ).classes("w-80")
        skills = ui.input(
            "Required Skills"
        ).classes("w-80")
        def post_internship():
            if not company.value or not role.value:
                ui.notify(
                    "Enter company and job role",
                    type="negative"
                )
                return
            add_internship(
                current_user[0],
                company.value,
                role.value,
                location.value,
                duration.value,
                skills.value
            )
            ui.notify(
                "Internship posted successfully"
            )
            company.value = ""
            role.value = ""
            location.value = ""
            duration.value = ""
            skills.value = ""
        ui.button(
            "Post Internship",
            on_click=post_internship
        )
        ui.separator()
        ui.label(
            "Applicants"
        ).classes("text-2xl font-bold")
        applicants = get_applicants(
            current_user[0]
        )
        if not applicants:
            ui.label(
                "No applicants yet"
            )
