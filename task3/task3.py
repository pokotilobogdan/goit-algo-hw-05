from search_algorithms import kmp_search, boyer_moore_search, rabin_karp_search
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np


real_substring_start = "автори публiкації"
real_substring_middle = "відрізняється"
real_substring_end = "література"
fake_substring = "алгоритми алго"

test_substrings = [real_substring_start, real_substring_middle, real_substring_end, fake_substring]
search_methods = [kmp_search, boyer_moore_search, rabin_karp_search]

# Зберігаємо статті у вигляді об'єктів str
with open("article1.txt", 'r', encoding="utf-8") as fh:
        article1 = fh.read()
        
with open("article2.txt", 'r', encoding="utf-8") as fh:
        article2 = fh.read()


def test_search(search_method: callable, text: str, substring: str):
    """
    Функція повертає час пошуку даного підрядка для заданого текста
    """
    return timeit(f'{search_method(text, substring)}', number = 1000000)


# Збираємо дані вимірювань
        
    # Результат буде у форматі
    #        
        # results =
        # {
        # "Article1":{
        #           "substring1":   {
        #                           method1: [100 results], 
        #                           method2: [100 results],
        #                           method3: [100 results]  
        #                           },
        #           "substring2":   {
        #                           method1: [100 results], 
        #                           method2: [100 results],
        #                           method3: [100 results]  
        #                           }, 
        #           ...       
        #            },
        #    
        # "Article2": {...}        
        # }
       
results = {}
        
# Для кожної зі статей...
for article in [article1, article2]:
    
    article_results = {}
    
    # Кожен підрядок...
    for substring in test_substrings:
        substring_results = {}
        
        # Шукаємо кожним з методів пошуку...
        for method in search_methods:
            substring_results[method] = []
            
            # 100 разів
            for _ in range(100):
                substring_results[method].append(test_search(method, article, substring))
        article_results[substring] = substring_results
    results[article] = article_results


def draw_multiple_histograms(arrays, bins=50, grid_shape=(2, 2)):
    """
    Draw a figure with multiple subplots, each containing three histograms.

    Parameters:
        arrays (list of lists): List of integer arrays to plot. Each element should be a list of 3 arrays.
        bins (int): Number of bins for the histograms.
        grid_shape (tuple): Shape of the grid (rows, columns) for plotting subplots.
    """
    num_subplots = len(arrays)
    rows, cols = grid_shape
    
    if rows * cols < num_subplots:
        raise ValueError("Grid shape is too small for the number of subplots")
    
    fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
    axes = axes.flatten()  # Flatten in case grid_shape is more than 1 row/column
    
    # Determine global bin edges to ensure consistent bar widths
    min_val = min(min(min(array) for array in triplet) for triplet in arrays)
    max_val = max(max(max(array) for array in triplet) for triplet in arrays)
    bin_edges = np.linspace(min_val, max_val, bins + 1)

    colors = ['blue', 'green', 'red']
    labels = ['kmp', 'bm', 'rk']
    
    for i, (triplet, ax) in enumerate(zip(arrays, axes)):
        for j, (array, color, label) in enumerate(zip(triplet, colors, labels)):
            ax.hist(array, bins=bin_edges, alpha=0.6, color=color, edgecolor='black', label=label)
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        ax.set_title(f'{test_substrings[i]}')
        ax.grid(True)
        ax.legend()
        
    plt.tight_layout()  


# Досліджуємо дані дві статті:
for article in [article1, article2]:
    draw_multiple_histograms([substrings.values() for substrings in results[article].values()], bins=100)

plt.show()
