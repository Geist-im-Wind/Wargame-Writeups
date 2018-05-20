NOT YET DONE

Here we step through the closet door into the land of exploitation.

Upon immediate entry, there is nothing out of the ordinary. Heading to /narnia/, I find a litany of files for each level, including some C source code.

Let's start by looking at the source code for level0.

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
	long val=0x41414141;
	char buf[20];

	printf("Correct val's value from 0x41414141 -> 0xdeadbeef!\n");
	printf("Here is your chance: ");
	scanf("%24s",&buf);

	printf("buf: %s\n",buf);
	printf("val: 0x%08x\n",val);

	if(val==0xdeadbeef){
        setreuid(geteuid(),geteuid());
		system("/bin/sh");
    }
	else {
		printf("WAY OFF!!!!\n");
		exit(1);
	}

	return 0;
}
```

After looking up the phrase 'deadbeef' itself, I found that '00xdeadbeef' commonly refers to a software crash or deadlock. I imagine this means we can probably cause a buffer overflow with scanf.
