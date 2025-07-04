from draw import draw_list

def bubble_sort(draw_info, ascending=True):
    values = draw_info.values

    for i in range(len(values) - 1):
        for j in range(len(values) - 1 - i):
            num1 = values[j]
            num2 = values[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                values[j], values[j + 1] = values[j + 1], values[j]
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
                draw_list(draw_info, {start + i: draw_info.GREEN}, True)
                yield True

    yield from merge_sort_recursive(0, len(values))