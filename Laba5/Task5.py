import random
import string


def get_random_password(n=8, uniq=2) -> str: #uniq - максимальное количство дублей символа в пароле
    symbols = string.ascii_letters + string.digits
    password = random.sample(symbols, n, counts=[uniq for _ in symbols])
    return "".join(password)


print(get_random_password())
