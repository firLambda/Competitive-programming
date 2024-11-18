def main():
    S = input()
    SList = S.split('|')
    resultList = []
    for stmp in SList:
        resultList.append(str(len(stmp)))

    print(' '.join(resultList[1:-1]))


if __name__ == '__main__':
    main()
