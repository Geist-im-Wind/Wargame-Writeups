Before even running the level02 executable, I took a look at the source code they supply for it.

```c
//a little fun brought to you by bla

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void catcher(int a)
{
        setresuid(geteuid(),geteuid(),geteuid());
	printf("WIN!\n");
        system("/bin/sh");
        exit(0);
}

int main(int argc, char **argv)
{
	puts("source code is available in level02.c\n");

        if (argc != 3 || !atoi(argv[2]))
                return 1;
        signal(SIGFPE, catcher);
        abs(atoi(argv[1])) / atoi(argv[2]);
}
```

This code seems to give us the euid we want only if the arguments are exactly 3 (so ./level02 x y), the second argument is a number (it will SEGFAULT otherwise), and we cause a Signal Floating Point Exception (SIGFPE) that causes an overflow.

Our only chance to do this seems to be in `abs(atoi(argv[1])) / atoi(argv[2])`.

A division by zero will simply get us to return 1, ending the function immediately. This means we need to find a way to cause a SIGFPE without the second argument being zero.

What I ended up finding in my research was [this StackOverflow](https://stackoverflow.com/questions/46378104/why-does-integer-division-by-1-negative-one-result-in-fpe/46378352).

All we need to do to cause the SIGFPE is take the absolute minimum value of the int datatype minus 1 and make sure it is divided by -1. The command I used was `./level02 -2147483648 -1`.

Password: OlhCmdZKbuzqngfz
