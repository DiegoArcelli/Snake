import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    is_playing = True
    while is_playing:
        try:
            clear()
            print("Select option:")
            print("1) Play\n2) Quit\n3) Rules")
            ch = input()
            if int(ch) == 1:
                os.system('python Game.py')
            elif int(ch) == 2:
                is_playing = False
            elif int(ch) == 3:
                rules = open("rules", "r")
                print(rules.read())
                input("Press the enter button to proceed\n")
                rules.close()
        except ValueError:
            pass
    return 1


if __name__ == "__main__":
    exit(main())
