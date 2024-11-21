import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = {}   # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля
        """
        return stored_password == hashlib.sha256(provided_password.encode('utf-8')).hexdigest()
    
    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
    
    @staticmethod
    def list_user():
        """
        Выводит список всех пользователей
        """
        return print("Users:\n",User.users)
    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя
        """
        if username in User.users:  # Проверяем, существует ли пользователь
            del User.users[username]  # Удаляем пользователя из словаря
            print(f"Пользователь {username} успешно удалён.")
            return True
        else:
            print(f"Пользователь {username} не найден.")
            return False
