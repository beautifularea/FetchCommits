#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

int 
main(int argc, char const *argv[])
{
    int pid;
	int newfd;

	if (argc != 2) {
		fprintf(stderr, "usage: %s output_file\n", argv[0]);
		exit(1);
	}
	if ((newfd = open(argv[1], O_CREAT|O_TRUNC|O_WRONLY, 0644)) < 0) {
		perror(argv[1]);	/* open failed */
		exit(1);
	}
	printf("This goes to the standard output.\n");
	printf("Now the standard output will go to \"%s\".\n", argv[1]);
	fflush(stdout);

	dup2(newfd, 1); 

	printf("This goes to the standard output too.\n");
	exit(0);
}
