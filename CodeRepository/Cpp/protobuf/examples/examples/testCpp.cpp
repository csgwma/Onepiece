#include <iostream>
#include <fstream>
#include "msg.pb.h"
using namespace std;
 

int main() {
	Person person;
	person.set_name("John Doe");
	person.set_id(1234);
	person.set_email("jdoe@example.com");
	fstream outputstream("myfile");
	person.SerializeToOstream(&outputstream);

	cout << "over" << endl;
}