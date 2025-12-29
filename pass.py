import bcrypt

# list of plain-text passwords you want to hash
passwords = ["soumyadip", "default"]

for pwd in passwords:
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    print(f"Plain: {pwd}  -> Hashed: {hashed.decode()}")
