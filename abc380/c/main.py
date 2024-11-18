def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N, K = int(data[0]), int(data[1])
    S = data[2]

    # 区間の始まりと長さを記録
    segments = []
    one_indices = []
    start = 0

    for i in range(1, N + 1):
        if i == N or S[i] != S[start]:  # セグメント終了条件
            segments.append((S[start], i - start))
            if S[start] == '1':
                one_indices.append(len(segments) - 1)
            start = i

    # K番目の "1" を含むセグメントの入れ替え
    swap_index = one_indices[K - 1]
    if swap_index > 0:
        segments[swap_index - 1], segments[swap_index] = segments[swap_index], segments[swap_index - 1]

    # 出力の生成
    result = []
    for char, length in segments:
        result.append(char * length)

    sys.stdout.write(''.join(result))


if __name__ == '__main__':
    main()
