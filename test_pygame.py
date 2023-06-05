import pygame

from pygame_recorder import ScreenRecorder

pygame.init()
# settings
video_duration = 3  # seconds
FPS = 30
screen_size = (100, 100)  # pixels (x,y)

# colors
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)

# text input
inpt = input()

# pygame settings
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# font settings
font = pygame.font.SysFont("cambria", 45)
# rendering text
text = font.render(inpt, True, WHITE, PURPLE)
# recorder settings
recorder = ScreenRecorder(screen_size[0], screen_size[1], FPS)  # (screen frame size x, screen frame size y, fps)
# text starting position settings
x, y = screen_size[0], screen_size[1] / 2 - text.get_height() / 2
# text moving speed settings
dx = (text.get_width() + screen_size[0] / 2) / (FPS * video_duration)

count = 0
total_frames = FPS * video_duration + 1
while count < total_frames:
    clock.tick(FPS)
    screen.fill(PURPLE)
    screen.blit(text, (x, y))
    pygame.display.update()
    recorder.capture_frame(screen)
    x -= dx
    count += 1
recorder.end_recording()
