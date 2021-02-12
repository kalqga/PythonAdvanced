class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAIN = ("com", "bg", "org", "net")


def validate_email(mail):
    try:
        name, domain = mail.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        domain_name, extension = domain.split('.')
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")

    return True


email = input()

while not email == "End":

    if validate_email(email):
        print('Email is valid')

    email = input()
