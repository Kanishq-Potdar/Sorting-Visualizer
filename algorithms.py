from draw import draw_list
import pygame
pygame.mixer.init()
SWAP_SOUND = pygame.mixer.Sound("swap.wav")
SWAP_SOUND.set_volume(0.2)

def bubble_sort(draw_info, ascending=True):
    values = draw_info.values

    for i in range(len(values) - 1):
        for j in range(len(values) - 1 - i):
            num1 = values[j]
            num2 = values[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                values[j], values[j + 1] = values[j + 1], values[j]
                SWAP_SOUND.play()
                pygame.time.delay(10) 
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True


def insertion_sort(draw_info, ascending=True):
    values = draw_info.values

    for i in range(1, len(values)):
        current = values[i]

        while True:
            ascending_sort = i > 0 and values[i - 1] > current and ascending
            descending_sort = i > 0 and values[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            values[i] = values[i - 1]
            i -= 1
            values[i] = current
            SWAP_SOUND.play()
            pygame.time.delay(10)
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True


def merge_sort(draw_info, ascending=True):
    values = draw_info.values

    def merge_sort_recursive(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort_recursive(start, mid)
            yield from merge_sort_recursive(mid, end)

            merged = []
            left = start
            right = mid

            while left < mid and right < end:
                if (values[left] <= values[right] and ascending) or (values[left] >= values[right] and not ascending):
                    merged.append(values[left])
                    left += 1
                else:
                    merged.append(values[right])
                    right += 1

            while left < mid:
                merged.append(values[left])
                left += 1

            while right < end:
                merged.append(values[right])
                right += 1

            for i, val in enumerate(merged):
                values[start + i] = val
                SWAP_SOUND.play()
                pygame.time.delay(10)
                draw_list(draw_info, {start + i: draw_info.GREEN}, True)
                yield True

    yield from merge_sort_recursive(0, len(values))

def quick_sort(draw_info, ascending=True):
    lst = draw_info.values
    yield from _quick_sort(draw_info, lst, 0, len(lst)-1, ascending)

def _quick_sort(draw_info, lst, low, high, ascending):
    if low < high:
        pivot_index = yield from partition(draw_info, lst, low, high, ascending)
        yield from _quick_sort(draw_info, lst, low, pivot_index - 1, ascending)
        yield from _quick_sort(draw_info, lst, pivot_index + 1, high, ascending)


def partition(draw_info, lst, low, high, ascending):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            SWAP_SOUND.play()
            pygame.time.delay(10)
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
            yield True

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    SWAP_SOUND.play()
    pygame.time.delay(10)
    draw_list(draw_info, {i + 1: draw_info.GREEN, high: draw_info.RED}, True)
    yield True
    return i + 1

def selection_sort(draw_info, ascending=True):
    values = draw_info.values
    n = len(values)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_info.comparisons += 1
            if (values[j] < values[min_idx] and ascending) or (values[j] > values[min_idx] and not ascending):
                min_idx = j
            yield True
            draw_list(draw_info, {j: draw_info.RED, min_idx: draw_info.GREEN, i: draw_info.GREEN}, True)

        if min_idx != i:
            values[i], values[min_idx] = values[min_idx], values[i]
            draw_info.swaps += 1
            SWAP_SOUND.stop()
            SWAP_SOUND.play()
            yield True
            draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        yield True


def heap_sort(draw_info, ascending=True):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            draw_info.comparisons += 1
            if (values[left] > values[largest] and ascending) or (values[left] < values[largest] and not ascending):
                largest = left

        if right < n:
            draw_info.comparisons += 1
            if (values[right] > values[largest] and ascending) or (values[right] < values[largest] and not ascending):
                largest = right

        if largest != i:
            values[i], values[largest] = values[largest], values[i]
            draw_info.swaps += 1
            SWAP_SOUND.stop()
            SWAP_SOUND.play()
            yield True
            draw_list(draw_info, {i: draw_info.RED, largest: draw_info.GREEN}, True)
            yield from heapify(n, largest)

    values = draw_info.values
    n = len(values)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)

    for i in range(n - 1, 0, -1):
        values[i], values[0] = values[0], values[i]
        draw_info.swaps += 1
        SWAP_SOUND.stop()
        SWAP_SOUND.play()
        yield True
        draw_list(draw_info, {i: draw_info.RED, 0: draw_info.GREEN}, True)
        yield from heapify(i, 0)
