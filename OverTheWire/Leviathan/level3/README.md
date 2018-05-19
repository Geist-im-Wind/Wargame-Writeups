In the initial folder is an executable named "level3", which, when run, simply asks for a password. Running an `ltrace` on it tells me that it is looking for the password "snlprintf". Inputting that in gives me "[You've got shell]!" and a simple shell.

If I run `id` in shell, I can clearly see that I am now leviathan4, and as such can simply read the password in leviathan_pass.

Password: vuH0coox6m
