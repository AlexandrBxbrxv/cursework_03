import json


def get_data():
    with open('../operations.json', 'rt', encoding='UTF-8') as file:
        j_data = file.read()

    data = json.loads(j_data)
    return data


def censor(sender, receiver):
    if type(sender) is not str:
        censored_sender = 'Неизвестный'
    else:
        sender_nums = [i for i in str(sender).split(' ') if i.isnumeric()]
        sender_nums = str(*sender_nums)

        box = []
        count = 0
        stars = len(sender_nums) - 10

        sender_limbs = sender_nums[:6] + ('*' * stars) + sender_nums[-4:]

        for i in sender_limbs:
            box.append(i)
            count += 1
            if count == 4:
                count -= 4
                box.append(' ')
        box.pop()

        box = ''.join(box)
        censored_sender = box

    censored_receiver = [i for i in str(receiver).split(' ') if i.isnumeric()]
    censored_receiver = f'**{(str(*censored_receiver)[-4:])}'

    return censored_sender, censored_receiver
