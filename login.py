import time
user_name = []
password = []
user_input = input('Enter username: ')
user_name.append(user_input)
print(f'Your name is: {user_input}')
user_pass = input('Enter password: ')
password.append(user_pass)
print(f'Your pass is: {user_pass}')
time.sleep(2)
print ('Password encrypted...')
print('Please LOGIN...')
while True:
    loginname = input('User name: ')
    if loginname in user_name:
        loginpass = input('Enter password: ')
        if loginpass in password:
            time.sleep(1)
            print ('Scanning password...')
            time.sleep(3)
            print ('Log in successful')
    break
else:
    time.sleep(1)
    print ('Scanning password...')
    time.sleep(3)
    print ('Wrong password')
