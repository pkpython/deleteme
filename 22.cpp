#include <bits/stdc++.h>  
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);
        int count=1,sum=0;
        for(int i=k;i<n;i++)
        {
            if(a[k-1]==a[i])
                count++;
            else
                break;
        }
        int x=k+count-1;
        long long int z=1;
        for(int i=x;i>k;i--)
            z*=i;
        int y=1;
        for(int i=count-1;i>1;i--)
            y*=i;
        cout<<z/(y)<<endl;
    }
    return 0;
}