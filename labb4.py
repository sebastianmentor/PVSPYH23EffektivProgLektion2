from timeit import default_timer
from helperfunctions import create_list_of_n_coders
from labb1 import bubble_sorter

coders_1000 = create_list_of_n_coders(1000)
coders_2000 = create_list_of_n_coders(2000)
coders_4000 = create_list_of_n_coders(4000)
coders_8000 = create_list_of_n_coders(8000)


t_start = default_timer()
bubble_sorter(coders_1000)
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 1000 kodare!')
t_start = default_timer()
bubble_sorter(coders_2000)
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 2000 kodare!')
t_start = default_timer()
bubble_sorter(coders_4000)
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 4000 kodare!')
t_start = default_timer()
bubble_sorter(coders_8000)
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 8000 kodare!')
