FILE = "users1.csv"


# ================= LOAD USERS =================
def load_users():
    users = {}
    try:
        with open(FILE, "r") as f:
            for line in f:
                u, p, pin, s, l = line.strip().split(",")
                users[u] = {
                    "password": p,
                    "pin": pin,
                    "status": int(s),
                    "locked": int(l)
                }
    except FileNotFoundError:
        pass
    return users


# ================= SAVE USERS =================
def save_users(users):
    with open(FILE, "w") as f:
        for u in users:
            f.write(
                u + "," +
                users[u]["password"] + "," +
                users[u]["pin"] + "," +
                str(users[u]["status"]) + "," +
                str(users[u]["locked"]) + "\n"
            )


# ================= REGISTER =================
def register(users):
    username = input("Enter username: ")

    if username in users:
        print("User already exists.")
        return

    password = input("Enter password: ")
    pin = input("Set 4-digit PIN: ")

    if not pin.isdigit() or len(pin) != 4:
        print("PIN must be exactly 4 digits.")
        return

    users[username] = {
        "password": password,
        "pin": pin,
        "status": 1,   # Active by default
        "locked": 0
    }

    save_users(users)
    print("Registration successful.")


# ================= LOGIN =================
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Account does not exist.")
        return

    if users[username]["locked"] == 1:
        print("Account is locked. Contact bank administrator.")
        return

    if users[username]["password"] == password:
        if users[username]["status"] == 0:
            print("Account is deactivated.")
            return

        print("Login successful. Welcome!")
    else:
        print("Invalid password.")


# ================= LOGOUT =================
def logout(users):
    print("Logout successful.")


# ================= DEACTIVATE ACCOUNT =================
def deactivate_account(users):
    username = input("Enter username: ")

    if username not in users:
        print("Account does not exist.")
        return

    if users[username]["locked"] == 1:
        print("Account is locked. Cannot deactivate.")
        return

    password = input("Enter password: ")

    if users[username]["password"] != password:
        print("Incorrect password.")
        return

    users[username]["status"] = 0
    save_users(users)
    print("Account deactivated successfully.")


# ================= DELETE ACCOUNT =================
def delete_account(users):
    username = input("Enter username: ")

    if username not in users:
        print("Account does not exist.")
        return

    if users[username]["locked"] == 1:
        print("Account is locked. Contact bank administrator.")
        return

    password = input("Enter password: ")

    if users[username]["password"] != password:
        print("Incorrect password.")
        return

    if users[username]["status"] == 1:
        print("Account must be deactivated before deletion.")
        return

    # 🔐 3 PIN Attempts
    attempts = 3
    while attempts > 0:
        pin = input("Enter PIN to confirm deletion: ")

        if users[username]["pin"] == pin:
            break
        else:
            attempts -= 1
            print("Incorrect PIN. Attempts left:", attempts)

    # 🚨 Lock account after 3 failed attempts
    if attempts == 0:
        users[username]["locked"] = 1
        save_users(users)
        print("Too many failed attempts. Account has been LOCKED.")
        return

    confirm = input("Type DELETE to permanently remove your account: ")

    if confirm != "DELETE":
        print("Deletion cancelled.")
        return

    del users[username]
    save_users(users)

    print("Account permanently deleted.")


# ================= MAIN MENU =================
def main():
    users = load_users()

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Deactivate Account")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            logout(users)
        elif choice == "4":
            deactivate_account(users)
        elif choice == "5":
            delete_account(users)
        elif choice == "6":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")


main()
