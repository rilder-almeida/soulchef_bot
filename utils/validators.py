import re


def cpf_valid(cpf: str) -> bool:

    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    for NUM in range(9, 11):

        c = [int(n) for n in cpf[:NUM]]
        n = list(range(NUM + 1, 1, -1))
        s = sum(map(lambda i: c[i] * n[i], range(NUM)))

        dv = 0
        if (s % 11) >= 2:
            dv = 11 - (s % 11)

        if not int(cpf[NUM]) == dv:
            return False

    return True


def phone_valid(phone: str) -> bool:
    return bool(
        re.match(
            "^(?:(?:\+|00)?(55)\s?)?\(?[0]?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[1-9])[0-9]{3} ?\-?[0-9]{4}$",  # noqa
            phone,
        )
    )


def email_valid(email: str) -> bool:
    return bool(re.match("^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", email))  # noqa
