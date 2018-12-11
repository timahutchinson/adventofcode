import sys

sys.setrecursionlimit(10000)


def treesum(tree):
    def helper(tree, acc):
        nchild = tree.pop(0)
        nmeta = tree.pop(0)
        acc += sum(treesum(tree) for _ in range(nchild))
        acc += sum(tree.pop(0) for _ in range(nmeta))
        return acc
    acc = 0
    return helper(tree, acc)


with open("../../../data/2018/8/data.txt") as f:
    tree = [int(x) for x in f.read().split()]

print(treesum(tree))
