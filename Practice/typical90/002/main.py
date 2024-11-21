def main():
    # 0:(, 1:)
    N = int(input())

    ansList = []

    if N % 2 == 0:
        for mask in range(1 << N):
            if not mask.bit_count() == N / 2:
                # print(bin(mask), mask.bit_count())
                continue
            else:
                uncouples = 0
                ans = ""
                # print(bin(mask))
                for digitIndex in range(N):

                    bitNum = 1 & (mask >> digitIndex)
                    # print(bitNum)

                    if bitNum == 0:
                        uncouples += 1
                        ans += "("
                    elif bitNum == 1:
                        uncouples -= 1
                        ans += ")"
                    if uncouples < 0:
                        break

                if uncouples == 0:
                    ansList.append(ans)

        if ansList:
            ansList = sorted(ansList)

            for ans in ansList:
                print(ans)
        # else:
        #     print("")


if __name__ == '__main__':
    main()
