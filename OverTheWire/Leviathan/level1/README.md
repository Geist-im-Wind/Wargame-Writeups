Upon login, there is an exectuable named "check" in the home folder with Leviathan2 as the owner. I imagine this is what we're looking for.

Opening it prompts a password that I obviously do not know. However, I can use `gdb` to determine what functions are being run in this program. With that being the case, I do think they very much under-exaggerated the foreknowledge needed to solve Leviathan, but oh well. After hopping into `gdb check`, I ran `info functions` and it returned:
```
All defined functions:

Non-debugging symbols:
0x00000488  _init
0x000004c0  strcmp@plt
0x000004d0  printf@plt
0x000004e0  getchar@plt
0x000004f0  geteuid@plt
0x00000500  puts@plt
0x00000510  system@plt
0x00000520  setreuid@plt
0x00000530  __libc_start_main@plt
0x00000550  _start
0x00000590  __x86.get_pc_thunk.bx
0x000005a0  deregister_tm_clones
0x000005e0  register_tm_clones
0x00000630  __do_global_dtors_aux
0x00000680  frame_dummy
0x000006bc  __x86.get_pc_thunk.dx
0x000006c0  main
0x000007a0  __libc_csu_init
0x00000800  __libc_csu_fini
0x00000804  _fini
```

None of these are really of interest except for strcmp. With that there, I know that it is likely being used to compare two strings for the program, what the user inputs versus the password required.

From here, I run `ltrace ./check` and hit enter until the program exited, which returned:

```
__libc_start_main(0x565556c0, 1, 0xffffd6f4, 0x565557a0 <unfinished ...>
printf("password: ")                                 = 10
getchar(0xf7fc5000, 0xffffd6f4, 0x65766f6c, 0x646f6700password:
) = 10
getchar(0xf7fc5000, 0xffffd6f4, 0x65766f6c, 0x646f6700
) = 10
getchar(0xf7fc5000, 0xffffd6f4, 0x65766f6c, 0x646f6700
) = 10
strcmp("\n\n\n", "sex")                              = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                 = 29
+++ exited (status 0) +++
```

Looks like it has defined right there that it compares the user-inputted string against "sex". Entering sex gives you a shell as leviathan2, which you can then use to read the password to the next level.

Password: ougahZi8Ta
