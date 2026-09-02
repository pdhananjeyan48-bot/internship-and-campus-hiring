import sqlite3
import hashlib
from pathlib import Path
DB_PATH = Path(__file__).with_name("internship.db")
def connect():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def create_database():
    db = connect()
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS internships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recruiter_id INTEGER NOT NULL,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT NOT NULL,
            duration TEXT NOT NULL,
            skills TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (recruiter_id) REFERENCES users(id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            internship_id INTEGER NOT NULL,
            status TEXT DEFAULT 'Applied',
            applied_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(student_id, internship_id),
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (internship_id) REFERENCES internships(id)
        )
    """)
    admin = cur.execute(
        "SELECT id FROM users WHERE email=?",
        ("admin@campushire.com",)
    ).fetchone()
    if not admin:
        cur.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(?,?,?,?)
        """, (
            "System Administrator",
            "admin@campushire.com",
            hash_password("admin123"),
            "admin"
        ))
    recruiter = cur.execute(
        "SELECT id FROM users WHERE email=?",
        ("recruiter@campushire.com",)
    ).fetchone()
    if not recruiter:
        cur.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(?,?,?,?)
        """, (
            "Campus Recruiter",
            "recruiter@campushire.com",
            hash_password("recruiter123"),
            "recruiter"
        ))
        recruiter_id = cur.lastrowid
        internships = [
            (
                recruiter_id,
                "TechNova Solutions",
                "Python Developer Intern",
                "Bangalore",
                "3 Months",
                "Python, SQL, Git",
                "Work on Python applications and database projects."
            ),
            (
                recruiter_id,
                "DataSphere Analytics",
                "Data Analyst Intern",
                "Chennai",
                "6 Months",
                "Python, Pandas, Excel",
                "Analyze data and prepare business reports."
            ),
            (
                recruiter_id,
                "CloudBridge Technologies",
                "AI/ML Intern",
                "Hyderabad",
                "4 Months",
                "Python, Machine Learning, NumPy",
                "Assist in machine learning model development."
            ),
            (
                recruiter_id,
                "InnovateX Labs",
                "AI Research Intern",
                "Coimbatore",
                "3 Months",
                "Python, AI, Data Science",
                "Work on artificial intelligence research projects."
            )
        ]
        cur.executemany("""
            INSERT INTO internships
            (recruiter_id,company,role,location,duration,skills,description)
            VALUES(?,?,?,?,?,?,?)
        """, internships)
    db.commit()
    db.close()
def create_user(name, email, password, role):
    db = connect()
    try:
        db.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(?,?,?,?)
        """, (
            name.strip(),
            email.strip().lower(),
            hash_password(password),
            role
        ))
        db.commit()
        return True, "Account created successfully."
    except sqlite3.IntegrityError:
        return False, "Email already registered."
    finally:
        db.close()
def get_user_by_email(email):
    db = connect()
    row = db.execute("""
        SELECT * FROM users
        WHERE lower(email)=lower(?)
    """, (email.strip(),)).fetchone()
    db.close()
    return dict(row) if row else None
def verify_user(email, password):
    user = get_user_by_email(email)
    if not user:
        return None
    if user["password"] == hash_password(password):
        return user
    return None
def get_all_users():
    db = connect()
    rows = db.execute("""
        SELECT id,name,email,role
        FROM users
        ORDER BY id DESC
    """).fetchall()
    db.close()
    return [dict(row) for row in rows]
def add_internship(
    recruiter_id,
    company,
    role,
    location,
    duration,
    skills,
    description
):
    db = connect()
    db.execute("""
        INSERT INTO internships
        (
            recruiter_id,
            company,
            role,
            location,
            duration,
            skills,
            description
        )
        VALUES(?,?,?,?,?,?,?)
    """, (
        recruiter_id,
        company,
        role,
        location,
        duration,
        skills,
        description
    ))
    db.commit()
    db.close()
def get_all_internships():
    db = connect()
    rows = db.execute("""
        SELECT
            i.*,
            u.name AS recruiter_name
        FROM internships i
        JOIN users u
        ON i.recruiter_id = u.id
        ORDER BY i.id DESC
    """).fetchall()
    db.close()
    return [dict(row) for row in rows]
def delete_internship(internship_id, recruiter_id):
    db = connect()
    db.execute("""
        DELETE FROM applications
        WHERE internship_id=?
    """, (internship_id,))
    cur = db.execute("""
        DELETE FROM internships
        WHERE id=?
        AND recruiter_id=?
    """, (
        internship_id,
        recruiter_id
    ))
    db.commit()
    db.close()
    return cur.rowcount > 0
def apply_for_internship(student_id, internship_id):
    db = connect()
    try:
        db.execute("""
            INSERT INTO applications
            (student_id,internship_id,status)
            VALUES(?,?,?)
        """, (
            student_id,
            internship_id,
            "Applied"
        ))
        db.commit()
        return True, "Application submitted successfully."
    except sqlite3.IntegrityError:
        return False, "You have already applied."
    finally:
        db.close()
def get_student_applications(student_id):
    db = connect()
    rows = db.execute("""
        SELECT
            a.id,
            a.status,
            a.applied_at,
            i.company,
            i.role,
            i.location
        FROM applications a
        JOIN internships i
        ON a.internship_id = i.id
        WHERE a.student_id=?
        ORDER BY a.id DESC
    """, (student_id,)).fetchall()
    db.close()
    return [dict(row) for row in rows]
def get_recruiter_applications(recruiter_id):
    db = connect()
    rows = db.execute("""
        SELECT
            a.id,
            a.status,
            a.applied_at,
            u.name AS student_name,
            u.email AS student_email,
            i.company,
            i.role
        FROM applications a
        JOIN users u
        ON a.student_id = u.id
        JOIN internships i
        ON a.internship_id = i.id
        WHERE i.recruiter_id=?
        ORDER BY a.id DESC
    """, (recruiter_id,)).fetchall()
    db.close()
    return [dict(row) for row in rows]
def update_application_status(
    application_id,
    recruiter_id,
    status
):
    db = connect()
    cur = db.execute("""
        UPDATE applications
        SET status=?
        WHERE id=?
        AND internship_id IN (
            SELECT id
            FROM internships
            WHERE recruiter_id=?
        )
    """, (
        status,
        application_id,
        recruiter_id
    ))
    db.commit()
    db.close()
    return cur.rowcount > 0
def get_counts():
    db = connect()
    users = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]
    students = db.execute(
        "SELECT COUNT(*) FROM users WHERE role='student'"
    ).fetchone()[0]
    recruiters = db.execute(
        "SELECT COUNT(*) FROM users WHERE role='recruiter'"
    ).fetchone()[0]
    internships = db.execute(
        "SELECT COUNT(*) FROM internships"
    ).fetchone()[0]
    applications = db.execute(
        "SELECT COUNT(*) FROM applications"
    ).fetchone()[0]
    db.close()
    return {
        "users": users,
        "students": students,
        "recruiters": recruiters,
        "internships": internships,
        "applications": applications
    }
