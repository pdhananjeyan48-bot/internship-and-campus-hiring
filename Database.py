import sqlite3
import hashlib
DATABASE = "internship.db"
def connect():
    return sqlite3.connect(DATABASE)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def create_database():
    con = connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS internships(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recruiter_id INTEGER,
            company TEXT,
            role TEXT,
            location TEXT,
            duration TEXT,
            skills TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS applications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            internship_id INTEGER,
            status TEXT
        )
    """)
    admin = cur.execute(
        "SELECT id FROM users WHERE email=?",
        ("admin@gmail.com",)
    ).fetchone()
    if not admin:
        cur.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(?,?,?,?)
        """, (
            "Admin",
            "admin@gmail.com",
            hash_password("admin123"),
            "Admin"
        ))
    con.commit()
    con.close()
