import datetime

def greeting():
    """Функция приветствия в зависимости от времени суток"""
    now = datetime.datetime.now()
    if now.hour > 6 and now.hour <= 12 :
        return "Доброе утро"
    if now.hour > 12 and now.hour <= 18 :
        return "Добрый день"
    if now.hour > 18 and now.hour <= 24 :
        return "Добрый вечер"
    if now.hour >= 0 and now.hour <= 6 :
        return "Добрый ночи"
print(greeting())