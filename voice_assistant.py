# voice_assistant.py

reminders = []

def speak(message):
    print(f"Speaking: {message}")

def add_reminder():
    speak("What should I remind you about?")
    reminder = input("Enter your reminder: ")
    reminders.append(reminder)
    speak("Reminder added successfully!")

def view_reminders():
    if not reminders:
        speak("You have no reminders.")
    else:
        speak("Here are your reminders:")
        for i, rem in enumerate(reminders, start=1):
            print(f"{i}. {rem}")

def greet_user():
    speak("Hello! What's your name?")
    name = input("Enter your name: ")
    speak(f"Nice to meet you, {name}!")

def show_help():
    speak("Here is what I can do:")
    print("""
1. Greet you and ask your name
2. Add a reminder
3. View your reminders
4. Exit the program
5. Show help menu
""")

def main():
    speak("Welcome to your Android Voice Assistant.")
    while True:
        print("\nWhat would you like me to do?")
        print("1. Greet me")
        print("2. Add a reminder")
        print("3. View reminders")
        print("4. Exit")
        print("5. Help")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            greet_user()
        elif choice == "2":
            add_reminder()
        elif choice == "3":
            view_reminders()
        elif choice == "4":
            speak("Goodbye!")
            break
        elif choice == "5":
            show_help()
        else:
            speak("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
