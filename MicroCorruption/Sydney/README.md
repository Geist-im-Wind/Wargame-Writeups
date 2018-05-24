Now we have a challenge worth slightly more points in Sydney.

Our manual this time lets us know that they are no longer writing the password into memory. It looks like we can't just read the password off memory anymore. That said, there is some promise to the mention of setting the password onto the device like it was just received.

Unfortunately, after a bit of looking around, that function does not seem to be defined in our disassembler. This means that we will need to find some way to bypass the password check function more than likely. At the very least, it seems a good place to first set a breakpoint, so I set a breakpoint on check_password.

```assembly
448a <check_password>
448a:  bf90 7324 0000 cmp	#0x2473, 0x0(r15)
4490:  0d20           jnz	$+0x1c
4492:  bf90 6a76 0200 cmp	#0x766a, 0x2(r15)
4498:  0920           jnz	$+0x14
449a:  bf90 516a 0400 cmp	#0x6a51, 0x4(r15)
44a0:  0520           jne	#0x44ac <check_password+0x22>
44a2:  1e43           mov	#0x1, r14
44a4:  bf90 3d73 0600 cmp	#0x733d, 0x6(r15)
44aa:  0124           jeq	#0x44ae <check_password+0x24>
44ac:  0e43           clr	r14
44ae:  0f4e           mov	r14, r15
44b0:  3041           ret
```

From the check_password function, it seems they are looking for "2473 766a 6a51 733d", just from the values being compared against in memory from r15. Basically, the function will compare a given hex value with an offset from r15. You can easily see the values you entered via `read r15`

```
> read r15
   439c:   7465 7374 7900 0000  testy...
   43a4:   0000 0000 0000 0000  ........
   43ac:   0000 0000 0000 0000  ........
   43b4:   0000 0000 0000 0000  ........
```

So, in the case of the first comparison, it will be comparing between 2473 and what is at 0x0 of r15, which is 7465. If the comparison turns out to be a match, we skip to the next comparison. If not, we jump to the end of the function and will get a message saying that we entered the wrong password. So, despite them not writing the password into memory, it is easily available in the disassembler. Well, sort of. You will see that entering "2473 766a 6a51 733d" actually doesn't work. It will fail the comparison and you will be back at square one.

As it turns out, the CPU stores information in little endian in memory. This means that we will need to convert the hex value from little endian to big endian.

```
[24 73] [76 6a] [6a 51] [73 3d]

turns into

[73 24] [6a 76] [51 6a] [3d 73]
```

Entering `73 24 6a 76 51 6a 3d 73` into the lock will get us in.
