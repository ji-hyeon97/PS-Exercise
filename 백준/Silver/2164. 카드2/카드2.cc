#include <iostream>
#include <queue>
using namespace std;

int main() {
	int n;	cin >> n;
	queue <int> q;

	for (int i = 1; i <= n; i++) {
		q.push(i);
	}

	// 디버깅
	/*while (!q.empty()) {
		cout << q.front() << endl;
		q.pop();
	}*/
	
	while (1) {
		if (q.size() == 1)
			break;
		q.pop();
		q.push(q.front());
		q.pop();
	}

	cout << q.front();

	return 0;
}