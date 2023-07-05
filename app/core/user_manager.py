import hashlib
from config.user_class import User

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, username: str, password: str):
        """Register a new user to the system"""
        if self.find_user(username):
            raise ValueError("User already exists")
        
        user = User(username, password)
        self.users.append(user)
        response =  f"User {username} registered successfully"
        print(response)
        
    
    def login_user(self, username: str, password: str):
        """Login a user to the system"""
        user = self.find_user(username)

        if user:
            if self._check_password(password, user.password):
                response = {
                    "message": "User logged in successfully",
                    "user": user,
                    "status": "success",
                    "action": "LOGIN"
                }
            else:   
                response =  {
                    "message": "Incorrect password",
                    "status": "error",
                    user: None,
                    "action": "LOGIN"
                }
        else:
            response = {
                "message": "User not found",
                "status": "error",
                user: None,
                "action": "LOGIN"
            }

        print(response)

    def logout_user(self, username: str):
        """Logout a user from the system"""
        return {
            "message": f"User {username} logged out successfully",
            "status": "success",
            "action": "LOGOUT"
        }

    def delete_user(self, username: str):
        """Delete a user from the system"""
        user = self.find_user(username)

        if user:
            self.users.remove(user)
            return {
                "message": f"User {username} deleted successfully",
                "status": "success",
                "action": "DELETE"
            }


    def _check_password(self, password, hashed_password: str) -> bool:
        """Check if the password is correct"""
        return self._hash_password(password) == hashed_password

    def _hash_password(self, password: str) -> str:
        """Hash the password using bcrypt"""
        return hashlib.sha256(password.encode()).hexdigest()


    def find_user(self, username: str) -> User:
        """Find a user by username"""
        for user in self.users:
            if user.username == username:
                return {
                    "message": f"User {username} found",
                    "status": "success",
                    "user": user,
                    "action": "FIND"
                }

        return None