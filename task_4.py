"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
# O(n) из-за метода get_access
class users:
    users_count = 0

    def __init__(self, login, password, activate=False):
        users.users_count += 1
        self.id = users.users_count
        self.login = login
        self.password = password
        self.activate = activate

    def __str__(self):
        return f"\nID: {self.id}\nЛогин: {self.login}\nПароль: {self.password}\nАктивированно: {self.activate}"

    def activ(self):
        self.activate = True

    def get_access(self):
        if self.activate:
            print(f"Доступ для пользователя {self.login} к ресурсам разрешен")
        else:
            print(f"Доступ запрещен, необходимо активировать учетную запись!")

users_list = []
users_list.append(users('first', 'jhgkgjhg'))
users_list.append(users('second', 'kljgjhg', True))
users_list.append(users('third', '987kijh87', False))

users_list[1].get_access()
print(users_list[0])
users_list[0].activ()
users_list[0].get_access()