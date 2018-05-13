Level Goal: "The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on"

Since we already have the private key, we can just use the `-i` flag of the `ssh` command to allow us to identify ourselves as "bandit14" to ssh in. Rather than going for the full hostname, since it is on the same computer, we log in to localhost. The full command is `ssh -i sshkey.private bandit14@localhost`. Once in, simply `cat /etc/bandit_pass/bandit14`.

Password: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
