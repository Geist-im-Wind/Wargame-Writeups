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
