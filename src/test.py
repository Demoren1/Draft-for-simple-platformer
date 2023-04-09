import pygame
pygame.init()

# определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# настройка окна
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Double Tap Demo")

# переменные для обработки двойного нажатия на клавишу "space"
last_space_down = 0
double_space = False

# основной цикл программы
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # обработка двойного нажатия на клавишу "space"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - last_space_down < 200:
            double_space = True
            last_space_down = 0
        else:
            last_space_down = current_time

    # отображение текста на экране
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    if double_space:
        text = font.render("Double Space!", True, BLACK)
    else:
        text = font.render("Press Space Twice!", True, BLACK)
    text_rect = text.get_rect(center=(size[0]//2, size[1]//2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
