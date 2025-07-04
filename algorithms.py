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
