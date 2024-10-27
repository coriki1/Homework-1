#include <stdio.h>
#include "utils.h"
#include "utils.c"

int main(void) {

    FILE *pokerArt = fopen("pokerArt.txt", "r");

    printart(pokerArt);
    

    return 0;
}