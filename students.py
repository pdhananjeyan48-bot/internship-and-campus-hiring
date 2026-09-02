from database import (
    get_all_internships,
    apply_for_internship,
    get_student_applications
)
def get_internships(search=""):
    internships = get_all_internships()
    search = search.strip().lower()
    if not search:
        return internships
    result = []
    for internship in internships:
        text = (
            internship["company"] +
            " " +
            internship["role"] +
            " " +
            internship["location"] +
            " " +
            internship["skills"]
        ).lower()
        if search in text:
            result.append(internship)
    return result
def apply_internship(student_id, internship_id):
    return apply_for_internship(
        student_id,
        internship_id
    )
def get_applications(student_id):
    return get_student_applications(
        student_id
    )
