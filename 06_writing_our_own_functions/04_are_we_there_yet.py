# DMOJ problem - ccc18j3
# https://dmoj.ca/problem/ccc18j3

distances = list(map(int, input().split()))

cumulative = [0]
for d in distances:
    cumulative.append(cumulative[-1] + d)

print(cumulative)

for i in range(5):
    print(" ".join(str(abs(cumulative[i] - cumulative[j])) for j in range(5)))