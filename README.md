#internship and campus hiring platform
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
current_user = None``
content = ui.column().classes("w-full items-center")
def clear_page():
    content.clear()
def logout():
    global current_user
    current_user = None``
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
