#include <iostream>
using namespace std;


int Find(int n) {
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;
	else if (n == 3)
		return 4;
	else {
		return Find(n - 1) + Find(n - 2) + Find(n-3);
	}
}


int main() {
	int t;	cin >> t;

	while (t--) {
		int n;	cin >> n;
		cout << Find(n) << "\n";
	}

	return 0;
}