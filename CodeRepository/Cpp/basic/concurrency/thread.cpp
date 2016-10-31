#include <iostream>
#include <thread>

void thread_function()
{
    std::cout << "thread function\n";
}

int main()
{
    std::thread t(&thread; _function);
    std::cout << "main thread\n";
    t.join();
    std::cout << "Over\n";
    return 0;
}