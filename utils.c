#include <stdio.h>
#include "utils.h"

void printart(FILE *art) {

printf("\n");

    while (!feof(art)) {
        char c = fgetc(art);
        printf("%c", c);
    }
    
printf("\n");

}