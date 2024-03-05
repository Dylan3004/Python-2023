import time
from mtablica import MonitorowanaTablica
import numpy as np
import matplotlib
# matplotlib.use('MacOSX')
# ze względuna problemy z matplotlibem na macu uzylem zamiast plotly
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

#wczesniejsza wersja działa ona szybciej natomast nie da sie zmierzyc ilosci operacji tak jak podane jest to w zadaniu

def prev_merge_sort(tablica: MonitorowanaTablica):

        def welder(left, right):
            result_array = []
            while len(left) > 0 and len(right) > 0:
                if left[0] < right[0]:
                    result_array.append(left[0])
                    left = left[1:]
                else:
                    result_array.append(right[0])
                    right = right[1:]
            if len(left) == 0:
                result_array.extend(right)
            else:
                result_array.extend(left)
            # print(result_array)
            return np.array(result_array)

        if len(tablica) == 1:
            return tablica

        mid = len(tablica) // 2
        left = tablica[:mid]
        right = tablica[mid:]

        left = prev_merge_sort(left)
        right = prev_merge_sort(right)

        return welder(left, right)


################################################################

def merge_sort(tablica: MonitorowanaTablica):

    def welder(tablica, left, mid, right):
        #tworzenie tablic pomocniczych
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

        #scalenie tablic
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

    def merge_sort_rec(tablica, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_rec(tablica, left, mid)
            merge_sort_rec(tablica, mid + 1, right)
            welder(tablica, left, mid, right)

    merge_sort_rec(tablica, 0, len(tablica) - 1)



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


test_fuction(merge_sort)