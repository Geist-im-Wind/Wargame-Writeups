NOT YET DONE

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

I made some C code on my end to test my understanding of this

```c
#include <stdio.h>

int main(int argc, char **argv)
{
        printf("%d, \n", argc, !atoi(argv[2]));
        if (argc != 3 || !atoi(argv[2]))
            printf("Failed\n");
            return 1;
        printf("Passed parameters.\n");
        printf("%s \n", abs(atoi(argv[1])) / atoi(argv[2]));
}
```

My inclination was that simply doing `./level02 1 0` would work, as that would satisfy the SIGFPE. I found that this was not the case, however, as this causes a SIGSEGV, or a Segmentation Fault. This is likely from a null value being passed into `atoi`.
