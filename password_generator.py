#password generator

import random 

chars = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+?>":'

print('New Generated password: ')

password = ''

for i in range(10): 
    password += random.choice(chars)


print(password)