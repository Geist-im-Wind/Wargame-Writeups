Level Goal: "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…"

On a whim, I checked if the cron from the last level ran for bandit24, as well. I found that it did, and I am not sure if this is intended. Basically, I ran `echo I am user bandit24 | md5sum | cut -d ' ' -f 1`, which resulted in "ee4ee1703b083edac9f8183e4ae70293". I then went used `cat /tmp/ee4ee1703b083edac9f8183e4ae70293` and received the password. I will try to find a more legitimate way to go about winning this level, though.

Taking a look in /etc/cron.d/, there are 4 files, cronjob_bandit22, cronjob_bandit23, cronjob_bandit24, and popularity-contest. After taking a look at each, the "cronjob" ones seem to run shell scripts in their respective /usr/bin/cronjob-<user>.sh. Looking at the one for bandit24, we get:
```
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        timeout -s 9 60 ./$i
        rm -f ./$i
    fi
done
```

Okay, so it determines the user, goes to /var/spool/<user>, then executes and deletes every script in /var/spool/<user>, one by one. We have to figure out a way to execute a script that gets us our password.

I created an initial script with a simple `cat /etc/bandit_pass/bandit24`, copied it to /var/spool/bandit24, and ran the shell script that would execute and delete it, but permission was denied, due to running it under bandit23 and going to executing in the folder I was running the command from. From here, I had to think of a way to go about writing a script in such a way that cron would execute my script, and how to have it do so in a way that would allow me to read the password.

What I ended up trying was a file with the script `cat /etc/bandit_pass/bandit24 > /tmp/<random string>pass`. I then used `chmod 777` on the file to allow cron to execute it, then copied it to /var/spool/bandit24. This didn't initially work, but I realized I needed to add `#!/bin/sh` to the top of my script, and it worked afterwards.

Password: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
