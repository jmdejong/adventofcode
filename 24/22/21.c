#include<stdio.h>
#include<stdlib.h>
#define mask24 0xFFFFFF

long evolve(int num, int times) {
	while(times--) {
		num = (num ^ (num << 6)) & mask24;
		num = (num ^ (num >> 5)) & mask24;
		num = (num ^ (num << 11)) & mask24;
	}
	return num;
}

int main(int argc, char *argv[]) {

	printf("%d\n", evolve(1, mask24));
	return 0;


	int initials[4096];
	int n_initials = 0;
	if (argc != 2) {
		printf("argument needed");
		return -1;
	}
	printf("%s\n", argv[1]);
	FILE *input = fopen(argv[1], "r");
	size_t _len = 0;
	char *line = NULL;
	while (getline(&line, &_len, input) != -1) {
		initials[n_initials++] = atoi(line);
	}
	free(line);

	long total = 0;
	for (int i=0; i<n_initials; ++i) {
		int num = initials[i];
		int r = evolve(num, 2000);
		// printf("%d: %ld\n", num, r);
		total += r;
	}
	printf("%ld\n", total);
	return 0;
}
