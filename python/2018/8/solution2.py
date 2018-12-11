import sys

sys.setrecursionlimit(10000)


def nodeval(tree):
    nchild = tree.pop(0)
    nmeta = tree.pop(0)
    nodevals = [nodeval(tree) for _ in range(nchild)]
    metas = [tree.pop(0) for _ in range(nmeta)]
    return sum(metas) if nchild == 0 else sum(nodevals[i-1] for i in metas
                                              if i-1 in range(nchild))


with open("../../../data/2018/8/data.txt") as f:
    tree = [int(x) for x in f.read().split()]

print(nodeval(tree))
