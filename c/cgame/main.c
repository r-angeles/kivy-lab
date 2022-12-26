#include <stdio.h>
#define FILENAME "data.txt"
#define MAXLINE 50

void readFile(char line[MAXLINE]);

typedef struct 
{
    char *name;
    int base_damage;
    int hp;
} entity;


int main() 
{
    char c[MAXLINE];
    readFile(c);
    printf("%s \n", c);

    return 0;
}

void readFile(char line[MAXLINE]) {
    FILE *fpointer = fopen(FILENAME, "r");

    fgets(line, MAXLINE, fpointer);

    fclose(fpointer);
}