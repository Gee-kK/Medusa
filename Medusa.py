import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

counter = 0


colorama.init()

session = requests.session()

print(Fore.GREEN + """      ___           ___          _____          ___           ___           ___     
     /__/\         /  /\        /  /::\        /__/\         /  /\         /  /\    
    |  |::\       /  /:/_      /  /:/\:\       \  \:\       /  /:/_       /  /::\   
    |  |:|:\     /  /:/ /\    /  /:/  \:\       \  \:\     /  /:/ /\     /  /:/\:\  
  __|__|:|\:\   /  /:/ /:/_  /__/:/ \__\:|  ___  \  \:\   /  /:/ /::\   /  /:/~/::\ 
 /__/::::| \:\ /__/:/ /:/ /\ \  \:\ /  /:/ /__/\  \__\:\ /__/:/ /:/\:\ /__/:/ /:/\:\    """)
print(""" \  \:\~~\__\/ \  \:\/:/ /:/  \  \:\  /:/  \  \:\ /  /:/ \  \:\/:/~/:/ \  \:\/:/__\/
  \  \:\        \  \::/ /:/    \  \:\/:/    \  \:\  /:/   \  \::/ /:/   \  \::/     
   \  \:\        \  \:\/:/      \  \::/      \  \:\/:/     \__\/ /:/     \  \:\     
    \  \:\        \  \::/        \__\/        \  \::/        /__/:/       \  \:\    
     \__\/         \__\/                       \__\/         \__\/         \__\/""")

print("")
print("")
print("Original project by Youtube: BioRat")
print("Original project link:")
print("https://github.com/Sadyyn/ReBomb2")

print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting the poor sod.....')
print('')
print('')

while True:
    req = session.post(x)
    
    counter = counter + 1
    print(req.text)
    print('reported ' + counter + 'times')

    if req.status_code == 0:
        print("reported a total of " + counter + "times")
        break

    time.sleep(10)


input()