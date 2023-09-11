from GameClasses.Interface.ClassInterface import Interface

from RenderedMedia import menu_animation_array


class MouseEffect(Interface):
    def __init__(self, sc, mouse):
        super().__init__()

        self.sc = sc
        self.mouse = mouse

        self.alive = 1

    def mouse_animation(self):
        m_size = [10, 12, 16, 20, 28, 34, 45, 48, 54, 58]

        draw_x = self.mouse[0] - m_size[int(self.animation_counter)] // 2
        draw_y = self.mouse[1] - m_size[int(self.animation_counter)] // 2

        self.sc.blit(menu_animation_array[int(self.animation_counter)], (draw_x, draw_y))
        self.animation_counter += 0.5

        if self.animation_counter == 10:
            self.animation_counter = 0

            self.key = 0
            self.alive = 0
