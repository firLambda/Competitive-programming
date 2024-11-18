def main():
    # 入力の読み込み
    total_numbers, num_pairs = map(int, input().split())  # total_numbers と num_pairs を1行で取得
    pairs = []

    # 最初の値（pairs[i].first）の入力
    first_values = list(map(int, input().split()))  # スペース区切りで入力をリストに変換
    for first in first_values:
        pairs.append([first, 0])  # 空のペアとして初期化

    # 次の値（pairs[i].second）の入力
    second_values = list(map(int, input().split()))  # スペース区切りで次の値をリストに変換
    for i in range(num_pairs):
        pairs[i][1] = second_values[i]

    # pairs を first の値でソート
    pairs.sort(key=lambda pair: pair[0])

    total_sum = 0
    weighted_sum = 0

    # メインの計算
    for pair in pairs:
        if total_sum < pair[0] - 1:
            print(-1)
            return
        total_sum += pair[1]
        weighted_sum += pair[1] * pair[0]

    # 最後に total_sum が total_numbers と一致するか確認
    if total_sum != total_numbers:
        print(-1)
        return

    # 結果を出力
    print(total_numbers * (total_numbers + 1) // 2 - weighted_sum)


# 実行
if __name__ == "__main__":
    main()
