#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NUM_DIALS 100
enum direction {LEFT = -1, RIGHT = 1};

int main(int argc, char* argv[]) {
  FILE *fptr;
  fptr = fopen("2025/1.txt", "r");

  int count = 0;
  int current = 50; // no need to be unsigned: same number of 0's in the end.
  char instruction[10];
  while(fgets(instruction, sizeof instruction, fptr) != NULL) {
    char magnitude[10]; strcpy(magnitude, &instruction[1]);

    enum direction dir = instruction[0]=='L' ? LEFT : RIGHT;
    int mag = atoi(magnitude);

    current = (current + mag * dir) % NUM_DIALS;
    if(current == 0) count++;
  }
  printf("%d", count);
  return 0;
}
