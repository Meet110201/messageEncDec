from tkinter import messagebox, simpledialog, Tk
from random import choice
def encrypt(m):
    encrypted_list = []
    fake_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'r', 's', 't', 'u', 'v']
    for counter in range(0, len(m)):
        encrypted_list.append(m[counter])
        encrypted_list.append(choice(fake_letters))
    new_m = ''.join(encrypted_list)
    return new_m
def decrypt(m):
    even_letters = get_even_letters(m)
    new_m = ''.join(even_letters)
    return new_m
def get_t():
    t = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return t
def get_m():
    m = simpledialog.askstring('Message', 'Enter the secret message: ')
    return m
root = Tk()
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
        m = m + 'x'
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
    if t == 'e':
        m = get_m()
        print()
        encrypted = encrypt(m)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif t == 'd':
        m = get_m()
        decrypted = decrypt(m)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop()

import onetimepad
