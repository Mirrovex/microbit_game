from microbit import*
import random

lista = {}

while True:
    zycia = 2
    ballx = random.randint(0,4)
    bally = 0
    ballx2 = random.randint(0,4)
    bally2 = 0
    graczx = 2
    graczy = 4
    lvl = 0
    trudnosc = 0
    predkosc = 700

    print('Musisz klikac przyciski "a" i "b" zeby ruszac postacia i lapac pilki (1 pilka to 1pkt)')
    odp = input('Wpisz poziom: "1", "2", "3", "4"')
    if odp == '1':
        trudnosc = 1
        nick = input('Wpisz swoj nick:')
    elif odp == '2':
        trudnosc = 15
        nick = input('Wpisz swoj nick:')
    elif odp == '3':
        trudnosc = 30
        nick = input('Wpisz swoj nick:')
    elif odp == '4':
        trudnosc = 45
        nick = input('Wpisz swoj nick:')
    elif odp == 'cheat':
        while True:
            nick = input('Wpisz swoj nick (Wpisz "stop" jesli to wszyscy):')
            lvl = input('Wpisz ile chcesz pkt (Wpisz "stop" jesli to wszyscy): ')
            if (lvl == 'stop' or nick == 'stop'):
                break
            if(not lvl.isdigit()):
                while True:
                    lvl = input('Wpisz ile chcesz pkt (liczba): ')
                    if (lvl.isdigit()):
                        break
            lista[nick] = lvl
        dalej = input('Czy chcesz zagrac normalnie? (Wpisz "tak" lub "nie"')
        if dalej == 'tak':
            trudnosc = 0
            odp = '1'
        else:
            break
    elif odp != '1' or odp != '2' or odp != '3' or odp != '4':
        while True:
            if odp == '1' or odp == '2' or odp == '3' or odp == '4':
                break
            odp = input('Nie ma takiego poziomu wpisz ponownie ("1", "2", "3", "4")')
    if trudnosc > 0:
        print('Powodzenia :)')
        sleep(4000)
        while True:
            display.clear()
            if zycia <= 0:
                break
            if trudnosc >= 15 and trudnosc < 30:
                predkosc = predkosc - 30
            if trudnosc == 1:
                zycia = zycia + 1
                print("Masz", zycia, "zycia")
                sleep(3000)
            if trudnosc == 15:
                graczx = 2
                zycia = zycia + 1
                print("Teraz predkosc spadania bedzie rosla z kazdym punktem, masz", zycia, "zycia")
                sleep(6000)
            if trudnosc == 30:
                graczx = 2
                zycia = zycia + 1
                print("Teraz spadaja 2 pilki - ciemna i jasna. Lap tylko JASNA!!!, masz", zycia, "zycia")
                sleep(6000)
            if trudnosc == 45:
                graczx = 2
                zycia = zycia + 1
                print("Teraz tylko raz pokaze sie pilka (na samej gorze) a pozniej zniknie, masz", zycia, "zycia")
                sleep(6000)
            display.set_pixel(graczx, graczy, 8)
            display.set_pixel(ballx, bally, 6)
            if ballx2 == ballx:
                while True:
                    if ballx2 != ballx:
                        break
                    ballx2 = random.randint(0,4)
     
            if trudnosc < 45:
                while True:
                    if ballx == graczx and bally == 4:
                        lvl = lvl + 1
                        trudnosc = trudnosc + 1
                        display.clear()
                        display.set_pixel(graczx, graczy, 8)
                        sleep(1000)
                        break
                    elif bally == 4 and ballx != graczx:
                        zycia = zycia - 1
                        trudnosc = trudnosc + 1
                        print("zostaly ci zycia: ", zycia)
                        print('lvl: ', lvl)
                        graczx = 2
                        display.clear()
                        sleep(3000)
                        break
                    elif button_a.get_presses():
                        graczx = graczx - 1
                        if graczx < 0:
                            graczx = 4
                        display.clear()
                        display.set_pixel(graczx, graczy, 8)
                        display.set_pixel(ballx, bally, 6)
                        if trudnosc >= 30 and trudnosc < 45:
                            display.set_pixel(ballx2, bally2, 4)
                    elif button_b.get_presses():
                        graczx = graczx + 1
                        if graczx > 4:
                            graczx = 0
                        display.clear()
                        display.set_pixel(graczx, graczy, 8)
                        display.set_pixel(ballx, bally, 6)
                        if trudnosc >= 30 and trudnosc < 45:
                            display.set_pixel(ballx2, bally2, 4)
                    elif trudnosc >= 30 and trudnosc < 45:
                        predkosc = 700
                        display.set_pixel(ballx2, bally2, 4)
                    sleep(predkosc)
                    bally = bally + 1
                    bally2 = bally2 + 1
                    display.clear()
                    display.set_pixel(graczx, graczy, 8)
                    display.set_pixel(ballx, bally, 6)
                    if trudnosc >= 30 and trudnosc < 45:
                        display.set_pixel(ballx2, bally2, 4)
                bally2 = 0
                ballx2 = random.randint(0,4)
                bally = 0
                ballx = random.randint(0,4)

            elif trudnosc >= 45:
                while True:
                    if ballx == graczx and bally == 4:
                        lvl = lvl + 1
                        trudnosc = trudnosc + 1
                        sleep(1000)
                        break
                    elif bally == 4 and ballx != graczx:
                        zycia = zycia - 1
                        trudnosc = trudnosc + 1
                        print("zostaly ci zycia: ", zycia)
                        print('lvl: ', lvl)
                        graczx = 2
                        display.clear()
                        for x in range(4):
                            display.set_pixel(ballx, 3, 9)
                            sleep(500)
                            display.clear()
                            sleep(500)
                        break
                    elif button_a.get_presses():
                        graczx = graczx - 1
                        trudnosc = trudnosc + 1
                        if graczx < 0:
                            graczx = 4
                        display.clear()
                        display.set_pixel(graczx, graczy, 8)
                    elif button_b.get_presses():
                        graczx = graczx + 1
                        if graczx > 4:
                            graczx = 0
                        display.clear()
                        display.set_pixel(graczx, graczy, 8)
                    sleep(predkosc)
                    display.clear()
                    display.set_pixel(graczx, graczy, 8)
                    bally = bally + 1
                bally = 0
                ballx = random.randint(0,4)
                if trudnosc == 60:
                    trudnosc = 15
        lista[nick] = lvl
        display.clear()
        display.show(Image.HAPPY)
        print('Koniec gry. Uzyskales punktow: ', lvl)
        odp = input('Czy ty lub inna osoba chce zagrac? (Wpisz "tak" lub "nie")')
        if odp == 'nie':
            break
print(' ')
print('Ranking:')
nr = 0
gracze = [(nick, lista[nick]) for nick in sorted(lista, key=lista.get, reverse = True)]
for nick, lvl in gracze:
    nr =+ 1
    ranking = str(nr) + '. ' + nick + ' ' + str(lvl) + 'pkt'
    print(ranking)
