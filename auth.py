from database import connect, hash_password
def register_user(name, email, password, role):
    con = connect()
    try:
        con.execute("""
            INSERT INTO users(name,email,password,role)
            VALUES(?,?,?,?)
        """, (
            name,
            email,
            hash_password(password),
            role
        ))
        con.commit()
        return True
    except:
        return False
    finally:
        con.close()
def login_user(email, password):
    con = connect()
    user = con.execute("""
        SELECT id,name,email,role
        FROM users
        WHERE email=? AND password=?
    """, (
        email,
        hash_password(password)
    )).fetchone()
    con.close()
    return user
