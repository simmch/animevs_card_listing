def categorize_characters(data):
    categories = {
        "Destiny": [],
        "Scenario": [],
        "Tales": [],
        "Dungeon": [],
        "Unlisted": [],
        "Boss": [],
    }

    for line in data:
        character, category = line.strip().split(" - ")
        if category in categories:
            categories[category].append(character)
        else:
            categories["Unlisted"].append(character)

    return categories

def main():
    folder_name = input("Enter the name of the folder: ")

    try:
        with open(f"{folder_name}/list.txt", "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("list.txt file not found in the specified folder.")
        return

    categorized_data = categorize_characters(data)

    with open(f"{folder_name}/list.txt", "w") as file:
        for category, characters in categorized_data.items():
            if characters:
                file.write(f"\n-- {category} List\n")
                for character in characters:
                    file.write(f"{character}\n")

if __name__ == "__main__":
    main()