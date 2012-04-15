#!/usr/bin/env python3

import sys

"""Solution to recycled numbers gcj2012 problem."""

__author__      = "Mark Whitney"
__copyright__   = "Copyright 2012, Mark Whitney"


def generate_recycled(n):
    n_str = str(n)
    return [int(n_str[i:] + n_str[:i]) for i in range(1, len(n_str))]

def count_all(minr, maxr):
    count = 0
    for n in range(minr, maxr + 1):
        candidates = generate_recycled(n)
        if len(candidates) >= 1:
            count += len([k for k in candidates if k >= minr and k <= maxr and k > n])
    return count

if __name__ == "__main__":
    with open(sys.argv[1]) as inf, open(sys.argv[2], "w") as outf:
        count = int(inf.readline().strip())
        for i in range(1, count + 1):
            minr, maxr = map(int, inf.readline().strip().split())
            outf.write("Case #%d: %s\n" % (i, str(count_all(minr, maxr))))

