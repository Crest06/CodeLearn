import random
import pygame

pygame.init()
width, height=600, 600
window=pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake and Ladder")
rows, cols=10,10 

rect_height=height//cols
rect_width=width//rows

background_color=(0, 255,0)
outline_thickness=5
grid1=[]
numbers=[i for i in range(1,100)]


def set_grid():
    for row in range(rows):
        for col in range(cols):
            grid1.append((row,col))
            print(numbers)
            

    
        

    for col in range(1, cols):
        x=col*rect_width
        


def draw_grid(Window):
    for row in range(1, rows):
        y=row*rect_height
        pygame.draw.line(Window, (0,0,0), (0,y), (width,y),outline_thickness)

    for col in range(1, cols):
        x=col*rect_width
        pygame.draw.line(Window, (0,0,0),(x,0), (x,height),outline_thickness)


def draw(window):
    window.fill(background_color)
    draw_grid(window)
    pygame.display.update()


def main():
    set_grid()
    run=True
    while run:
        for events in pygame.event.get():
            if events.type ==pygame.QUIT:
                run=False
                break
        draw(window)
        
    pygame.quit()

if __name__=="__main__":
    main()

