from note_manager import add_note, draw_random_note
from sync import git_pull, git_push
from config import MY_NAME

def main():
    print("1. Add note")
    print("2. Draw note")
    choice = input("> ")

    git_pull()

    if choice == "1":
        msg = input("Write your message: ")
        recipient = "alice" if MY_NAME == "bob" else "bob"
        add_note(MY_NAME, recipient, msg)
        git_push()
    elif choice == "2":
        draw_random_note()
        git_push()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()