import secrets
import string
#github: https://github.com/zxcresp

#y = True
#n = False
#============ASK USER FOR ALL PASSWORD INFORMATION============

def get_length():
    while True:
        length_password = int(input('Enter the password length: '))

        if 12 <= length_password <= 40:
            return length_password

        print('The password length must be between 12 and 40 characters')

def get_digits():
    while True:
        digits_yn = input('Do you want the digits? (Y/N): ')

        if digits_yn.lower() == 'y':
            return True
        if digits_yn.lower() == 'n':
            return False

        print('Enter only "y" or "n"')

def get_specials():
    while True:
        specials_yn = input('Do you want the special characters? (Y/N): ')

        if specials_yn.lower() == 'y':
            return True
        if specials_yn.lower() == 'n':
            return False

        print('Enter only "y" or "n"')

def get_letters():
    while True:
        letters_yn = input('Do you want the letters? (Y/N): ')

        if letters_yn.lower() == 'y':
            return True
        if letters_yn.lower() == 'n':
            return False

        print('Enter only "y" or "n"')

def create_chars(letters, digits, specials):
    chars = ""
    if letters:
        chars += string.ascii_letters
    if digits:
        chars += string.digits
    if specials:
        chars += string.punctuation

    return chars

def generate_password(length, chars):
    password = ""

    for _ in range(length):
        password += secrets.choice(chars)

    return password

#============FUNCTION CALLS============
while True:
    length = get_length()
    digits = get_digits()
    specials = get_specials()
    letters = get_letters()
    chars = create_chars(letters, digits, specials)
    if not chars:
        print("At least one character type must be selected")
        continue
    break

password = generate_password(length, chars)
print(password)
