NOT DONE

With this being a reverse engineering challenge, I busted out r2 immediately. I am fairly new with it, so perhaps I just got lucky, but I essentially went into main, had r2 read it out, then paged through looking for where a string comparison was being made.

Just before the string comparison was the declared string being created in memory for comparison. The "1337 h4x0r" seems to have also artificially added a bunch of passwords, so that anyone using `strings` would be confused.

I started my analysis by going into r2 and looking for the assembly instructions at the main function.

```assembly
;-- main:
/ (fcn) sym.main 46
|   sym.main ();
|           ; var int local_4h_2 @ ebp-0x4
|           ; var int local_4h @ esp+0x4
|           ; DATA XREF from 0x08048327 (entry0)
|           0x0804840b      8d4c2404       lea ecx, dword [local_4h]   ; 4
|           0x0804840f      83e4f0         and esp, 0xfffffff0
|           0x08048412      ff71fc         push dword [ecx - 4]
|           0x08048415      55             push ebp
|           0x08048416      89e5           mov ebp, esp
|           0x08048418      51             push ecx
|           0x08048419      83ec04         sub esp, 4
|           0x0804841c      83ec0c         sub esp, 0xc
|           0x0804841f      68c0840408     push str.Hello_World        ; 0x80484c0 ; "Hello World!"
|           0x08048424      e8b7feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x08048429      83c410         add esp, 0x10
|           0x0804842c      b800000000     mov eax, 0
|           0x08048431      8b4dfc         mov ecx, dword [local_4h_2]
|           0x08048434      c9             leave
|           0x08048435      8d61fc         lea esp, dword [ecx - 4]
\           0x08048438      c3             ret
```
