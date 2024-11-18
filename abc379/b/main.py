def main():
    N, K = map(int, input().split())
    teeths = list(input())
    safe = 'O'
    danger = 'X'
    count = 0

    checkIndex = 0
    while checkIndex < N:
        checkTeeths = teeths[checkIndex:checkIndex + K]
        if len(checkTeeths) == K:
            if checkTeeths.count(danger) == 0:
                count += 1
                checkIndex = checkIndex + K
            else:
                checkIndex += K - checkTeeths[::-1].index(danger)
        else:
            break
    print(count)


if __name__ == '__main__':
    main()
