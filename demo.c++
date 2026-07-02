#include<iostream>
using namespace std;
int main(){
    int age;

    cout<<"enter age: ";
    cin>>age;
    if(age<18){
        cout<<"you are elligible\n";
    }
    else{
        cout<<"not eligible\n";
    }
    cout<<"your age is:  "<<age;
}