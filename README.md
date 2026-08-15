#internship and campus hiring platform
from nicegui import ui
from database import create_database, connect
from auth import register_user, login_user
create_database()
current_user = None
content = ui.column().classes("w-full items-center")
def clear_page():
    content.clear()
