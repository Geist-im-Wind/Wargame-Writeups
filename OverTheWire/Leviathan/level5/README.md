There is a single executable named "leviathan5", which, when an ltrace is run on it, tells us that it is trying to open "/tmp/file.log" and convert the output to binary.

If we look at the owner of the file, leviathan6 owns it. This means we can set up a symbolic link in tmp named file.log that directs to /etc/leviathan_pass/leviathan6.

The command to do this is `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log`. Opening the executable now gives us the password.

Password: UgaoFee4li
