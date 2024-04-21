#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 100

/**
 * Function: count_bits
 * --------------------
 * counts the number of 1's and 0's in the binary representation of an integer.
 *
 * val: the integer to be analyzed.
 *
 * returns: void. The function prints the original number, the count of 0's, and the count of 1's.
 */
void count_bits(int val)
{
    int num = val;
    int numsize = sizeof(val);
    numsize = numsize * 8;
    int countof0 = 0;
    int countof1 = 0;

    while (numsize > 0)
    {

        if (val & 1)
        {
            countof1++;
        }
        else
        {
            countof0++;
        }

        val = val >> 1;
        numsize--;
    }

    printf("Passed number: %d || Qty of zeros: %d || Qty of ones: %d\n", num, countof0, countof1);
}

/**
 * Function: print_fibonnaci
 * -------------------------
 * prints the first n numbers in the Fibonacci sequence.
 *
 * n: the number of Fibonacci numbers to print.
 *
 * returns: void. The function prints the Fibonacci sequence.
 */
void print_fibonnaci(int n)
{
    int a = 1;
    int b = 0;
    int c = 0;

    while (n > 0)
    {
        printf("%d ", c);
        c = a + b;
        a = b;
        b = c;

        n--;
    }

    printf("\n");
}

/**
 * Function: file_symbol_freq
 * --------------------------
 * counts the number of occurrences of a character in a file.
 *
 * filename: the name of the file to be analyzed.
 * symbol: the character to count.
 *
 * returns: the count of the symbol. If the symbol is not found, it returns -1.
 */
int file_symbol_freq(char *filename, char symbol)
{
    int count_symbol = 0;
    char sym;

    FILE *file = fopen(filename, "r");

    while ((sym = fgetc(file)) != EOF)
    {
        if (sym == symbol)
        {
            count_symbol++;
        }
    }

    if (count_symbol == 0)
    {
        return -1;
    }
    else
    {
        return count_symbol;
    }
}

/**
 * Function: file_histogram
 * ------------------------
 * creates a histogram of ASCII characters in a file.
 *
 * filename: the name of the file to be analyzed.
 *
 * returns: void. The function prints each ASCII character and its frequency in the file.
 */
void file_histogram(char *filename)
{
    int ascii[256] = {0};
    FILE *file = fopen(filename, "r");
    char sym;

    while ((sym = fgetc(file)) != EOF)
    {
        ascii[sym]++;
    }

    int n = 0;
    while (n < 256)
    {
        if (ascii[n] != 0)
        {
            printf("%c = %d\n", n, ascii[n]);
        }
        n++;
    }
}

/**
 * Function: reverse_file
 * ----------------------
 * reverses the content of a file.
 *
 * input_file_name: the name of the file to be reversed.
 * output_file_name: the name of the file where the reversed content will be written.
 *
 * returns: void. The function writes the reversed content to the output file.
 */
void reverse_file(char *input_file_name, char *output_file_name)
{
    int size = 1000;
    char *text;
    text = (char *)malloc(size);
    FILE *file_in = fopen(input_file_name, "r");
    FILE *file_out = fopen(output_file_name, "w");
    int n = 0;
    char sym;
    while ((sym = fgetc(file_in)) != EOF)
    {
        if (n == size)
        {
            size += 1000;
            text = (char *)realloc(text, size);
        }
        text[n] = sym;
        n++;
    }

    while (n > 0)
    {
        n--;
        int ascii = text[n];
        int abc = putc(ascii, file_out);
    }

    fclose(file_in);
    fclose(file_out);
}

int main()
{
    // 1
    // printf("count_bits:\n");
    // count_bits(10);
    // count_bits(25);
    // count_bits(79);
    // count_bits(99);

    // 2
    // print_fibonnaci(3);
    // print_fibonnaci(5);
    // print_fibonnaci(7);
    // print_fibonnaci(10);

    // 3
    // char filename[] = "symbol.txt";
    // char symbol = 'c';
    // int count_symbol = file_symbol_freq(filename, symbol);
    // printf("Symbol: %c || Count of symbol: %d\n", symbol, count_symbol);

    // 4
    // char filename[] = "symbol.txt";
    // file_histogram(filename);

    // 5
    char filename[] = "symbol.txt";
    char filenameb[] = "symbolb.txt";
    reverse_file(filename, filenameb);
}
