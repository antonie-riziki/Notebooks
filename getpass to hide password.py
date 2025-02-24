from getpass import win_getpass
from getpass import *

username = input("Username : ")
password = getpass("Password : ")
win_getpass(prompt='Passcode: ', stream= None)
print("Logging in...")

#print(help(getpass))
