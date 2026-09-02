from database import (
    add_internship,
    delete_internship,
    get_recruiter_applications,
    update_application_status
)
def create_internship(
    recruiter_id,
    company,
    role,
    location,
    duration,
    skills,
    description
):
    fields = [
        company,
        role,
        location,
        duration,
        skills
    ]
    for field in fields:
        if not str(field).strip():
            return False, "Please fill all required fields."
    add_internship(
        recruiter_id,
        company.strip(),
        role.strip(),
        location.strip(),
        duration.strip(),
        skills.strip(),
        description.strip()
    )
    return True, "Internship published successfully."
def remove_internship(
    internship_id,
    recruiter_id
):
    return delete_internship(
        internship_id,
        recruiter_id
    )
def get_applicants(recruiter_id):
    return get_recruiter_applications(
        recruiter_id
    )
def change_application_status(
    application_id,
    recruiter_id,
    status
):
    return update_application_status(
        application_id,
        recruiter_id,
        status
    )
