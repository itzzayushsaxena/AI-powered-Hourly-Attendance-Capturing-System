from cryptography.fernet import Fernet
from database import connect_database



def writeId(session_id):
    encoded_text = str(session_id).encode()
    key = Fernet.generate_key()

    f = Fernet(key)
    token = f.encrypt(encoded_text)
    with open('session_id.txt', 'w') as f:
        f.write(key.decode("utf-8"))
        f.write("\n")
        f.write(token.decode("utf-8"))
    return


def readId():
    with open('session_id.txt', 'r') as f:
        lines = f.readlines()
        key = lines[0].strip()
        encrpted_text = lines[1].strip()
    fer = Fernet(key.encode())
    session_id = (fer.decrypt(encrpted_text.encode())).decode("utf-8")
    result = connect_database()
    result[1].execute("select username from register where reg_id=%s", session_id)
    rows = result[1].fetchall()
    result[0].commit()
    result[0].close()
    return rows