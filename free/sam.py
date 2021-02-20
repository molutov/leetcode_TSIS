n, k = int(input()),  float(input())
print(sum(int(i) * k for i in range(1, n + 1, 2)) + sum(int(i) / k for i in range(2, n + 1, 2)))
