import streamlit as st
import matplotlib.pyplot as plt

from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort
from algorithms.heap import heap_sort

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Sorting Algorithms Race",
    layout="wide"
)

st.title("🌌 Sorting Algorithms Race Visualizer")

st.markdown(
    "Enter a list of numbers and watch **six sorting algorithms** "
    "race side-by-side."
)

# ---------- USER INPUT ----------
user_input = st.text_input(
    "Enter numbers separated by spaces:"
)

run = st.button("🚀 Run Sorting Race")

# ---------- COLORS ----------
COLORS = {
    "Bubble Sort": {"base": "#2f6bff", "highlight": "#9bb6ff"},
    "Selection Sort": {"base": "#8a2be2", "highlight": "#c7a6f5"},
    "Insertion Sort": {"base": "#ff2fdc", "highlight": "#ff9ae9"},
    "Merge Sort": {"base": "#00e5ff", "highlight": "#8cf3ff"},
    "Quick Sort": {"base": "#ff3b3b", "highlight": "#ff9b9b"},
    "Heap Sort": {"base": "#39ff14", "highlight": "#9dff8f"},
}

BACKGROUND = "#0a0f1f"

# ---------- MAIN LOGIC ----------
if run:
    try:
        base_array = list(map(int, user_input.split()))
    except ValueError:
        st.error("Please enter only numbers separated by spaces.")
        st.stop()

    MAX_INPUT_SIZE = 20

    if len(base_array) > MAX_INPUT_SIZE:
        st.warning(
            f"For smooth animation, please enter {MAX_INPUT_SIZE} numbers or fewer."
        )
        st.stop()

    original_array = base_array.copy()
    final_sorted = sorted(base_array)

    arrays = {name: base_array.copy() for name in COLORS}

    generators = {
        "Bubble Sort": bubble_sort(arrays["Bubble Sort"]),
        "Selection Sort": selection_sort(arrays["Selection Sort"]),
        "Insertion Sort": insertion_sort(arrays["Insertion Sort"]),
        "Merge Sort": merge_sort(arrays["Merge Sort"]),
        "Quick Sort": quick_sort(arrays["Quick Sort"]),
        "Heap Sort": heap_sort(arrays["Heap Sort"]),
    }

    finished = set()
    finish_order = []

    # ---------- FIGURE ----------
    fig, axes = plt.subplots(2, 3, figsize=(12, 5.7))
    axes = axes.flatten()
    fig.patch.set_facecolor(BACKGROUND)
    plt.tight_layout(pad=2)
    plt.subplots_adjust(hspace=0.35, wspace=0.25)

    plot_placeholder = st.empty()

    STEPS_PER_FRAME = 5   
    FRAME_DELAY = 0.08


    # ---------- ANIMATION LOOP ----------
   import time
    while len(finished) < len(generators):
     highlights = {}

     for _ in range(STEPS_PER_FRAME):
        for name in generators:
            if name in finished:
                continue
            try:
                _, i, j = next(generators[name])
                highlights[name] = (i, j)
            except StopIteration:
                finished.add(name)
                finish_order.append(name)

     for ax, (name, arr) in zip(axes, arrays.items()):
         if name in finished:
             ax.clear()
             ax.bar(range(len(arr)), arr, color=COLORS[name]["base"])
             ax.set_title(f"{name} ✓", color=COLORS[name]["base"], fontsize=10)
             ax.set_xticks([])
             ax.set_yticks([])
             continue

        ax.clear()
        ax.set_facecolor(BACKGROUND)

        colors = [
            COLORS[name]["highlight"] if highlights.get(name) and i in highlights[name]
            else COLORS[name]["base"]
            for i in range(len(arr))
        ]

        ax.bar(range(len(arr)), arr, color=colors)
        ax.set_title(name, color=COLORS[name]["base"], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

     with plot_placeholder:
        st.pyplot(fig)

     time.sleep(FRAME_DELAY)

    # ---------- LEADERBOARD ----------
    st.markdown("### 🏁 Leaderboard")
    for i, algo in enumerate(finish_order, 1):
        st.markdown(f"**{i}. {algo}**")

    # ---------- DISPLAY INPUT / OUTPUT CLEANLY ----------
    st.markdown("### 📥 Input & 📤 Output")
    st.code(f"Input  : {original_array}")
    st.code(f"Sorted : {final_sorted}")

