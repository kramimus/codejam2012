#!/usr/bin/env python3

import sys

"""Solution to dancing with the googlers gcj2012 problem."""

__author__      = "Mark Whitney"
__copyright__   = "Copyright 2012, Mark Whitney"

def count_p_pluses(p, s, scores):
    min_non_surprising = max(p, p * 3 - 2)
    min_surprising = max(p, p * 3 - 4)
    non_surprising_pass = sum(score >= min_non_surprising for score in scores)
    surprising_only_pass = sum(score >= min_surprising and score < min_non_surprising for score in scores)
    return non_surprising_pass + min(s, surprising_only_pass)

if __name__ == "__main__":
    with open(sys.argv[1]) as f, open(sys.argv[2], "w") as out:
        count = int(f.readline())
        for i in range(1, count + 1):
            n, s, p, *scores = (int(j) for j in f.readline().strip().split())
            out.write("Case #%d: %d\n" % (i, count_p_pluses(p, s, scores)))
