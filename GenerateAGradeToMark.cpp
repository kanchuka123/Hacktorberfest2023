#include <iostream>
using namespace std;

int main(){
    int marks;
    cout<<"Enter Your Marks: ";
    cin>>marks;
    if (marks >= 75 && marks <= 100){
        cout<<"Your Grade is A";
    }
    else if (marks >= 65){
        cout<<"Your Grade is B";
    }
    else if (marks >= 55){
        cout<<"Your Grade is C";
    }
    else if (marks >= 35){
        cout<<"Your Grade is E";
    }
    else if (marks <= 35 && marks >= 0){
        cout<<"Your Grade is F";
    }
    else{
        cout<<"Enter Valid Marks";
    }
    return 0;
}
