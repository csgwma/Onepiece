#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::string;

// 定义一个指向函数的指针
typedef int (*op) (const int , const int );


int add (const int a, const int b) {
    return a + b;
}

int sub (const int a, const int b) {
    return a - b;
}

// 函数指针做形参的函数
int numOp (const int a, const int b, op fp) {
    return fp (a, b);
}


int main(int argc, char * argv[]) {
    cout << add(2, 3) << endl;
    op fp = add; // 或者 op fp = &add

    // 下面两种调用方式一样
    cout << fp(2, 3) << " : " << (*fp)(2, 3) << endl;

    // 函数指针形参
    cout << numOp (2, 3, sub) << endl;
}
