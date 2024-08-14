import os

def generate_directory_structure(root_dir, indent_level=0):
    structure = ""
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            structure += " " * indent_level + f"- **{item}/**\n"
            structure += generate_directory_structure(item_path, indent_level + 2)
        else:
            structure += " " * indent_level + f"- {item}\n"
    return structure

def main():
    root_dir = os.getcwd()  
    structure = "# Directory Structure\n\n"
    structure += generate_directory_structure(root_dir)

    with open("structure.md", "w") as md_file:
        md_file.write(structure)

    print("Directory structure has been written to structure.md")

if __name__ == "__main__":
    main()
