import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def initArr():
    arr = [random.randint(1, 100)]*100
    for i in range(len(arr)):
        arr[i] = random.randint(1, 100)
    return arr

def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a
    # also in python A[i],A[j]=A[j],A[i]


def quickSort(arr,p,q):
    if p >= q:
        return
    piv = arr[q]
    pivotIdx = p
    for i in range(p, q):
        if arr[i] < piv:
            swap(arr,i,pivotIdx)
            pivotIdx += 1
        yield arr
    swap(arr, q, pivotIdx)
    yield arr

    yield from quickSort(arr,p,pivotIdx-1)
    yield from quickSort(arr,pivotIdx+1,q)


def insertionSort(arr):
    if(len(arr)==1):
        return
    for i in range(1,len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            swap(arr,j,j-1)
            j-=1
            yield arr


arr = initArr()
fig, ax = plt.subplots()
ax.set_title("Sort Visualizer :)")
bar_rect = ax.bar(range(len(arr)), arr, align='edge')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]
def update_plot(arr, rect, epochs):
    for rect, val in zip(rect, arr):
        rect.set_height(val)
    epochs[0] += 1
    text.set_text("No.of operations :{}".format(epochs[0]))

# algorithm = insertionSort(arr)
algorithm = quickSort(arr, 0, len(arr) - 1)
anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rect, epochs), frames=algorithm, interval=1, repeat=False)
plt.show()