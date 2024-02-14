#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 값, 인덱스, 카운트
vector<pair<int, pair<int, int>>> v;

bool comp1(pair<int, pair<int, int>> o1, pair<int, pair<int, int>> o2){
    return o1.first < o2.first;
}

bool comp2(pair<int, pair<int, int>> o1, pair<int, pair<int, int>> o2){
    return o1.second.first < o2.second.first;
}

int main(){
    int N;  cin >> N;
    
    for(int i=0; i<N; i++){
        int n;  cin >> n;
        v.push_back({n, {i,0}});
    }
    
    sort(v.begin(), v.end(), comp1);
  
    int prev = v[0].first;    
    int cnt = 0;
    
    for(int i=0; i<N; i++){
        if(prev ==  v[i].first){
            v[i].second.second = cnt;
            prev = v[i].first;
        } 
        else if(prev < v[i].first){
            v[i].second.second = ++cnt;
            prev = v[i].first;
        }
    }
    
    sort(v.begin(), v.end(), comp2);
    
    for(int i=0; i<N; i++){
        cout << v[i].second.second << " ";
    }

    return 0;
}




