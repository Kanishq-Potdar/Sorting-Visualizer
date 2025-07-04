import pygame
import random
from draw import DrawInfo, draw
from algorithms import bubble_sort, insertion_sort


def generate_random_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    values = generate_random_list(n, min_val, max_val)

    draw_info = DrawInfo(800, 600, values)

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

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

    pygame.quit()


if __name__ == "__main__":
    main()
