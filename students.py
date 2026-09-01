import sqlite3
from database import connect
def get_internships():
    db = connect()
    data = db.execute("""
        SELECT id, recruiter_id, company, role,
               location, duration, skills
        FROM internships
    """).fetchall()
    db.close()
    return data
def apply_internship(student_id, internship_id):
    db = connect()
    existing = db.execute("""
        SELECT id
        FROM applications
        WHERE student_id=? AND internship_id=?
    """, (
        student_id,
        internship_id
    )).fetchone()
    if existing:
        db.close()
        return False
    db.execute("""
        INSERT INTO applications
        (student_id, internship_id, status)
        VALUES (?, ?, ?)
    """, (
        student_id,
        internship_id,
        "Applied"
    ))
    db.commit()
    db.close()
    return True
def get_applications(student_id):
    db = connect()
    data = db.execute("""
        SELECT internships.company,
               internships.role,
               internships.location,
               applications.status
        FROM applications
        JOIN internships
        ON applications.internship_id = internships.id
        WHERE applications.student_id = ?
    """, (
        student_id,
    )).fetchall()
    db.close()
    return data
