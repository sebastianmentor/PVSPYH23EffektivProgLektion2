from coder import Coder

def selection_sorter(coders:list[Coder]) -> None:
    """Sort a list of Coder inplace!"""

    n = len(coders)

    for i in range(n):
        lazy_coder = i
        
        for j in range(i + 1, n):
            if coders[j] < coders[lazy_coder]:
                lazy_coder = j

        coders[i], coders[lazy_coder] = coders[lazy_coder], coders[i]

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

selection_sorter(list_of_coders)

for coder in list_of_coders:
    print(coder)

