#include <iostream>
using namespace std;

int range(int len);

int main()
{
    int l;
    
    cout<<"Enter val: "   ;
    cin>>l;
    
    int rng[] = {range(l)};
    
    for (int i : rng)
        cout<<i;
    return 0;
}

int range(int len)
{
    const int N = len;
    int arr[N];
    for (int i=0; i<N; i++)
        arr[i]=i;
    return *arr;
}