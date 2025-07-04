import pygame
import math

pygame.init()

class DrawInfo:
    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BACKGROUND_COLOR = WHITE

    # Gradient colors for bars
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    # Fonts for UI text
    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    # Padding
    SIDE_PAD = 150
    TOP_PAD = 150

    def __init__(self, width, height, values):
        self.width = width
        self.height = height

        # Create the pygame window
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(values)

    def set_list(self, values):
        self.values = values
        self.min_val = min(values)
        self.max_val = max(values)

      
        right_margin = 200  # space reserved for button panel
        usable_width = self.width - self.SIDE_PAD - right_margin
        self.block_width = round(usable_width / len(values))

        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    """Draw UI Text and bars."""
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Title
    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        True,
        draw_info.GREEN
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    draw_list(draw_info)

    if hasattr(draw_info, 'buttons'):
        mouse_pos = pygame.mouse.get_pos()
        for btn in draw_info.buttons:
            btn.check_hover(mouse_pos)
            btn.draw(draw_info.window)

    pygame.display.update()



def draw_list(draw_info, color_positions={}, clear_bg=False):
    values = draw_info.values

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(values):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

class Button:
    def __init__(self, x, y, width, hieght, text, font, bg_color, text_color, hover_color, callback=None):
        self.rect = pygame.Rect(x, y, width, hieght)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.iscallback = callback
        self.is_hovered = False

    def draw(self,surface):
        color = self.hover_color if self.is_hovered else self.bg_color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2) #border

        text_surf=self.font.render(self.text, True, self.text_color)
        surface.blit(
            text_surf,
            (
                self.rect.x + (self.rect.width - text_surf.get_width())//2,
                self.rect.y + (self.rect.height - text_surf.get_height())//2
            )
        )
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    
    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and self.callback:
            self.callback()
