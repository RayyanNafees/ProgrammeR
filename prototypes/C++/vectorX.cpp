#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector <int> vec;
    for (int i=0; i<5; i++){
        vec += [i];
        cout << vec[i];
       }
   
}