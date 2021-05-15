#include <stdio.h>
#include <stdlib.h>
int main(){
   char str[2];

   puts("how long do you think this lasso is: (hint: its really long)");
   fflush(stdout);
   fgets(str, 600, stdin);
   int val = atoi(str);
   printf("You guessed %d\n", val);
   puts("Its gotta be way longer than that");
   fflush(stdout);

   return(0);
}


