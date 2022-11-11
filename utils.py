import numpy as np
from matplotlib import pyplot as plt
from random import random


def cdf(log):
    log.sort()
    x = np.linspace(min(log), max(log), 100)
    c = []
    add = c.append
    for n in x:
        i = 0
        for p in log:
            if p <= n:
                i += 1
            else:
                break
        add(i / len(log))
    return x, c


def run(func_def, trials):
    closure = dict()
    s = "def g(U):\n"
    for row in func_def.split('\n'):
        s += f'\t{row}\n'
    exec(s, closure)
    g = closure['g']

    log = []

    add = log.append

    for _ in range(trials):
        add(g(random()))
    
    return log, g


def plot_density(log):
    fig, _ = plt.subplots()
    plt.hist(log, 50, density=True)
    plt.xlabel('g(U)')
    plt.ylabel('count')
    plt.title('Distribution')
    return fig


def plot_cdf(log):
    fig, _ = plt.subplots()
    xs, ys = cdf(log)
    plt.plot(xs, ys)
    plt.ylim((0, 1))
    plt.xlabel('k')
    plt.ylabel('P(g(U) <= k')
    plt.title('CDF')
    return fig

def plot(g):
    fig, _ = plt.subplots()
    xs = np.linspace(0, 1, 100)
    plt.plot(xs, [g(x) for x in xs])
    plt.xlabel('U')
    plt.ylabel('g(U)')
    plt.title('g(U)')
    return fig
