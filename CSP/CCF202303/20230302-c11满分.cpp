#include<bits/stdc++.h>
#include<iostream>
using namespace std;

int n, k;
long long int m;
map<int, int>tim, res, flag;

int main(){
    cin >> n >> m >> k;

    int max = 0;
    for(int i = 0; i < n; ++i){
        cin >> tim[i] >> res[i];
        max = max > tim[i] ? max : tim[i];
        flag[tim[i]] += res[i];
        // flag[i]为用时i天的区域缩短一天所用时
    }
    for(int i = max; i > 0; i--){
        //cout << i << " " << flag[i] << endl;
        if(max == k)break;
        if(m > flag[i]){
            m = m - flag[i];
            flag[i - 1] += flag[i];
            max--;
        }else break;
    }
    cout << max;
    return 0;
}