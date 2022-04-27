import random, numpy, onetimepad, string,math

print('\n\n*********[ CRYTOGRAPGHY IN PYTHON ]***********\n\n')

str = input("Enter the message : ")  
print(str)

output = ''
i = 0
while i < len(str):
        if i + 1 < len(str):
                output = output + str[i + 1]
                output = output + str[i]
        i = i + 2
r_str = ''.join(reversed(output))

# printing letters
letters = string.ascii_letters
f_l= ''.join(random.choice(letters) for i in range(3))
# printing digits
letters = string.digits
f_d = ''.join(random.choice(letters) for i in range(3))
f1_str = (f_d,r_str,f_l)
strsh= list(f1_str)
random.shuffle(strsh)
fake_str = ''.join(strsh)
print('\n****************************')

print('Given   String: ' + str)
print('reverse String: ' + r_str)
print('fake le String: ' + f_l)
print('fake de String: ' + f_d)
print('fake    String: ' + fake_str)
print('\n****************************')

cipher = onetimepad.encrypt(fake_str, 'random')
print("Cipher text is ")
print(cipher)

print('\n****************************')


def generateOTP() : 
	digits = "0123456789"
	OTP = ""  
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
	return OTP 

if __name__ == "__main__" : 
	print("OTP of 4 digits:", generateOTP()) 

print('\n****************************')
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')
print(msg)

