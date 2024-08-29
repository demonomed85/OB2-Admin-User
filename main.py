admins = []
users = []

class User():
    def __init__(self, name, ID):
        self.__ID = ID
        self.__name = name
        self.__access_level = 'User'

    def get(self, ID):
        return users[ID-1].get_name()

    def get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name
        print(f'Имя пользователя c ID = {self.get_id()} изменено на {self.__name}')

    def __set_access_level(self, access_level):
        self.__access_level = access_level
        print(f'Уровень доступа пользователя c ID = {self.get_id()} изменен на {self.__access_level}')

    def get_id(self):
        return self.__ID

class Admin(User):
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self.__access_level = 'Admin'
        admins.append(self)
        print(f'Cоздан Администратор {self.get_name()} с ID = {self.get_id()} и уровнем доступа = {self.__access_level}')

    def add_user(self, name, ID):
        users.append(User(name, ID))
        user_name = users[-1].get_name()  # Получаем имя последнего добавленного пользователя
        print(f'Пользователь {user_name} добавлен.')

    def delete_user(self, ID):
        index = ID - 1  # Приводим к индексу списка
        if 0 <= index < len(users):
            del users[index]
            print(f'Пользователь с ID = {ID} удален.')
        else:
            print(f'Пользователь с ID = {ID} не найден.')

# Пример использования
admin = Admin('Admin1', len(admins) + 1)
admins[0].add_user('User1', len(users) + 1)
