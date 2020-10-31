#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        int a[n],b[m],c[n]={0};
        for(int i=0;i<n;i++)
            cin>>a[i];
        for(int i=0;i<m;i++)
            cin>>b[i];
        int x=0;
        for(int i=1;i<=m;i++)
        {
            for(int j=i;j<=n;j=j+i)
            {
                //cout<<j<<"  ";
                if(a[j-1]>0)
                {
                    if((a[j-1]-b[i-1])<=0)
                    {
                        c[j-1]=i;
                        a[j-1]=0;
                    }
                }
            }
            //cout<<endl;
        }
        for(int i=0;i<n;i++)
        {
            if(c[i]>0)
                cout<<c[i]<<endl;
            else
                cout<<-1<<endl;
        }
    }
}