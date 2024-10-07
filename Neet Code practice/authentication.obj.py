
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)


class AuthSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username, password)
            print(f"User '{username}' registered successfully.")

    def login(self, username, password):
        if username in self.users and self.users[username].check_password(password):
            print(f"User '{username}' logged in successfully.")
        else:
            print("Login failed. Invalid username or password.")

    def change_password(self, username, old_password, new_password):
        if username in self.users and self.users[username].check_password(old_password):
            self.users[username] = User(username, new_password)
            print(f"Password for user '{username}' changed successfully.")
        else:
            print("Password change failed. Invalid username or password.")

user_instance = AuthSystem()
user_instance.register_user("Ather", "123456")
user_instance.login("Ather", "123456")
user_instance.change_password("Ather", "123456", "AtherisKool")
user_instance.register_user("Aadil", "Iamdumb")
user_instance.login("Aadil", "Iamdumb")
user_instance.change_password("Aadil", "Iamdumb", "whatami")