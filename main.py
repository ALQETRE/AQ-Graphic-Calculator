import pygame, os, time, math
from clipboard import copy, paste

pygame.init()

width = 400
height = 600

base_font = pygame.font.Font("Font.ttf", 30)

fps = 60

color1 = pygame.Color("lightskyblue3")
color2 = (0, 0, 0)
color3 = (225, 225, 225)

py = 3.141592653589

history = []

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graphic Calculator")
win.fill(color3)
rect = pygame.Rect(0, 400, 400, 5)
pygame.draw.rect(win, color1, rect)
pygame.display.update()

def get_text_input(x, y, text1):
    back_round_text = pygame.Rect(x-110, y-25, 220, 50)
    text = text1
    enter = True
    while enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                enter = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    enter = False
                else:
                    if text == text1:
                        text = ""
                    if len(text) < 12:
                        text += event.unicode
        if pygame.key.get_pressed()[pygame.K_LCTRL] and pygame.key.get_pressed()[pygame.K_v]:
            text = paste()

        pygame.draw.rect(win, color1, back_round_text)
        text_sf = base_font.render(text, True, color3)
        win.blit(text_sf, (back_round_text.x+10, back_round_text.y+10))
        pygame.display.update()
    pygame.draw.rect(win, color3, back_round_text)
    pygame.display.update()
    try:
        return float(text)
    except ValueError:
        pygame.draw.rect(win, color1, back_round_text)
        text_sf = base_font.render("Try again.", True, color3)
        win.blit(text_sf, (back_round_text.x+10, back_round_text.y+10))
        pygame.display.update()
        time.sleep(0.5)
        return get_text_input(x, y, text1)

def button(x, y, text, quest):
    idx = 0
    clock = pygame.time.Clock()
    run = True
    pressed = True

    while run:
        clock.tick(fps)
        pos = pygame.mouse.get_pos()
        back_rect = pygame.Rect(x-75, y-30, 150, 60)
        pygame.draw.rect(win, color1, back_rect)
        text_sf = base_font.render(text[idx%len(text)].center(12), True, color3)
        win.blit(text_sf, (x-75, y+17-33))
        text_sf = base_font.render(quest.center(20), True, color2)
        win.blit(text_sf, (x-120, y+17-33-60))
        pygame.display.update()


        if back_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and pressed == False:
                pressed = True
                rect = pygame.Rect(x-125, y-100, 250, 140)
                pygame.draw.rect(win, color3, rect)
                pygame.display.update()
                return text[idx%len(text)]
        if pygame.mouse.get_pressed()[0] == 0:
            pressed = False

        pos = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if back_rect.collidepoint(pos):
                if event.type == pygame.MOUSEWHEEL:
                    idx += event.y
                    event.y = 0
    pygame.quit()

def add_history(text):
    if len(history) == 0:
        history.append(str(text))
    elif not str(text) == history[-1]:
        history.append(str(text))

def obvod():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)
    rad = get_text_input(200, 500, "(Radius)")
    circ = round(rad*2*py*100000)/100000
    multi = 100/rad
    pygame.draw.circle(win, color1, (200, 210), rad*multi, 7)
    text_sf = base_font.render(str(rad).center(6), True, color2)
    win.blit(text_sf, (170+rad*multi/2, 210))
    text_sf = base_font.render(str(circ).center(8), True, color2)
    win.blit(text_sf, (140, 220+rad*multi))
    rad_rect = pygame.Rect(200, 208, rad*multi, 4)
    pygame.draw.rect(win, color2, rad_rect)
    pygame.draw.circle(win, color1, (200, 210), 5)
    pygame.display.update()
    add_history(circ)

def rad_circ():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)
    circ = get_text_input(200, 500, "(Circum.)")
    rad = round((circ/2/py)*100000)/100000
    multi = 100/rad
    pygame.draw.circle(win, color1, (200, 210), rad*multi, 7)
    text_sf = base_font.render(str(rad).center(10), True, color2)
    win.blit(text_sf, (90+rad*multi, 210))
    text_sf = base_font.render(str(circ).center(8), True, color2)
    win.blit(text_sf, (140, 220+rad*multi))
    rad_rect = pygame.Rect(200, 208, rad*multi, 4)
    pygame.draw.rect(win, color2, rad_rect)
    pygame.draw.circle(win, color1, (200, 210), 5)
    pygame.display.update()
    add_history(rad)



def rad_cont():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)
    cont = get_text_input(200, 500, "(Content)")
    rad = round((math.sqrt(cont/py))*100000)/100000
    circ = round(rad*2*py*100000)/100000
    multi = 100/rad
    pygame.draw.circle(win, color1, (200, 210), rad*multi, 7)
    text_sf = base_font.render(str(rad).center(6), True, color2)
    win.blit(text_sf, (100+rad*multi, 210))
    text_sf = base_font.render(str(circ).center(8), True, color2)
    win.blit(text_sf, (140, 220+rad*multi))
    text_sf = base_font.render(str(cont).center(8), True, color2)
    win.blit(text_sf, (160, 150+rad*multi))
    rad_rect = pygame.Rect(200, 208, rad*multi, 4)
    pygame.draw.rect(win, color2, rad_rect)
    pygame.draw.circle(win, color1, (200, 210), 5)
    pygame.display.update()
    add_history(rad)

