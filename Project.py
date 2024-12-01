import json
import random
import os

# File to save flashcards
DATA_FILE = "flashcards.json"

# Load flashcards from the file
def load_flashcards():
    """Loads the flashcards from the file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save flashcards to the file
def save_flashcards(flashcards):
    """Saves all flashcards to the file."""
    with open(DATA_FILE, "w") as file:
        json.dump(flashcards, file, indent=4)

# Show all flashcards
def show_flashcards(flashcards):
    """Displays all the flashcards."""
    if not flashcards:
        print("Oops, no flashcards found!")
        return
    print("\nHere are your flashcards:")
    for i, card in enumerate(flashcards):
        print(f"{i + 1}. Word: {card['word']}, Translation: {card['translation']}")

# Add a new flashcard
def add_flashcard(flashcards):
    """Adds a new flashcard to the collection."""
    word = input("Enter the word: ").strip()
    translation = input("Enter the translation: ").strip()
    flashcards.append({"word": word, "translation": translation})
    save_flashcards(flashcards)
    print("Flashcard added! Keep learning :)")

# Remove a flashcard
def remove_flashcard(flashcards):
    """Deletes a flashcard by its index."""
    show_flashcards(flashcards)
    try:
        idx = int(input("Enter the number of the flashcard to remove: ")) - 1
        if 0 <= idx < len(flashcards):
            removed = flashcards.pop(idx)
            save_flashcards(flashcards)
            print(f"Deleted: {removed['word']}")
        else:
            print("That number isn't valid.")
    except ValueError:
        print("Please enter a valid number!")

# Quiz yourself
def quiz(flashcards):
    """Tests your knowledge of the flashcards."""
    if not flashcards:
        print("No flashcards to quiz yourself. Add some first!")
        return

    print("\nQuiz time! Let's see how you do :)")
    random.shuffle(flashcards)
    score = 0

    for card in flashcards:
        answer = input(f"What's the translation of '{card['word']}'? ").strip()
        if answer.lower() == card['translation'].lower():
            print("Yay, that's correct!")
            score += 1
        else:
            print(f"Oops, the right answer is: {card['translation']}")
    print(f"\nYou scored {score}/{len(flashcards)}. Keep practicing!")

# Main app
def main():
    flashcards = load_flashcards()
    while True:
        print("\n--- Flashcard App ---")
        print("1. View flashcards")
        print("2. Add a flashcard")
        print("3. Remove a flashcard")
        print("4. Quiz myself")
        print("5. Exit")

        choice = input("What do you want to do? ").strip()
        if choice == "1":
            show_flashcards(flashcards)
        elif choice == "2":
            add_flashcard(flashcards)
        elif choice == "3":
            remove_flashcard(flashcards)
        elif choice == "4":
            quiz(flashcards)
        elif choice == "5":
            print("Goodbye and happy learning!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
