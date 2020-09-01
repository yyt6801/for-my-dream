#include <stdio.h>

int main()
{
    // char a = 'k';
    // char zhaomingxing = 'b'; //char 类型    字符型  只能存放一位字符
    // char *c = "zhaomingxingaibaba"; //char* 字符串类型，
    // int b = 1234; //整形  
    // printf("%c \n",a); //char 字符型 用%c输出/表示
    // printf("%d \n",b); //int 整形  用%d输出/表示   %o 八    %x十六进制
    // printf("%s \n",c);//字符串类型，用%s输出

    //char d[6] ="ax5hy"; //字符串的正常表示形式，字符串d包含20个字符
    //char d[3] ={'k','e','y'}; //字符串的正常表示形式，字符串d包含20个字符
    // d[0] = 'a';
    // d[1] = 'x';
    // d[2] = '5';
    // d[3] = 'h';
    // d[4] = 'y';
    // d[5] ='\n';
    //printf("%s\n",d);


    // //数组，是好多个元素的集合
    // int xing[100];
    // xing[0] = 34566543;
    // xing[1] = 23456;

    int x =543;
    int *p = &x;  //  int a  = b;
    printf("%d",*p);
    printf("%d",x);
    &x



}