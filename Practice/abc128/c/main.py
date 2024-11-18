def main():
    N, M = map(int, input().split())
    switches = []
    switchToBulb = {}
    for i in range(M):
        tmpSwitches = list(map(int, input().split()))
        switches.append(tmpSwitches[1:])
        for switch in tmpSwitches[1:]:
            if switch not in switchToBulb.keys():
                switchToBulb[switch] = [i]
            else:
                switchToBulb[switch].append(i)
    p = list(map(int, input().split()))

    count = 0
    for bitnum in range(1 << N):
        switchChecker = [[False for i in range(len(switches[x]))] for x in range(M)]
        bulbsCount = [0 for i in range(M)]
        for shift in range(N):
            if shift + 1 in switchToBulb.keys():
                if 1 & bitnum >> shift == 1:
                    for bulbIndex in switchToBulb[shift + 1]:
                        bulbsCount[bulbIndex] += 1

        turnOnBulbCount = 0
        for i in range(M):
            if bulbsCount[i] % 2 == p[i]:
                turnOnBulbCount += 1
        if turnOnBulbCount == M:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
