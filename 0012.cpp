#include <bits/stdc++.h>

using namespace std;

int calculate_divisors(long n) {
  int d = 1;
  for (long i = 1L; i <= n / 2; i++) {
    if (n % i == 0) {
      d++;
    }
  }
  return d;
}

int main() {
  long n = 0L;
  for (long i = 1;; i++) {
    n += i;
    if (calculate_divisors(n) >= 500) {
      break;
    }
  }
  cout << n << endl;
}