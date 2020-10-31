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
        int b[(n*(n-1))/2][k],count=1,w=0,c[(n*(n-1))/2];
        for(int i=0;i<=n-k;i++)
        {
            for(int j=i+1;j<=n-k+1;j++)
            {
                int x=j,y=k-1;
                b[w][0]=a[i];
                int e=1;
                while(y--)
                    b[w][e++]=a[x++];
                w++;
            }
        }
        int s=(n*(n-1))/2;
        for(int i=0;i<(n*(n-1))/2;i++)
        {
            long long sum=0;
            for(int j=0;j<k;j++)
            {
                sum+=b[i][j];
                cout<<b[i][j]<<" ";
            }
            cout<<endl;
            c[i]=sum;
        }
        /*sort(c,c+s);
        for(int i=0;i<s;i++)
        {
            if(c[i]==c[0])
                count++;
            else
                break;
            cout<<c[i]<<" ";
        }*/
        //cout<<count<<endl;
    }
    return 0;
}