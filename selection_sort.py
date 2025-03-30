"""Selection Sort
"""

def selection_sort(list1):
    passes = 0
    for i in range(passes, len(list1)):
        for j in range(passes+1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]

        passes += 1

if __name__ == "__main__":
    list1 = [55, 20, 4, 89, 65, 1, 95, 3]
    selection_sort(list1)
    print(list1)                