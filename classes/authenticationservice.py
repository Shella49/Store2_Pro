from classes.users import User
import uuid
from datetime import datetime

class AUthenticationService:
    """
    Класс для управления регистрацией и аутентификацией пользователей
    """
    def __init__(self):
        self._session = []  # Список активных сессий
   
    def register(self, user_class, username, email, password):
        """
        Регистрация нового пользователя
        """
        # проверка имени
        if username in User.users:
            print(f'Пользователь с именем {username} уже зарегистрирован.')
            return False
        else:
            User.users[username] ={"user_class": user_class, "email": email, "пароль": User.hash_password(password)}
            print(f"Регистрация нового пользователя^ {username}")
            return True
      
    
    def login(self, username, password):
        """
        Аутентификация пользователя
        """
        if username in User.users:
            stored_password = User.users[username]['пароль']   # достаем пароль
            existing_session = next((session for session in self._session if session['username'] == username), None)

            if existing_session:
                    print(f'Пользователь {username} уже в системе.')
                    return True
            else:
                if User.check_password(stored_password , password):  # проверям пароль
                    # Если сессии нет, добавляем новую
                    
                    new_session = {
                            "username": username,
                            "session_id": str(uuid.uuid4()),  # Уникальный идентификатор
                            "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    self._session.append(new_session)  # Сохраняем пользователя в сессии
                    print(f'Пользователь {username} вошел в систему.')              
                    return True
                else:
                    print("Пароль введен неверно.")
                    return False
        else:
            print(f"Пользователь {username} не найден. Пожалуйста, пройдите регистрацию.")
            return False

    def logout(self,username):
        """
        Выход пользователя из системы
        """
        for session in self._session:
            if session['username'] == username:
                self._session.remove(session)
                print(f"Пользователь {username} вышел из системы.")
                return True
        else:
            print(f'Пользователь {username} не найден в сессии.')
            return False

      
    def print_session(self):
        return print(f'Текущая сессия: {self._session}') 
    
    def get_current_user(self):
        """
        Возвращает информацию о текущем вошедшем пользователе.
        """
        # Ищем сессию для пользователя
        existing_session = next((session for session in self._session if session['username'] == self._session[-1]['username']), None)
    
        if existing_session:
            username = existing_session['username']
            print(f"Текущий пользователь {username}.")
            return username  # Возвращаем имя пользователя или другую информацию о нем
        else:
            print("Нет активного пользователя.")
            return None

