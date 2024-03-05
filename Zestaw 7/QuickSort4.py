import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib
# matplotlib.use('MacOSX')
# ze względuna problemy z matplotlibem na macu uzylem zamiast plotly
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
def quick_sort(tablica: MonitorowanaTablica):

    def pivoting(tablica, left, right):
        i = left - 1
        pivot = tablica[right]
        for j in range(left, right):
            if tablica[j] < pivot:
                i += 1
                # zamiana miejscami
                tablica[i], tablica[j] = tablica[j], tablica[i]
        tablica[i+1], tablica[right] = tablica[right], tablica[i+1]
        return i+1

    def partition(tablica, left, right):
        if left < right:
            balance = pivoting(tablica, left, right)
            partition(tablica, left, balance-1)
            partition(tablica, balance+1, right)

    partition(tablica, 0, len(tablica)-1)


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


test_fuction(quick_sort)