def content():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)
    rad = get_text_input(200, 500, "(Radius)")
    cont = round((py*rad**2)*100000)/100000
    circ = round(rad*2*py*100000)/100000
    multi = 100/rad
    pygame.draw.circle(win, color1, (200, 210), rad*multi, 7)
    text_sf = base_font.render(str(rad).center(6), True, color2)
    win.blit(text_sf, (100+rad*multi, 210))
    text_sf = base_font.render(str(circ).center(8), True, color2)
    win.blit(text_sf, (140, 220+rad*multi))
    text_sf = base_font.render(str(cont).center(15), True, color2)
    win.blit(text_sf, (100, 150+rad*multi))
    rad_rect = pygame.Rect(200, 208, rad*multi, 4)
    pygame.draw.rect(win, color2, rad_rect)
    pygame.draw.circle(win, color1, (200, 210), 5)
    pygame.display.update()
    add_history(cont)


def kruh():
    akce = button(200, 530, ["Circum.", "Radius", "Content"], "Select action:")

    if akce == "Circum.":
        obvod()
    elif akce == "Radius":
        if button(200, 530, ["Circum.", "Content"], "From:") == "Circum.":
            rad_circ()
        else:
            rad_cont()
    elif akce == "Content":
        content()

def triangle():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)
    pygame.draw.polygon(win, color1, [[100, 250], [300, 250], [300, 150]], 5)
    text_sf = base_font.render("a", True, color2)
    win.blit(text_sf, (200, 265))
    text_sf = base_font.render("b", True, color2)
    win.blit(text_sf, (315, 185))
    text_sf = base_font.render("c", True, color2)
    win.blit(text_sf, (210, 135))
    rect = pygame.Rect(280, 230, 20, 20)
    pygame.draw.rect(win, color1, rect, 5)
    pygame.display.update()

    side1 = button(200, 530, ["a", "b", "c"], "Select side:")
    leng1 = get_text_input(200, 500, "(Length)")
    if side1 == "a":
        sideA = leng1
    elif side1  == "b":
        sideB = leng1
    else:
        sideC = leng1
    list = ["a", "b", "c"]
    list.remove(side1)
    side2 = button(200, 530, list, "Select side:")
    leng2 = get_text_input(200, 500, "(Length)")
    if side2 == "a":
        sideA = leng2
    elif side2  == "b":
        sideB = leng2
    else:
        sideC = leng2

    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)

    if (side1 == "c" and side2 == "a"):
        sideB = math.sqrt(leng1**2 - leng2**2)
    elif (side2 == "c" and side1 == "a"):
        sideB = math.sqrt(leng2**2 - leng1**2)

    if (side1 == "c" and side2 == "b"):
        sideA = math.sqrt(leng1**2 - leng2**2)
    elif (side2 == "c" and side1 == "b"):
        sideA = math.sqrt(leng2**2 - leng1**2)

    if (side1 == "a" and side2 == "b") or (side1 == "b" and side2 == "a"):
        sideC = math.sqrt(leng1**2 + leng2**2)

    if sideA >= sideB:
        multi = 100/sideA
    else:
        multi = 100/sideB
        

    pygame.draw.polygon(win, color1, [[140, 250], [140+sideA*multi, 250], [140+sideA*multi, 250-sideB*multi]], 5)
    text_sf = base_font.render(("a = "+str(sideA)).center(20), True, color2)
    win.blit(text_sf, (140+sideA*multi/2-90, 265))
    text_sf = base_font.render(("b = "+str(sideB)).center(20), True, color2)
    win.blit(text_sf, (140+sideA*multi+15-50, 250-sideB*multi/2))
    text_sf = base_font.render(("c = "+str(sideC)).center(20), True, color2)
    win.blit(text_sf, (100+sideA*multi/2-110, 210-sideB*multi/2))
    rect = pygame.Rect(140+sideA*multi-20, 230, 20, 20)
    pygame.draw.rect(win, color1, rect, 5)
    pygame.display.update()
    if (side1 == "a" and side2 == "b") or (side2 == "b" and side1 == "a"):
        sideF = sideC
    if (side1 == "c" and side2 == "b") or (side2 == "b" and side1 == "c"):
        sideF = sideA
    if (side1 == "a" and side2 == "c") or (side2 == "c" and side1 == "a"):
        sideF = sideB
    add_history(sideF)

def diagonal():
    rect = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(win, color3, rect)

    side1 = get_text_input(200, 500, "(Side 1:)")
    side2 = get_text_input(200, 500, "(Side 2:)")

    if side1 >= side2:
        multi = 100/side1
    else:
        multi = 100/side2

    rect = pygame.Rect(200-side1*multi/2, 100, side1*multi, side2*multi)
    pygame.draw.rect(win, color1, rect, 5)
    pygame.draw.line(win, color1, (203-side1*multi/2, 103), (197-side1*multi/2+side1*multi, 97+side2*multi), 5)
    text_sf = base_font.render(str(side1).center(20), True, color2)
    win.blit(text_sf, (60+side1*multi/2, 100+side2*multi))
    text_sf = base_font.render(str(math.sqrt(side1**2+side2**2)).center(22), True, color2)
    win.blit(text_sf, (20+side1*multi/2, 135+side2*multi))
    text_sf = base_font.render(str(side2).center(20), True, color2)
    win.blit(text_sf, (140-side1*multi/2+side1*multi, 90+side2*multi/2))

    pygame.display.update()
    add_history(math.sqrt(side1**2+side2**2))



def pythagorova_veta():
    akce = button(200, 530, ["Triangle", "Diagonal"], "Select action:")
    if akce == "Triangle":
        triangle()
    elif akce == "Diagonal":
        diagonal()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        akce = button(200, 530, ["Circle", "Pytha.", "History"], "Select theme:")
        if akce == "Circle":
            kruh()
        elif akce == "Pytha.":
            pythagorova_veta()
        else:
            if len(history) == 0:
                pass
            elif len(history) == 1:
                copy(history[0])
            else:
                copy(button(200, 530, list(reversed(history)), "History (Copy):"))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main()