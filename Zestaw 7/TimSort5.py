import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib
# matplotlib.use('MacOSX')
# ze względuna problemy z matplotlibem na macu uzylem zamiast plotly
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation


def insertion_sort(tablica: MonitorowanaTablica, left=0, right=None):
    # UWAGA: algorytm został zmieniony na potrzeby tim sorta
    '''Performs the insertion sort on the given array.

    Args:
    tablica (MonitorowanaTablica): The array to be sorted.
    '''
    if right is None:
        right = len(tablica) - 1

    for i in range(left + 1, right + 1):
        key_item = tablica[i]
        j = i - 1
        while j >= left and tablica[j] > key_item:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = key_item


################################################################



# do tim sorta
def welder(tablica, left, mid, right):
    # tworzenie tablic pomocniczych
    leftSize = mid - left + 1
    rightSize = right - mid
    Left = [0] * (leftSize)
    Right = [0] * (rightSize)
    for i in range(0, leftSize):
        Left[i] = tablica[left + i]
    for j in range(0, rightSize):
        Right[j] = tablica[mid + 1 + j]
    i = 0
    j = 0
    sorceTableIndex = left

    # scalenie tablic
    while i < leftSize and j < rightSize:
        if Left[i] <= Right[j]:
            tablica[sorceTableIndex] = Left[i]
            i += 1
        else:
            tablica[sorceTableIndex] = Right[j]
            j += 1
        sorceTableIndex += 1
    while i < leftSize:
        tablica[sorceTableIndex] = Left[i]
        i += 1
        sorceTableIndex += 1
    while j < rightSize:
        tablica[sorceTableIndex] = Right[j]
        j += 1
        sorceTableIndex += 1
    return tablica


###############################################################


def tim_sort(tablica: MonitorowanaTablica):

    min_run = 30
    n = len(tablica)

    for i in range(0, n, min_run):
        insertion_sort(tablica, i, min((i + min_run - 1), n - 1))

    curr_size = min_run
    while curr_size < n:
        for left in range(0, n, 2 * curr_size):
            mid = min(n - 1, left + curr_size - 1)
            right = min((left + 2 * curr_size - 1), (n - 1))
            welder(tablica, left, mid, right)
        curr_size *= 2

    return tablica


################################################################
def plot_sorting_animation(tablica: MonitorowanaTablica, algorithm_name: str, fps=60):
    '''Plots the sorting animation for the given data.

    Args:
    tablica (MonitorowanaTablica): The array being sorted.
    algorithm_name (str): Name of the sorting algorithm.
    fps (int): Frames per second for the animation.
    '''
    plt.rcParams['font.size'] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(range(len(tablica)), tablica.pelne_kopie[0], align='edge', width=0.8)
    fig.suptitle(f'Sorting: {algorithm_name}')
    ax.set(xlabel='Index', ylabel='Value')
    ax.set_xlim([0, len(tablica)])
    txt = ax.text(0.01, 0.99, '', ha='left', va='top', transform=ax.transAxes)

    def update(frame: int):
        '''Updates the histogram for each frame of the animation.

        Args:
        frame (int): The current frame number.
        '''
        txt.set_text(f'Operations = {frame}')
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color('darkblue')

        idx, op = tablica.aktywnosc(frame)
        if op == 'get':
            container.patches[idx].set_color('green')
        elif op == 'set':
            container.patches[idx].set_color('red')

        return (txt, *container)

    ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000. / (fps / 1),
                        repeat=False)
    plt.show()
    # prev : frames=range(len(tablica.pelne_kopie))


################################################################
def test_fuction(sorting_function):
    Tablica1 = MonitorowanaTablica(0, 1000, 50, tryb='R')
    Tablica2 = MonitorowanaTablica(0, 1000, elem=50, tryb='S')
    Tablica3 = MonitorowanaTablica(0, 1000, elem=50, tryb='A')
    Tablica4 = MonitorowanaTablica(0, 1000, elem=50, tryb='T')
    string0 = "Sorting: " + str(sorting_function.__name__)
    t0 = time.perf_counter()
    sorting_function(Tablica1)
    delta_t = time.perf_counter() - t0
    string1 = f"R:Array sorted in {delta_t * 1000:.1f} ms. Number of operations: " + str(len(Tablica1.pelne_kopie))
    t0 = time.perf_counter()
    sorting_function(Tablica2)
    delta_t = time.perf_counter() - t0
    string2 = f"S:Array sorted in {delta_t * 1000:.1f} ms. Number of operations: " + str(len(Tablica2.pelne_kopie))
    sorting_function(Tablica3)
    delta_t = time.perf_counter() - t0
    string3 = f"A:Array sorted in {delta_t * 1000:.1f} ms. Number of operations: " + str(len(Tablica3.pelne_kopie))
    sorting_function(Tablica4)
    delta_t = time.perf_counter() - t0
    string4 = f"T:Array sorted in {delta_t * 1000:.1f}  ms. Number of operations: " + str(len(Tablica4.pelne_kopie))
    print(Tablica1.tablica)
    print(Tablica2.tablica)
    print(Tablica3.tablica)
    print(Tablica4.tablica)
    with open('testy.txt', 'a') as file:
        file.write(string0 + '\n')
        file.write(string1 + '\n')
        file.write(string2 + '\n')
        file.write(string3 + '\n')
        file.write(string4 + '\n')


test_fuction(tim_sort)