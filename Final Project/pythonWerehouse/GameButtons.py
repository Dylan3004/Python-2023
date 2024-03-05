import sys
import time

import Employer as emp
import ShiftOrders as so
import Shift as sh
import ShiftProgress as sp
import pygame
import pygame
import os
import random as rd




def StartDisplay(width, height,action=None):

    pygame.init()
    pygame.font.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    clock.tick(60)
    #zmienne do przycisku quit
    active_color_for_quit = (255, 0, 0)
    temp_inactive_color_for_quit = (41, 115, 184)
    inactive_color_for_quit = (41, 115, 184)

    #zmienne do przycisku start
    active_color_for_start = (10, 250, 10)
    tmp_inactive_color_for_start = (41, 115, 184)
    inactive_color_for_start = (41, 115, 184)

    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load(
        'background.jpg')  # Replace 'path/to/your/image.jpg' with your image path
    background_image = pygame.transform.scale(background_image,(width,height))  # Scale the image to fit the window

    pygame.display.set_caption('Wherehouse Simulator')
    clock = pygame.time.Clock()

    # Tworzenie przycisku Start
    button_font = pygame.font.Font(None, 60)
    button_text = button_font.render('Start', True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(width // 2, height// 2))

    # Tworzenie przycisku Quit
    button_font_quit = pygame.font.Font(None, 60)
    button_text_quit = button_font_quit.render('Quit', True, (0, 0, 0))
    button_rect_quit = button_text_quit.get_rect(center=(width // 2, height// 2 + 50))

    # Tworzenie napisu nazwy gry
    font = pygame.font.Font(None, 50)
    text_surface = font.render('Wherehouse Simulator', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(background_image, (0, 0))

    running = True
    while running:

        # Rysowanie przycisku Start
        pygame.draw.rect(screen, inactive_color_for_start , button_rect)
        # Rysowanie przycisku Quit
        pygame.draw.rect(screen, inactive_color_for_quit , button_rect_quit)
        # Rysowanie napisu nazwy gry
        screen.blit(text_surface, text_rect.topleft)
        screen.blit(button_text, button_rect.topleft)
        screen.blit(button_text_quit, button_rect_quit.topleft)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                # Sprawdzenie czy kursor myszy jest nad którymkolwiek z przycisków
                if button_rect.collidepoint(event.pos):
                    inactive_color_for_start = active_color_for_start
                    print(active_color_for_start)
                    print(inactive_color_for_start)
                else:
                    inactive_color_for_start = tmp_inactive_color_for_start
                    pass

                if button_rect_quit.collidepoint(event.pos):
                    inactive_color_for_quit = active_color_for_quit
                else:
                    inactive_color_for_quit = temp_inactive_color_for_quit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):

                    GameDifficulty(screen,width,height)
                    running = False
                if button_rect_quit.collidepoint(event.pos):
                    #Zamknięcie okna
                    running = False
        pygame.display.flip()


    pygame.quit()
    sys.exit()

def GameDifficulty(screen,width,height):
    background_image_diff = pygame.image.load(
        'bacgrounddiff.jpg')
    background_image = pygame.transform.scale(background_image_diff, (width, height))
    screen.blit(background_image_diff, (0, 0))


    #zmienne do przycisku easy
    active_color_for_easy = (10, 250, 10)
    tmp_inactive_color_for_easy = (41, 115, 184)
    inactive_color_for_easy = (41, 115, 184)

    #zmienne do przycisku medium
    active_color_for_medium = (255, 255, 0)
    tmp_inactive_color_for_medium = (41, 115, 184)
    inactive_color_for_medium = (41, 115, 184)

    #zmienne do przycisku hard
    active_color_for_hard = (255, 0, 0)
    tmp_inactive_color_for_hard = (41, 115, 184)
    inactive_color_for_hard = (41, 115, 184)

    # Tworzenie przycisku easy
    button_font_easy = pygame.font.Font(None, 60)
    button_text_easy = button_font_easy.render('Easy', True, (0, 0, 0))
    button_rect_easy = button_text_easy.get_rect(center=(width // 2, height// 2 - 100))

    # Tworzenie przycisku medium

    button_font_medium = pygame.font.Font(None, 60)
    button_text_medium = button_font_medium.render('Medium', True, (0, 0, 0))
    button_rect_medium = button_text_medium.get_rect(center=(width // 2, height// 2))

    # Tworzenie przycisku hard

    button_font_hard = pygame.font.Font(None, 60)
    button_text_hard = button_font_hard.render('Hard', True, (0, 0, 0))
    button_rect_hard = button_text_hard.get_rect(center=(width // 2, height// 2 + 100))

    # Tworzenie napisu nazwy gry
    font = pygame.font.Font(None, 50)
    text_surface = font.render('Wherehouse Simulator', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2 + 200))
    screen.blit(background_image, (0, 0))

    running = True
    while running:

            # Rysowanie przycisku easy
            pygame.draw.rect(screen, inactive_color_for_easy , button_rect_easy)
            # Rysowanie przycisku medium
            pygame.draw.rect(screen, inactive_color_for_medium , button_rect_medium)
            # Rysowanie przycisku hard
            pygame.draw.rect(screen, inactive_color_for_hard , button_rect_hard)
            # Rysowanie napisu nazwy gry
            screen.blit(text_surface, text_rect.topleft)
            screen.blit(button_text_easy, button_rect_easy.topleft)
            screen.blit(button_text_medium, button_rect_medium.topleft)
            screen.blit(button_text_hard, button_rect_hard.topleft)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    # Sprawdzenie czy kursor myszy jest nad którymkolwiek z przycisków
                    if button_rect_easy.collidepoint(event.pos):
                        inactive_color_for_easy = active_color_for_easy

                    else:
                        inactive_color_for_easy = tmp_inactive_color_for_easy
                        pass

                    if button_rect_medium.collidepoint(event.pos):
                        inactive_color_for_medium = active_color_for_medium
                    else:
                        inactive_color_for_medium = tmp_inactive_color_for_medium

                    if button_rect_hard.collidepoint(event.pos):
                        inactive_color_for_hard = active_color_for_hard
                    else:
                        inactive_color_for_hard = tmp_inactive_color_for_hard

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect_easy.collidepoint(event.pos):

                        GameDisplay(screen,width,height,12,45)
                        running = False

                    if button_rect_medium.collidepoint(event.pos):

                        GameDisplay(screen,width,height,10,40)
                        running = False

                    if button_rect_hard.collidepoint(event.pos):

                        GameDisplay(screen,width,height,8,30)
                        running = False
            pygame.display.flip()




def GameDisplay(screen,width,height,employersAmount,timeforgame):
    global end_game
    background_image = pygame.image.load(
        'bacgroundgame.jpg')
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))
    game_time = time.time()
    loading_progresses = [{"progress": 0, "visible": True} for _ in range(4)]  # Przykładowa lista czterech pasków postępu

    ClassTable = []
    for i in range(len(loading_progresses)):
        Order = so.ShiftOrders(1)
        Ordertable = Order.Random_Generator()
        ShiftProgress1 = sp.ShiftProgress(Ordertable, [])
        ClassTable.append({"Ordertable":Ordertable,"ShiftProgress":ShiftProgress1,"EmployersArray":[]})

    printEmployers(screen,employersAmount,0,width,height)


    print("Loading process",loading_progresses)
    print("ClassTable",ClassTable)
    temp = 0
    previous_time = time.time()
    running = True
    game_ended = 0
    end_game = False

    while running:

        padding=0
        for progress_bar, class_item in zip(loading_progresses, ClassTable):

            if progress_bar["progress"] >= 100:
                print("koniec")
                progress_bar["visible"] = False
                game_ended += 1
                if game_ended == 4:
                    end_game = True
                    running = False
            else:
               pass
            temp_prev = temp
            if progress_bar["visible"]:
                temp = LoadingBar(screen, width, height - padding, progress_bar["progress"], class_item["EmployersArray"],employersAmount,temp)
                if temp_prev != temp:
                    screen.blit(background_image, (0, 0))
                    printEmployers(screen,employersAmount,temp,width,height)
                class_item["ShiftProgress"]= sp.ShiftProgress(class_item["Ordertable"], class_item["EmployersArray"])
                progress_bar["progress"] += class_item["ShiftProgress"].ProgressProgress()


                if progress_bar["progress"] > 10 and time.time()-previous_time>1:
                    screen.blit(background_image, (0, 0))
                    printEmployers(screen,employersAmount,temp,width,height)
                    printTime(screen,timeforgame-(time.time()-game_time),width,height)
                    printItem(screen,class_item["Ordertable"][rd.randint(1,30)],width,height)
                    previous_time = time.time()


                if time.time()-previous_time>1:
                    screen.blit(background_image, (0, 0))
                    printTime(screen, timeforgame - (time.time() - game_time), width, height)
                    printEmployers(screen,employersAmount,temp,width,height)
                    previous_time = time.time()
                pygame.display.flip()
            print(game_ended)
            padding += 100
            if game_ended == 4:
                print("bbbbb")
                running = False
        print("aaaaa")

        game_ended = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if time.time()-game_time>timeforgame:
            running = False
    if end_game:
        printScore(screen, timeforgame - (time.time() - game_time), width, height)
        pygame.display.flip()

        # Czekaj 5 sekund przed zamknięciem okna
        start_time = time.time()
        while time.time() - start_time < 5:
            pass  # Wyświetl wyniki przez 5 sekund
    else:
        printLoose(screen,width,height)
        pygame.display.flip()

        # Czekaj 5 sekund przed zamknięciem okna
        start_time = time.time()
        while time.time() - start_time < 5:
            pass
    pygame.mixer.music.stop()
    pygame.quit()



def LoadingBar(screen,width, height,loading_progress=0,EmployersArray=[],employersAmount=0,currentEmployersAmount=0):
    loading = 0
    max_loading = 100
    bar_width = 400
    bar_height = 30
    progress_width = (loading_progress / max_loading) * bar_width
    bar_x = (width - bar_width) // 2
    bar_y = (height - bar_height) // 2
    pygame.draw.rect(screen, (0,0,0), (bar_x, bar_y, bar_width, bar_height), 2)
    pygame.draw.rect(screen, (255,0,0), (bar_x, bar_y, progress_width, bar_height))
    return plusminusButtons(screen,width,height,EmployersArray,employersAmount,currentEmployersAmount)



def plusminusButtons(screen,width,height,EmployersArray,employersAmount=0,currentEmployersAmount=0):
    button_font_plus = pygame.font.Font(None, 30)
    button_text_plus = button_font_plus.render('+', True, (0, 0, 0))
    button_rect_plus = button_text_plus.get_rect(center=(width - (width * 0.8), height // 2))
    button_rect_plus.inflate_ip(20, 20)

    button_font_minus = pygame.font.Font(None, 30)
    button_text_minus = button_font_minus.render('-', True, (0, 0, 0))
    button_rect_minus = button_text_minus.get_rect(center=(width - (width * 0.2), height // 2))
    button_rect_minus.inflate_ip(20, 20)

    button_surface_plus = pygame.Surface(button_rect_plus.size, pygame.SRCALPHA)
    pygame.draw.ellipse(button_surface_plus, (41, 115, 184), button_surface_plus.get_rect())
    screen.blit(button_surface_plus, button_rect_plus)
    screen.blit(button_text_plus, button_text_plus.get_rect(center=button_rect_plus.center))

    button_surface_minus = pygame.Surface(button_rect_minus.size, pygame.SRCALPHA)
    pygame.draw.ellipse(button_surface_minus, (41, 115, 184), button_surface_minus.get_rect())
    screen.blit(button_surface_minus, button_rect_minus)
    screen.blit(button_text_minus, button_text_minus.get_rect(center=button_rect_minus.center))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_plus.collidepoint(event.pos):
                if employersAmount-1 >= currentEmployersAmount:
                    EmployersArray.append(emp.Employer("Stawski", "Adam", "Employee", False))
                    currentEmployersAmount += 1
                    print("Nowy pracownik")
                else:
                    font = pygame.font.Font(None, 50)
                    item = "Nie ma już więcej pracowników"
                    text_surface = font.render(str(item), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=(width // 2, height * 0.15))
                    screen.blit(text_surface, text_rect)
            if button_rect_minus.collidepoint(event.pos):
                if currentEmployersAmount > 0:
                    EmployersArray.pop()
                    currentEmployersAmount -= 1
                    print("Usunięto pracownika")
                else:
                    font = pygame.font.Font(None, 50)
                    item = "Nie dodani żadnego pracownika"
                    text_surface = font.render(str(item), True, (255, 0, 0))
                    text_rect = text_surface.get_rect(center=(width // 2, height * 0.15))
                    screen.blit(text_surface, text_rect)
    return currentEmployersAmount


def printItem(screen,item,width,height):
    font = pygame.font.Font(None, 30)
    item = " You picked up: " + item[0] + " " + item[1]
    text_surface = font.render(str(item), True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(rd.randint(0,width), rd.randint(0,height)))
    screen.blit(text_surface,text_rect)


def printEmployers(screen,employersAmount=0,currentEmployersAmount=0,width=0,height=0):
    font = pygame.font.Font(None, 30)
    item = "Amount of workers :" + str(currentEmployersAmount) + "/" + str(employersAmount)
    text_surface = font.render(str(item), True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width * 0.8, height * 0.8))
    screen.blit(text_surface,text_rect)


def printTime(screen,time,width,height):
    font = pygame.font.Font(None, 30)
    item = "Time left: " + str(int(time)) + " seconds"
    text_surface = font.render(str(item), True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(width * 0.2, height * 0.8))
    screen.blit(text_surface,text_rect)

def printScore(screen,score,width,height):
    font = pygame.font.Font(None, 60)
    item = "You won "+" Score: " + str(int(score))
    text_surface = font.render(str(item), True, (0, 255, 0))
    text_rect = text_surface.get_rect(center=(width //2, height //2))
    screen.blit(text_surface,text_rect)

def printLoose(screen,width,height):
    font = pygame.font.Font(None, 60)
    item = "You lost"
    text_surface = font.render(str(item), True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width //2, height //2))
    screen.blit(text_surface,text_rect)



