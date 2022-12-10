import time
import score
import screen_content

# main game
get = score.Score('User_data.json')
get_choice = ''
print('===========================================================')
while get_choice != '1':
    print('             |Welcome to Mos jul the runner|')
    print("1) start")
    print("2) How to play")
    print("3) Score board")
    print("4) Quit")
    print('===========================================================')
    get_choice = str(input('please select you choice |1-4| = '))
    if get_choice == "2":
        print('===================== how to play =====================\n'
              'this is an parkour game that you need to run \n'
              'and jump over the obstruction.\n'
              'Press |W| to jump\n'
              'Press |A| to move left\n'
              'Press |D| to move right\n'
              'Press |S| to stop moving\n'
              'Press |Q| to Quit the game\n'
              'for now have only 2 stage and have fun |(-u-)|')
        print('===========================================================')
        time.sleep(2)

    if get_choice == "3":
        get.score_display()
        print('===========================================================')
        time.sleep(2)
    if get_choice == "4":
        print("see you next time (OUO)/")
        break

    if get_choice not in ["1", "2", '3', "4"]:
        print('===========================================================')
        print('Input must be 1-4 please type again')
        print('===========================================================')
        time.sleep(1)

if get_choice == "1":
    print('===========================================================')
    name = input('Please put you name: ')
    # create Screen
    screen = screen_content.Screen_display(name, 600, 900, 'underground.png',
                                           'mos jul the runner')
    # run game
    screen.create_screen()
    get.score_display()
    print('===========================================================')
