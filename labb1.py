from coder import Coder

def bubble_sorter(coders:list[Coder]) -> None:
    '''Uses bubblesort to sort a list of Coder inplace'''

    n = len(coders)

    for i in range(n):
        for j in range(0, n - i -1):
            if coders[j] > coders[j+1]:
                coders[j], coders[j+1] = coders[j+1], coders[j]

    return None

list_of_coders = [
        Coder('kalle', 2.2),
        Coder('Erik', 2.2),
        Coder('Fia', 3.5),
        Coder('Patrik', 8.1),
        Coder('Sven', 1.2),
        Coder('Nisse', 0.2 ),
        Coder('Lina', 3.3),
        Coder('Lisa', 5.5),
        Coder('Göran', 7.0),
        Coder('Amanda', 4.8)
        ]

bubble_sorter(list_of_coders)

for coder in list_of_coders:
    print(coder)
