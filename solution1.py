import numpy as np
import matplotlib.pyplot as plt


def fitness(x):
    return 10 * np.sin(5 * x) + 7 * abs(x - 5) + 10


class individual:
    def __init__(self):
        self.x = 0
        self.fitness = 0

    def __eq__(self, other):
        self.x = other.x
        self.fitness = other.fitness


def initPopulation(ppl, n):
    for i in range(n):
        indi = individual()
        indi.x = np.random.uniform(0, 10)
        indi.fitness = fitness(indi.x)
        ppl.append(indi)


def selection(n):
    return np.random.choice(n, 2)


def crossover(p1: individual, p2: individual):
    child_1 = individual()
    child_2 = individual()
    child_1.x = 0.9 * p1.x + 0.1 * p2.x
    child_2.x = 0.1 * p1.x + 0.9 * p2.x
    child_1.fitness = fitness(child_1.x)
    child_2.fitness = fitness(child_2.x)
    return child_1, child_2


def mutation(ppl):
    indi = np.random.choice(ppl)
    indi.x = np.random.uniform(0, 10)
    indi.fitness = fitness(indi.x)


def implement():
    n = 20
    ppl = []
    iter_n = 50
    initPopulation(ppl, n)
    best_res = [0, 0, 0]
    res_lst = []
    for it in range(iter_n):
        a, b = selection(n)
        if np.random.random() < 0.75:
            c1, c2 = crossover(ppl[a], ppl[b])
            new = sorted([ppl[a], ppl[b], c1, c2], key=lambda indi: indi.fitness, reverse=True)
            ppl[a], ppl[b] = new[0], new[1]
        if np.random.random() < 0.1:
            mutation(ppl)
        ppl.sort(key=lambda indi: indi.fitness, reverse=True)
        res_lst.append(ppl[0].fitness)
        if ppl[0].fitness > best_res[1]:
            best_res[0] = ppl[0].x
            best_res[1] = ppl[0].fitness
            best_res[2] = it
    print('最佳结果：x={0:.2f},fitness={1:.2f} 该结果首次出现在第{2}轮迭代'.format(best_res[0], best_res[1], best_res[2]))
    x = [_ for _ in range(iter_n)]
    plt.plot(x,res_lst,color='green')
    plt.show()
    return ppl


if __name__ == '__main__':
    ppl = implement()
