import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort
from algorithms.heap import heap_sort


# ---------- THEME ----------
BACKGROUND = "#0a0f1f"
COLORS = {
    "Bubble Sort": {
        "base": "#2f6bff", "highlight": "#9bb6ff"
    },
    "Selection Sort": {
        "base": "#8a2be2", "highlight": "#c7a6f5"
    },
    "Insertion Sort": {
        "base": "#ff2fdc", "highlight": "#ff9ae9"
    },
    "Merge Sort": {
        "base": "#00e5ff", "highlight": "#8cf3ff"
    },
    "Quick Sort": {
        "base": "#ff3b3b", "highlight": "#ff9b9b"
    },
    "Heap Sort": {
        "base": "#ffb703", "highlight": "#ffe29a"
    }
}



# ---------- INPUT ----------
user_input = input("Enter numbers separated by space: ")
base_array = list(map(int, user_input.split()))

arrays = {name: base_array.copy() for name in COLORS}

generators = {
    "Bubble Sort": bubble_sort(arrays["Bubble Sort"]),
    "Selection Sort": selection_sort(arrays["Selection Sort"]),
    "Insertion Sort": insertion_sort(arrays["Insertion Sort"]),
    "Merge Sort": merge_sort(arrays["Merge Sort"]),
    "Quick Sort": quick_sort(arrays["Quick Sort"]),
    "Heap Sort": heap_sort(arrays["Heap Sort"])
}


fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()
fig.patch.set_facecolor(BACKGROUND)

# ---------- DRAW ----------
def draw(highlights):
    for ax, (name, arr) in zip(axes, arrays.items()):
        ax.clear()
        ax.set_facecolor(BACKGROUND)

        bar_colors = []
        for i in range(len(arr)):
            if highlights.get(name) and i in highlights[name]:
              bar_colors.append(COLORS[name]["highlight"])
            else:
              bar_colors.append(COLORS[name]["base"])


        ax.bar(range(len(arr)), arr, color=bar_colors)
        ax.set_title(name, color=COLORS[name]["base"])
        ax.set_xticks([])
        ax.set_yticks([])

speed = 0.25  # ← speed dial (smaller = faster)

while True:
    done = 0
    highlights = {}

    for name in generators:
        try:
            _, i, j = next(generators[name])
            highlights[name] = (i, j)
        except StopIteration:
            done += 1

    draw(highlights)
    plt.pause(speed)

    if done == len(generators):
        break

plt.show()
