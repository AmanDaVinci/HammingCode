#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char* getHamming(char* message);
char parity(char* msg, int index);
char* getBinaryMsg(char* msg);
char* asciiToBinary(int input);

int main(int argc, char** argv)
{
    if(argc != 3)
    {
        printf("Usage: ./hamming -send/receive message\n");
        return 0;
    }
      
    char* message = argv[2];
    char* flag = argv[1];
   
    char* receiveFlag = "-receive";
    char* sendFlag = "-send";
    
    if (strcmp(flag, sendFlag) == 0)
    {
        char* hammingCode;
        hammingCode = getHamming(message);
        
        int len = strlen(hammingCode);
        
        int i;
        for(i = 0; i <= len; i++)
            printf("%c", hammingCode[i]);
            
        printf("\n");
        return 0;
    }
    else if(strcmp(flag, receiveFlag) == 0)
    {
        printf("Not implemented\n");
        return 0;
    }
    else
    {
        printf("Usage: ./hamming -send/receive message\n");
        return 0;   
    }
}

char* getHamming(char* message)
{
    char* msgStream = getBinaryMsg(message);

    // Counting parity bits
    int msglen = strlen(msgStream);
    int paritylen = 0;
    for (int i = 1; i <= msglen; i=i*2)
        paritylen++;

    // Declaring the hamming code stream
    int len = msglen + paritylen;
    char* hammingCode = (char*)malloc(sizeof(char)*len+1);

    // Filling up the hamming code
    int i, j = 0;
    for (i = 0; i < len; i++)
    {
        // Filling up parity positions
        if( i==0 || (i!=1 && ((i & (i-1)) == 0)) ) // Bit hack to check if i is power of 2
        {
            printf("%i\n", i );
            hammingCode[i]=parity(msgStream, i);
        }
        // Filling up the data
        else
        {
            hammingCode[i] = msgStream[j];
            j++;
        }
    }
    
    // Terminating the hamming code string
    hammingCode[len] = '\0';
    return hammingCode;
}

char parity(char* msg, int index)
{
    return '*';
}

char* getBinaryMsg(char* msg)
{
    int len = strlen(msg);
    
    // Entire message stream
    char* msgStream = (char*) malloc(len * 8);
    
    // Converting each ascii character to binary
    int i;
    for(i=0; i<len; i++)
    {
        int letter = (int)msg[i];
        char* binCode = asciiToBinary(letter);

        // Feeding each char's binary to the stream
        msgStream = strcat(msgStream, binCode);
    }
    
    return msgStream;
}

char* asciiToBinary(int input)
{    
    int result = 0, i = 1, indx = 7, remainder;
    char* ascii = (char*)malloc(sizeof(char)*8);

    /* convert decimal to binary format */
    while (input > 0)
    {
        remainder = input % 2;
        
        // Making the ascii array of binary chars
        if (remainder == 0)
            ascii[indx] = '0';
        else if( remainder == 1)
            ascii[indx] = '1';
        indx--;
            
        result = result + (i * remainder);
        input = input / 2;
        i = i * 10;
    }
    
    for(;indx >= 0; indx--)
    {
        ascii[indx] = '0';
    }

    return ascii;
}