import numpy as np


def main():
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    trees = np.array([])
    for query in queries:
        if query[0] == 1:
            trees = np.append(trees, 0)
        elif query[0] == 2:
            trees += query[1]
        elif query[0] == 3:
            mask = trees >= query[1]
            print(np.sum(mask))
            trees = np.delete(trees, mask)


if __name__ == '__main__':
    main()
