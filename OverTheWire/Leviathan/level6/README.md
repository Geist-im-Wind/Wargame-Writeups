This level features an executable much like the last, named 'leviathan6' owned by the user 'leviathan7'. Running it tells us that it requires us input a 4 digit code along with it.

Running an `ltrace` with a random 4 digit code gives us the following:

```console
leviathan6@leviathan:~$ ltrace ./leviathan6 9999
__libc_start_main(0x565556c0, 2, 0xffffd6e4, 0x56555780 <unfinished ...>
atoi(0xffffd822, 0xffffd6e4, 0xf7ffcd00, 0x565556d8) = 9999
puts("Wrong"Wrong
)                                        = 6
+++ exited (status 0) +++
```

The 'atoi' in particular is what we are looking to break. I'm sure there are other ways to do it, but I decided it would be fun to beat this by bruteforce.

I used this simple script:

```bash
#!/bin/bash
for i in {0001..9999}; do
        ~/leviathan6 $i
done
```

Leviathan done. 

Password: ahy7MaeBo9
