FILE = "users.csv"


def load_users():
    users = {}
    try:
        f = open(FILE, "r")
        for line in f:
            u, p, s = line.strip().split(",")
            users[u] = {"password": p, "status": int(s)}
        f.close()
    except:
        pass
    return users


def save_users(users):
    f = open(FILE, "w")
    for u in users:
        f.write(u + "," + users[u]["password"] + "," + str(users[u]["status"]) + "\n")
    f.close()


def register(users):
    u = input("Enter username: ")
    if u in users:
        print("User already exists")
        return
    p = input("Enter password: ")
    users[u] = {"password": p, "status": 0}
    save_users(users)
    print("Registration successful")


def login(users,status):
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u in users and users[u]["password"] == p:
        if u in users:
            print("already logged in!")
        else:
         users[u]["status"] = 1
         save_users(users)
        print("Welcome user!")
    else:
        print("Invalid username or password")


def logout(users):
    u = input("Enter username: ")
    if u in users and users[u]["status"] == 1:
        users[u]["status"] = 0
        save_users(users)
        print("Logged out successfully")
    else:
        print("User not logged in or does not exist")


def main():
    users = load_users()
    while True:

     print("1. Login")
     print("2. Register")
     print("3. Logout")
     print("4. Exit")

     choice = input("Enter choice: ")

     if choice == "1":
        login(users)
     elif choice == "2":
        register(users)
     elif choice == "3":
        logout(users)
     elif choice == "4":
        print("program ended")
        break
     else:
        print("Invalid choice")


main()
