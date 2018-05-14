Level Goal: "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed."

Taking a look in /etc/cron.d/, there are 4 files, cronjob_bandit22, cronjob_bandit23, cronjob_bandit24, and popularity-contest. After taking a look at each, the "cronjob" ones seem to run shell scripts in their respective /usr/bin/cronjob-<user>.sh. Looking at the one for bandit22, we get:
```
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

This is exactly what we're looking for. It allows us to have access to a file in the /tmp/ folder and writes the password for the next level to it. The password is in the file mentioned above.

Password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
