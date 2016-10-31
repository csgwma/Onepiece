#include <iostream>
#include "person.pb.h"
using namespace std;
int main() {
	std::cout << "begin ... " << std::endl;
	x::Person p;
	p.set_name("tom");
	p.set_id(88);
	p.set_email("xx@xx.com");
	printf("name=%s, id=%d, email=%s \n", p.name().c_str(), p.id(), p.email().c_str()); 
	std::string str;
	p.SerializeToString(&str); 

	printf("---\n %s \n-----\n", str.c_str());
	x::Person a;
	a.ParseFromString(str);
	std::cout << "parse from embeding string.." << std::endl;
	printf("name=%s, id=%d, email=%s \n", a.name().c_str(), a.id(), a.email().c_str()); 

	std::cout << "over ... " << std::endl;
	return 0;
} 