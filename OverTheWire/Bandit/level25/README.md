Level Goal: "Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it."

Looking at the helpful commands list, I have a pretty good idea about what the challenge will be here.

Initially I tried logging in to bandit26 using the provided key (`ssh -i bandit26.sshkey bandit26@localhost`), but I was immediately disconnected with an ASCII art of "bandit26" at the bottom.

This led me to do some searching on how to identify the shell being used by a given user. At first, I tried using `finger`, but I found it was not installed. Looking for an alternative approach, I found `getent passwd | awk -F: -v user="bandit26" '$1 == user {print $NF}'`. I will be honest and say I had no idea how this worked when I found it, so I decided to read the manuals to get an idea of which each command here was doing.

`getent passwd` takes the database of entries in passwd and lists it. Passwd itself is basically a database of information about users that can log into the system.

`awk -F: -v user="bandit26" '$1 == user {print $NF}'` uses `fs` for the input field separator (`-F`). This separates the input record into fields. It then creates a variable named 'user' containing the word "bandit26" (`-v user="bandit26"`) and defines the first positional argument as this variable before printing it's results `'$1 == user {print $NF}'`. It struck me in reading this that this command is a bit strange, as doing just `getent passwd | awk -F: '$1 == "bandit26" {print $NF}'` works all the same.

Anyway, this returns /usr/bin/showtext as the shell. In reading it, it contains the following:

```bash
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

Now that we know what is being run immediately, we can try to figure out a way to break out of it. In running `ls -l /usr/bin/showtext`, we can see that the owner is root, so we are unable to edit it directly.

My first attempt was to try running this:

```bash
ssh -i bandit26.sshkey bandit26@localhost /bin/bash -s << EOF
<random commands here>
EOF
```

This only ended up echoing the commands before the ASCII art and exit and no more.

So, I went back to puzzling over the initial "shell" we have to deal with. The only real thing we could manipulate is more. The only way we could seemingly execute any shell commands would be to somehow execute those commands before `more` terminates. That's when I realized the somewhat silly solution.

You just make your terminal tiny. Log into bandit26 like that, and `more` will not quit until you make the terminal large enough to see the whole ASCII art. From there, `more` allows one to press v to open vi inside it. You can read the password by running an edit on it with `:e /etc/bandit_pass/bandit26`.

Password: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
