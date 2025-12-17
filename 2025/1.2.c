#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <complex.h>

#define NUM_DIALS 100
enum direction {LEFT = -1, RIGHT = 1};

int main(int argc, char* argv[]){
  FILE *fptr;
  fptr = fopen("2025/1.txt", "r");

  int count = 0;
  int current = 50;
  char instruction[10];
  while(fgets(instruction, sizeof instruction, fptr) != NULL) {
    char magnitude[10]; strncpy(magnitude, &instruction[1], 9);

    enum direction dir = instruction[0] == 'L' ? LEFT : RIGHT;
    int mag = atoi(magnitude);

    // num_full_rotations * NUM_DIALS + remainder = mag
    int num_full_rotations = mag / NUM_DIALS;
    int remainder = mag % NUM_DIALS;

    int next = (current + (mag * dir)) % NUM_DIALS;
    next = (next + NUM_DIALS) % NUM_DIALS; // removing negatives

    // counting
    count += num_full_rotations;
    if(current != 0) {
      if(current + (remainder * dir) >= NUM_DIALS) count++;
      if(current + (remainder * dir) <= 0) count++;
    }

    printf("%d + (%d * %d + %d) = %d \t (count = %d)\n", 
           current, num_full_rotations, NUM_DIALS, remainder*dir, next, count);

    current = next;
  }
  printf("FINAL COUNT: %d", count);
  return 0;
}
