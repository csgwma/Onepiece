#include <iostream>
#include <cstdio> //包含语言重定向函数freopen的库
using namespace std;
int main()
{
 //正式提交代码时，删除下面两项就行了
	// freopen("input.txt","r",stdin); //重定向输入流
	// freopen("output.txt","w",stdout); //重定向输出流
 /* input.txt 文件内容如下：
 2
 1 1
 2 2 
 */
 cout<<"begin.."<<endl;
 int n;
 int a,b;
 cin>>n;
 for(int i=0; i<n; ++i){
 	cin>>a>>b;
 	cout<<a+b<<endl;
 }
 /* output输出文件
 2
 4
 */
 return 0;
}
