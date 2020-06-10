import random as rn
import matplotlib.pyplot as plt
import seaborn as sns


def hypergeometric(N,K,n):
    x = 0
    c = N - K
    k = K
    for i in range(n-1):
        r = rn.random()
        if r <= k/N:
            x += 1
            k -= 1
        else:
            c -= 1
        N -= 1
    return x

if __name__ == "__main__":
    data = []
    for i in range(10000):
        data.append(hypergeometric(500, 50, 100))

    sns.distplot(data, kde=False, color="b")
    plt.show()