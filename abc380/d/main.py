def main():
    S = input()
    Q = int(input())
    K = list(map(int, input().split()))
    max_K = max(K)
    Slen = len(S)
    ls = [True]
    lenLs = 1

    while Slen * lenLs < max_K:
        ls = ls + list(map(lambda x: not x, ls))
        lenLs *= 2

    ansLs = []
    for i in range(Q):
        ans = S[K[i] % Slen - 1]
        if not ls[K[i] // Slen]:
            ans = ans.swapcase()
        ansLs.append(ans)

    print(' '.join(ansLs))

    """
    qWeRtYuIoP
    q:1,11,21,
    W:2,22
    10
    20
    40
    80
    
    ind % len(S) == (大文字小文字問わない値)
    """


if __name__ == '__main__':
    main()
