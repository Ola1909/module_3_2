dog = '@'
endmail = ('.com', '.ru', '.net')

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if not (recipient.endswith(endmail) and sender.endswith(endmail)) or (recipient.count(dog) != 1 or sender.count(dog) != 1):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')  # 2

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')  # 3

    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')  # 4


#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')  # 1
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')   #2
#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')  #3
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')    #4





