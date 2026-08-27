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
