from random import choice
import onetimepad,string,math,numpy,random,pyotp

def decrypt(m):
    even_letters = get_even_letters(m)
    new_m = ''.join(even_letters)
    return new_m
def get_t():
    t = input('\nENTER THE OPTION to Encrypted(e) or Decrypted(d) or Quit(q) : ')
    return t
def get_m():
    m = input('\nENTER MESSAGE : ')
    return m
def is_even(number):
    return number % 2 == 0
def get_even_letters(m):
    even_letters = []
    for counter in range(0, len(m)):
        if is_even(counter):
            even_letters.append(m[counter])
    return even_letters
def get_odd_letters(m):
    odd_letters = []
    for counter in range(0, len(m)):
        if not is_even(counter):
            odd_letters.append(m[counter])
    return odd_letters
def swap_letters(m):
    letter_list = []
    if not is_even(len(m)):
        # printing letters
        letters = string.ascii_letters
        f_l= ''.join(random.choice(letters) for i in range(3))
        # printing digits
        letters = string.digits
        f_d = ''.join(random.choice(letters) for i in range(2))
        m = m + f_d + f_l
    else:
        # printing letters
        letters = string.ascii_letters
        f_l= ''.join(random.choice(letters) for i in range(2))
        # printing digits
        letters = string.digits
        f_d = ''.join(random.choice(letters) for i in range(2))
        m = m + f_d + f_l
    even_letters = get_even_letters(m)
    odd_letters = get_odd_letters(m)
    for counter in range(0, int(len(m)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
        new_m = ''.join(letter_list)
    return new_m
def encrypt(m):
    swapped_m = swap_letters(m)
    encrypted_m = ''.join(reversed(swapped_m))
    return encrypted_m
def decrypt(m):
    unreversed_m = ''.join(reversed(m))
    decrypted_m = swap_letters(unreversed_m)
    return decrypted_m
while True: 
    t = get_t()
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    if t == 'e':
        m = get_m()
        encrypted = encrypt(m)
        cipher = onetimepad.encrypt(encrypt(m), 'random')
        print('\nCiphertext of the secret message is:', cipher)
        print("\nCurrent OTP : ", totp.now())
        pin = totp.now()
        print('\n')
    
    elif t == 'd':
        x = input('\nENTER OTP : ')
        if x == pin:
            m = get_m()
            msg = onetimepad.decrypt(cipher, 'random')
            m = msg
            decrypted = decrypt(m)
            print('\nPlaintext of the secret message is:', decrypted)
        else:
            print('\n******INVALID OTP*******\n')
    elif t == 'q':
        break