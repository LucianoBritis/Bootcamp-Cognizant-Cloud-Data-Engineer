import sys

N = int(input())
pessoas = sys.stdin.readline().split()

menor_pos = 0

for i in range(N):
    if i == 0:
      menor = pessoas[i]
      continue
    if pessoas[i] < menor:
      menor = pessoas[i]
      menor_pos = i

print(menor_pos + 1)