Level Goal: "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints."

Taking a look in /etc/cron.d/, there are 4 files, cronjob_bandit22, cronjob_bandit23, cronjob_bandit24, and popularity-contest. After taking a look at each, the "cronjob" ones seem to run shell scripts in their respective /usr/bin/cronjob-<user>.sh. Looking at the one for bandit23, we get:
```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Let's take this apart piece by piece.

`myname=$(whoami)` assigns the result of the `whoami` command, which echo's the user you currently are, to the variable myname.

`mytarget=$(echo I am user $myname | mdsum | cut -d ' ' -f 1)` sets the variable mytarget to be equal to the result of the command `echo I am user $myname | mdsum | cut -d ' ' -f 1`, which just uses the phrase "I am user <user>" to make a random sequence of numbers and letters unique to each user.

The next two lines tell the user of the script that the password file is being copied to a set location and saves a file containing the password of the current user to that location.

Assuming this cron is being run for bandit23, we can acquire the password we are looking for by running this line: `echo I am user $myname | mdsum | cut -d ' ' -f 1` with $myname = bandit23. This gives us "8ca319486bfbbc3663ea0fbe81326349", and, if we run `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`, we get the password.

Password: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
