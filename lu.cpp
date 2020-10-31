#include <bits/stdc++.h>
    using namespace std;
    int age[3];
    int cost[3];
    int main()
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        int t ;
        cin >> t;
        while(t--)
        {
            int f = 1;
            for(int i = 0; i < 3 ;++i) cin >> age[i];
            for(int i = 0; i < 3 ;++i) cin >> cost[i];
            
            for(int i = 0; i < 3 ;++i)
            {
                for(int j = 0; j < 3 ;++j)
                {
                    if(i!=j)
                    {
                        if(age[i] < age[j] && cost[i] >= cost[j])
                            {f = 0; break;}
                        else if(age[i] == age[j] && cost[i] != cost[j])
                            {f = 0; break;}
                        if(cost[i] <= cost[j])
                        {f = 0; break;}
                    }
                }
            }
            if(f==0) 
                cout << "FAIR\n";
            else
                cout << "NOT FAIR\n";
        }
    }
