#include <bits/stdc++.h>  
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string j,s;
        cin>>j>>s;
        int count=0;
        int l=j.length();
        int a[52]={0};
        for(int i=0;i<l;i++)
        {
            char y=j[i];
            int x=int(y);
            if(x>=65 && x<=90)
                x=x-65;
            else if(x>=97 && x<=122)
                x-=71;
            a[x]=1;
        }
        for(int i=0;i<s.length();i++)
        {
            char y=s[i];
            int x=int(y);
            if(x>=65 && x<=90)
                x=x-65;
            else if(x>=97 && x<=122)
                x-=71;
            count+=a[x];
            
        }
        cout<<count<<endl;
    }
    return 0;
}