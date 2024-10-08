from timeit import default_timer
from helperfunctions import create_list_of_n_coders
from labb3 import selection_sorter

coders_1000 = create_list_of_n_coders(1000)
coders_2000 = create_list_of_n_coders(2000)
coders_4000 = create_list_of_n_coders(4000)
coders_8000 = create_list_of_n_coders(8000)
coders_16000 = create_list_of_n_coders(16000)
coders_32000 = create_list_of_n_coders(32000)
coders_128000 = create_list_of_n_coders(128000)
coders_512000 = create_list_of_n_coders(512000)
coders_2048000 = create_list_of_n_coders(2048000)


t_start = default_timer()
coders_1000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 1000 kodare!')
t_start = default_timer()
coders_2000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 2000 kodare!')
t_start = default_timer()
coders_4000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 4000 kodare!')
t_start = default_timer()
coders_8000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 8000 kodare!')
t_start = default_timer()
coders_16000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 16000 kodare!')
t_start = default_timer()
coders_32000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 32000 kodare!')
t_start = default_timer()
coders_128000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 128000 kodare!')
t_start = default_timer()
coders_512000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 512000 kodare!')
t_start = default_timer()
coders_2048000.sort()
t_end = default_timer()
print(f'Det tog {t_end - t_start} att sortera 2048000 kodare!')