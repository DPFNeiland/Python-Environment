

# Temos 1 <= N <= 10^5 pedras numeradas de 1 a N e a i-ésima pedra tem um valor associado
# 1 <= hi <= 10~4. Um sapo começa na posição 1 e deve chegar até a posição N com o menor custo
# possível. um sapo na posição i pode ir para as posições j = i + 1, i +2 , ..., i + k, 1 <= K <= 100
# com um custo |hi - hj|, qual é o custo mínimo para o sapo chegar ao seu destino?

# Exemplo: N = 5, K = 3
# h: | 1 3 4 5 2
# resp: 3

N, K = list(map(int, input().split()))
h = list(map(int,input().split()))

print(h)

# Por exemplo: c(4) = min c(i) + |h(i) - h(4)|
#                  1<= i <= 3

# Sendo c(i) o custo da pedra i

from math import inf

def c(i: int) -> int:
    if i == 0: return 0
    
    ret = inf
    
    for j in range(max(0, i - K),i):
        ret = min(ret, c(j) + abs(h[j] - h[i]))
    
    return ret


print(c(len(h) - 1))