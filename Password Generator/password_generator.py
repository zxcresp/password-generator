import secrets
import string
#github: https://github.com/zxcresp
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

        if digits_yn.lower() == 'y' or digits_yn.lower() == 'n':
            break

        print('Enter only "y" or "n"')

def get_specials():
    while True:
        pass

def get_letters():
    while True:
        pass

lenght = get_length()
digits = get_digits()