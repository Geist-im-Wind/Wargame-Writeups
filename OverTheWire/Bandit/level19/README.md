Level Goal: "To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary."

Setuid binaries allow a user to execute a program under the privileges of another user. In this case, it seems that we will be running a program that gives us bandit20's permissions.

Lo and behold, in the home folder is a file aptly named "bandit20-do". Running it by itself seems to indicate that I can run commands with it as bandit20. Giving it a shot, I used `./bandit20-do ls`. Seeing that it worked, I used `./bandit20-do cat /etc/bandit_pass/bandit20` and received the password for bandit level 20.

Password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
