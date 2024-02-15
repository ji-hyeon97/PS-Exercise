#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

int N, M;
bool visited[8];
vector<int> input;
int selected[8];
set<string>s;

void func(int cnt){
    if(cnt == M){
        string str = "";
        for(int i=0; i<M; i++){
            // cout << selected[i] << " ";
            str += to_string(selected[i]) + " ";
        }
        if(s.find(str) == s.end()){
            cout << str << "\n";
            s.insert(str);
        }
        return;
    }
    
    for(int i=0; i<N; i++){
        if(visited[i])
            continue;
        visited[i] = true;
        selected[cnt] = input[i];
        func(cnt+1);
        visited[i] = false;
    }
}

int main(){
    cin >> N >> M;
   
    for(int i=0; i<N; i++){
       int n;   cin >> n;
       input.push_back(n);
    }
    
    sort(input.begin(), input.end());

    func(0);
    
    return 0;
}
