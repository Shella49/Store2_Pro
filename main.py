from classes.users import Customer, Admin
from classes.authenticationservice import AUthenticationService

# Создаём объект для работы с сессиями
auth_service = AUthenticationService()
# Создаем пользователей
admin = Admin(username="root", email="root@derkunov.ru", password ='12345678', admin_level=5)
customer1 = Customer(username="Mikhail", email="python@derkunov.ru", password ='1020304050', address="033 Russ Bur")
customer2 = Customer(username="Leonid", email="add@mail.ru", password ='111222333', address="Yaroslavl")
customer3 = Customer(username="Maria", email="swit@mail.ru", password ='0000009999', address="Boston")
customer4 = Customer(username="Mikhail", email="pyt2@derkunov.ru", password ='6767676', address="Moskva")

auth_service .register(admin.admin_level, admin.username, admin.email, admin.password)

auth_service .register(0, customer1.username, customer1.email, customer1.password) 
auth_service .register(0, customer2.username, customer2.email, customer2.password)
auth_service .register(0, customer3.username, customer3.email, customer3.password) 
auth_service .register(0, customer4.username, customer4.email, customer4.password)  
#
admin.list_user()
admin.delete_user(customer3.username)

auth_service.login(customer2.username, customer2.password)

auth_service.print_session()
auth_service.login(customer1.username, customer1.password)
auth_service.login(customer3.username, customer3.password)
#
auth_service.get_current_user()
auth_service.print_session()
auth_service.logout(customer2.username)
auth_service.logout(customer1.username)
auth_service.logout(customer3.username)
auth_service.print_session()
auth_service.get_current_user()