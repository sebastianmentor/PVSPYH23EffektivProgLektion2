from coder import Coder

def insertion_sorter(coders:list[Coder]) -> None:
    """Sort a list inplace with insertion sorting method"""
    n = len(coders)

    for i in range(1, n):
        current_coder = coders[i]

        j = i - 1
        while j >= 0 and current_coder < coders[j]:
            coders[j + 1] = coders[j]
            j -= 1

        coders[j+1] = current_coder

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

insertion_sorter(list_of_coders)

for coder in list_of_coders:
    print(coder)
