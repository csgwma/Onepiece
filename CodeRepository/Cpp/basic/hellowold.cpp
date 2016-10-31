#include <iostream>
using namespace std;
using std::string;
int main(int argc, char * argv[]) {
    cout << "hello world!" << endl;
    int val = 5;
    int &ref = val;
    ref = 7;
    cout << ref << endl;
    string str2 = "maguowei 2";
    string str = str2;
    cout << str << endl;
    //getchar();
    //getchar();
}
