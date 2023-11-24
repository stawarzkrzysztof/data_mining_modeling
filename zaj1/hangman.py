import os
import random

PASSWORS = ["jajko", "ul", "dom"]
TRIES = 20
game_count = 0
play_again = True

def clear():
    os.system('clear')

def genrate_password():
    return random.choice(PASSWORS)


def get_indexes(pas, let):
    return [i for i, x in enumerate(pas) if x == let]

def main():
    global game_count
    global play_again
    global TRIES

    clear()
    print("Witaj w grze Pajączek!")

    while play_again:

        game_count += 1

        current_password = genrate_password()
        blanks = ["_" for letter in current_password]
        tries = TRIES-len(current_password)

        print(f"Zaczynamy grę {game_count}")
        print(''.join(blanks))

        while "_" in blanks and tries != 0:

            print(f"Zgadnij litere (ilosc prob: {tries})")
            guessed_letter = input()

            try:
                #TODO: correct all the wrong types except 'char' len(1)
                int(guessed_letter)
                print("Miała być literka, jeszcze raz!!")
                continue
            except:
                pass

            if guessed_letter in current_password:
                print(f"Gratulacje, zgadłeś literke {guessed_letter}")
                guessed_indexes = get_indexes(current_password, guessed_letter)
                for index in guessed_indexes:
                    blanks[index] = guessed_letter

            print(''.join(blanks))
            tries-=1

        if "_" not in blanks:
            print("congrats, you won")
        elif tries == 0:
            print("przegrales nie masz prob")
        else:
            print("cos nie dziala XDDD")

        play_again = True if input("Wanna play again?") == "tak" else False
        if play_again:
            clear()

    print("ended")

if __name__ == "__main__":
    main()
    exit()