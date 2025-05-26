import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def copy_static(src, dest):
    """
    Recursively copy files and directories from src to dest.
    """
    # Remove the destination directory if it exists
    if os.path.exists(dest):
        print(f"Deleting existing directory: {dest}")
        shutil.rmtree(dest)

    # Create the destination directory
    print(f"Creating directory: {dest}")
    os.makedirs(dest)

    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Calculate relative path from src to current directory
        relative_path = os.path.relpath(root, src)
        dest_dir = os.path.join(dest, relative_path)

        # Create corresponding directory in destination
        if not os.path.exists(dest_dir):
            print(f"Creating subdirectory: {dest_dir}")
            os.makedirs(dest_dir)

        # Copy each file
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            print(f"Copying file: {src_file} -> {dest_file}")
            shutil.copy(src_file, dest_file)

def main():
    print("Starting site generation...")

    # Clean public directory
    if os.path.exists("public"):
        print("Removing existing public directory...")
        shutil.rmtree("public")

    # Copy static files
    print("Copying static files...")
    copy_static("static", "public")

    # Generate all pages
    print("Generating all content pages recursively...")
    generate_pages_recursive("content", "template.html", "public")
    print("All pages generated.")



if __name__ == "__main__":
    main()


