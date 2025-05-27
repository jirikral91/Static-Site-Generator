import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys



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

    # Get base path from command-line argument or default to "/"
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Use "docs" instead of "public" for GitHub Pages
    output_dir = "docs"

    # Clean output directory
    if os.path.exists(output_dir):
        print(f"Removing existing {output_dir} directory...")
        shutil.rmtree(output_dir)

    # Copy static files
    print("Copying static files...")
    copy_static("static", output_dir)

    # Generate all pages recursively
    print("Generating all content pages recursively...")
    generate_pages_recursive("content", "template.html", output_dir, base_path)
    print("All pages generated.")



if __name__ == "__main__":
    main()


