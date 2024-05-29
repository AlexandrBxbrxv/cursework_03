from datetime import datetime
from functions import get_data, censor


def main():
    executed = []

    for pos in get_data():
        if pos.get('state') == 'EXECUTED':
            executed.append(pos)

    new = sorted(executed, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)

    msg = []
    for pos in new[:5]:
        form = datetime.strptime(pos.get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        date = datetime.strftime(form, '%d.%m.%Y')

        operation = pos.get('operationAmount')
        sender = pos.get('from')
        receiver = pos.get('to')

        censored = censor(sender, receiver)

        msg.append (f'{date} {pos.get('description')}\n'
                f'{censored[0]} -> {censored[1]}\n'
                f'{operation.get('amount')} {operation.get('currency')['name']}')

    return '\n\n'.join(msg)


print(main())
