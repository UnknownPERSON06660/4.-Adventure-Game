while True:
    playing = input("Welcome to Advanture Game. (Start/Quit)\n").lower()    
    if playing == 'quit':
        break
    elif playing == 'start':
        while True:
            decision_1 = input("It's 1 a.m. You're in the jungle, and your car has run out of fuel, causing it to turn off.\nDecide whether to (remain) in the car or (venture) outside in search of assistance.\n").lower()
            if decision_1 == 'remain':
                while True:
                    decision_2 = input("It's 3 a.m. and you hear the sounds of dangerous animals nearby. Would you rather (stay) in the car or go outside to (confront) the animals armed with your shotgun, which has 5 bullets?\n").lower()
                    if decision_2 == 'stay':
                        print("At 3:45 a.m., you encountered lethal animals that smashed your car window, leading to your demise.\nGame over.")
                        quit()
                    elif decision_2 == 'confront':
                        print("At 3:05 a.m., you succumbed to the overwhelming presence of numerous animals outside, unable to fend them off, ultimately resulting in your demise.\nGame over.")
                        quit()
                    else:
                        continue
            elif decision_1 == 'venture':
                while True:
                    decision_3 = input("You can either (proceed) towards your destination or (retreat) backward.\n").lower()
                    if decision_3 == 'proceed':
                        while True:
                            decision_4 = input("At 3 a.m., you reach the end of the road. You're faced with two narrow paths to your (left) and (right), or you can (return) to your car.\n").lower()
                            if decision_4 == 'left' or decision_4 == 'right':
                                while True:
                                    decision_5 = input("At 3:45 a.m., you arrive at a lake. You have the option to either (cross) the lake or (walk) towards its shores.\n").lower()
                                    if decision_5 == 'cross':
                                        print("You encountered a crocodile in the lake and unfortunately were eaten by it.\nGame over.")
                                        quit()
                                    elif decision_5 == 'walk':
                                        while True:
                                            decision_6 = input("At 7 a.m., feeling exhausted and thirsty, you have the choice to either (drink) water from the lake to replenish your energy or (continue) moving forward.\n").lower()
                                            if decision_6 == 'drink':
                                                print("The lake water being unhygienic, drinking it caused an infection. Despite efforts to stabilize yourself, the pain intensified over time, eventually causing loss of consciousness and marking the end of your journey.\nGame Over.")
                                                quit()
                                            elif decision_6 == 'continue':
                                                print("It's 9 a.m., and after hours of relentless travel, exhausted and weary, you finally reach a village where the kind people offer you refuge and safety.\nCongratulations, you have survived.")
                                                quit()
                                            else:
                                                continue
                                    else:
                                        continue
                            elif decision_4 == 'return':
                                while True:
                                    decision_7 = input("Upon reaching your car, you face the decision to either (sit) inside the car or (proceed) forward.\n").lower()
                                    while True:
                                        if decision_7 == 'sit':
                                            print("A snake was inside the car, and unfortunately, you were bitten by it, leading to your demise.\nGame Over")
                                            quit()
                                        elif decision_7 == 'proceed':
                                            while True:
                                                decision_8 = input("A deadly wolf is chasing you. (Hide) somewere or (run) for your life\n").lower()
                                                if decision_8 == 'hide' or decision_8 == 'run':
                                                    print("You were caught by the wolf, marking the end of your journey.\nGame over.")
                                                    quit()
                                                else:
                                                    continue
                                        else:
                                            continue
                    elif decision_3 == 'retreat':
                        while True:
                            decision_9 = input("A deadly wolf is chasing you. (Hide) somewere or (run) for your life\n").lower()
                            if decision_9 == 'hide' or decision_9 == 'run':
                                print("You were caught by the wolf, marking the end of your journey.\nGame over.")
                                quit()
                            else:
                                continue
                    else:
                        continue
            else:
                continue
    else:
        continue