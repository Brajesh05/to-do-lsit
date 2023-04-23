import os


def make_list():
    list_name = input("Enter list name: ")
    print("Enter items: ")
    # items = True
    lst = []
    while True:
        x = input()
        if x == "":
            break
        lst.append(x)

    with open(f"saved/{list_name}.txt", "a") as f:
        for x in lst:
            f.write(f"{x}\n")

    print("Your list has been created successfully!")
    return


def read_list(list_name):
    try:
        with open(f"saved/{list_name}.txt", "r") as f:
            page = f.read()
            lines = page.split("\n")
            lines.pop(len(lines) - 1)
            for i, x in enumerate(lines):
                print(f"{i + 1}. {x}")
    except FileNotFoundError:
        print(f"There is no to-do list with name {list_name}")

    return


def show_list():
    all_list = os.listdir(path="saved/")
    if len(all_list) == 0:
        print("No to-do list\n")
    else:
        print("All to-do lists are: ")
        for x in all_list:
            print(f"- {x[:-4]}")
        print("\n")
        return


def main():
    while True:
        choice = input(
            "Do you want to\nread an already existing to-do list [R]\ncreate a new to-do list [C]\nexit the program [E]\nshow all to-do lists [S]: \n"
        )
        if choice.lower() == "r":
            read_list(list_name=input("Enter list name you want to read: "))
        elif choice.lower() == "c":
            make_list()
        elif choice.lower() == "s":
            show_list()
        elif choice.lower() == "e":
            break
        else:
            print("Choose a correct option")
    return


main()
