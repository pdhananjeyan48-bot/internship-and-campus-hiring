from database import connect
def add_internship(
    recruiter_id,
    company,
    role,
    location,
    duration,
    skills
):
    db = connect()
    db.execute(
        """
        INSERT INTO internships
        (recruiter_id,company,role,location,duration,skills)
        VALUES (?,?,?,?,?,?)
        """,
        (
            recruiter_id,
            company,
            role,
            location,
            duration,
            skills
        )
    )
    db.commit()
    db.close()
def get_applicants(recruiter_id):
    db = connect()
    data = db.execute(
        """
        SELECT users.name,
               users.email,
               internships.company,
               internships.role,
               applications.status
        FROM applications
        JOIN users
        ON applications.student_id=users.id
        JOIN internships
        ON applications.internship_id=internships.id
        WHERE internships.recruiter_id=?
        """,
        (recruiter_id,)
    ).fetchall()
    db.close()
    return data
