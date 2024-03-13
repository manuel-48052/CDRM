#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 100

void count_bits(int val)
{
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

    printf("Qty of zeros: %d\nQty of ones: %d\n", countof0, countof1);
}

void print_fibonnaci(int n)
{
    int a = 0;
    int b = 1;
    int c;

    printf("1 ");
    while (n > 0)
    {
        c = a + b;
        a = b;
        b = c;

        printf("%d ", c);
        n--;
    }

    printf("\n");
}

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
        // printf("%c\n", abc);
    }

    fclose(file_in);
    fclose(file_out);
}

int main()
{
    // 1
    // count_bits(8);

    // 2
    // print_fibonnaci(10);

    // 3
    // char filename[] = "symbol.txt";
    // int count_symbol = file_symbol_freq(filename, 'a');
    // printf("%d\n", count_symbol);

    // 4
    // char filename[] = "symbol.txt";
    // file_histogram(filename);
    // char filename[] = "symbol.txt";
    // char filenameb[] = "symbolb.txt";
    // reverse_file(filename,filenameb);
}
