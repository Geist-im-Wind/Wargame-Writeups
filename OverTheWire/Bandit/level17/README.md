Level Goal: "There are 2 files in the home directory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new"

This one is simple after just reading the man page for `diff`. Running `diff passwords.new passwords.old` and selecting the first output, which is the line that is different in passwords.new gives the password.

Password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
