import pygame
import random
from draw import DrawInfo, draw, Button
from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort

def generate_random_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    values = generate_random_list(n, min_val, max_val)

    draw_info = DrawInfo(1200, 600, values)

    #--- Button Setup ---

    button_width = 140
    button_height  = 40
    button_x = draw_info.width - button_width - 80
    button_y_start = 100
    button_spacing = 10

    buttons = []

    def set_sort_algorithm(algo, name):
        def inner():
            nonlocal sorting_algorithm, algorithm_name
            sorting_algorithm = algo
            algorithm_name = name
        return inner
    
    def start_sort():
        nonlocal sorting, sorting_algorithm_generator
        if not sorting:
            sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            sorting = True

    def step_sort():
        nonlocal sorting, step_mode, step_once
        if not sorting:
            sorting = True
            step_mode = True
            step_once = True

    def resume_sort():
        nonlocal step_mode
        step_mode = False

    def reset_array():
        nonlocal values, sorting
        values = generate_random_list(n, min_val, max_val)
        draw_info.set_list(values)
        sorting = False

    def set_ascending():
        nonlocal ascending 
        ascending = True

    def set_descending():
        nonlocal ascending 
        ascending = False

    button_data = [
        ("Step", step_sort),
        ("Resume", resume_sort),
        ("Start", start_sort),
        ("Reset", reset_array),
        ("Ascend", set_ascending),
        ("Descend", set_descending),
        ("Bubble", set_sort_algorithm(bubble_sort, "Bubble Sort")),
        ("Insertion", set_sort_algorithm(insertion_sort, "Insertion Sort")),
        ("Merge", set_sort_algorithm(merge_sort, "Merge Sort")),
        ("Quick", set_sort_algorithm(lambda draw_info, asc: quick_sort(draw_info, asc), "Quick Sort"))
    ]


    for i, (label, action) in enumerate(button_data):
        y = button_y_start + i * (button_height + button_spacing)
        btn = Button(
            button_x, y,
            button_width, button_height,
            label,
            draw_info.FONT,
            draw_info.WHITE, draw_info.BLACK,
            (200,200,200), #hover color
            callback = action
        )

        buttons.append(btn)

    draw_info.buttons = buttons

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    step_mode = False
    step_once = False

    while run:
        clock.tick(60)

        if sorting:
            try:
                if not step_mode or step_once:
                    next(sorting_algorithm_generator)
                    step_once = False
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for btn in draw_info.buttons:
                    btn.check_click(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    values = generate_random_list(n, min_val, max_val)
                    draw_info.set_list(values)
                    sorting = False

                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

                elif event.key == pygame.K_a and not sorting:
                    ascending = True

                elif event.key == pygame.K_d and not sorting:
                    ascending = False

                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    algorithm_name = "Insertion Sort"

                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    algorithm_name = "Bubble Sort"

                elif event.key == pygame.K_m and not sorting:
                    sorting_algorithm = merge_sort
                    algorithm_name = "Merge Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
