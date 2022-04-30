
# include <string.h>
# include <stdio.h>

//https://leetcode.com/problems/length-of-last-word/
// Runtime: 0 ms, faster than 100.00% of C online submissions for Length of Last Word.
//Memory Usage : 5.7 MB, less than 74.46 % of C online submissions for Length of Last Word.

int lengthOfLastWord(char* s) {

    int size = strlen(s);

    int last_position_index = 0;

    for (int i = 0; i < size; ++i) {
        // printf("s: %d, %d", sizeof s[i], sizeof  );


        if ((char)s[i] == ' ') {
            //printf("inhere");
            last_position_index = i + 1;
        }
    }


    printf("\n: %d: %c :%d", last_position_index, s[last_position_index], size-last_position_index);

    if (s[last_position_index] == '\0') {
        printf("\nthis is the end eh!");
        int j = last_position_index -1;

        while (s[j] == ' ') {
            j--;
            printf("\n > %d", j);
        }

        printf("loop broken at %c", s[j]);

        int counter = 0;

        for (; j >= 0; --j) {
            if (s[j] == ' ') {
                break;
            }
            else {
                counter++;
            }
        }

        return counter;
        
    }
    else {
        int counter = 0;


        for (int i = last_position_index; i < size; ++i) {

            if (s[i] == ' ') {
                break;
            }
            counter++;
            //printf("%d", counter);

        }

        return counter;
    }



   
}

int main() {
    char words[100] = "   fly me   to   the moon  ";

    for (int i = 0; i < strlen(words); ++i) {
        printf("\n%d : %c", i, words[i]);
    }
    printf("\nLength of last word: %d", lengthOfLastWord(words));

}
