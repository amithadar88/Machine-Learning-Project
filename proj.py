import pandas as pd
import numpy as np


def weight_the_graph(source: list, target: list):
    mem = {}
    i = 0
    for s, t in zip(source, target):
        k = (s, t)
        mem[k] = mem.get(k, 0) + 1

    new_source = []
    new_target = []
    weightes = []
    for k, v in mem.items():
        new_source.append(k[0])
        new_target.append(k[1])
        weightes.append(v)
    return (new_source, new_target, weightes)


source = [1, 2, 1, 3, 9, 3]
target = [2, 1, 2, 4, 4, 4]

print(weight_the_graph(source, target))
