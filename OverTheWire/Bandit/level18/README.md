Level Goal: "The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH."

Logging in initially logs you out immediately with a "Byebye !" message. You can entirely bypass this with just using dash instead of bash, though. The full command to log in is `ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/dash`. While this does hide the prompt, commands still execute just fine. Reading the contents of the "readme" file gets you the password.

Password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
