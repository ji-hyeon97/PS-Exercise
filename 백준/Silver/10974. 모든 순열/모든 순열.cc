#include <iostream>
using namespace std;

bool visited[9];
int nums[8];
int N;

void permutation(int cnt){
    if(cnt == N){
        for(int i=0; i<N; i++){
            cout << nums[i] << " ";
        }
        cout << "\n";
        return;
    }
    
    for(int i=1; i<=N; i++){
        if(visited[i])
            continue;
        visited[i] = true;
        nums[cnt] = i;
        permutation(cnt+1);
        visited[i] = false;
    }
}


int main(){
    
    cin >> N;
    
    permutation(0);
    
    return 0;
}
