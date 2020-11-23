import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def initArr():
    arr = [random.randint(1, 100)]*100
    for i in range(len(arr)):
        arr[i] = random.randint(1, 100)
    return arr

arr = initArr()
x = len(arr)

def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a
    # also in python A[i],A[j]=A[j],A[i]

def insertionSort(arr):
    if(len(arr)==1):
        return
    for i in range(1,len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            swap(arr,j,j-1)
            j-=1
            yield arr


# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# ax.bar(x, arr)

fig, ax = plt.subplots()
ax.set_title("Sorting Visualizer :)")
bar_rect = ax.bar(range(len(arr)), arr, align='edge')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]
def update_plot(arr, rect, epochs):
    for rect, val in zip(rect, arr):
        rect.set_height(val)
    epochs[0] += 1
    text.set_text("No.of operations :{}".format(epochs[0]))


algorithm = insertionSort(arr)
anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rect, epochs), frames=algorithm, interval=1, repeat=False)
plt.show()