import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    #check for all events
    # vai checar todos os eventos que passarem
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             print('Quitting...')
             pygame.quit() # Close window
             quit() #end pygame
