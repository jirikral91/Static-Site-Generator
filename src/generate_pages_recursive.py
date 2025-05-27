import os
from generate_page import generate_page

def generate_pages_recursive(content_dir, template_path, dest_dir, base_path="/"):
    for entry in os.listdir(content_dir):
        full_path = os.path.join(content_dir, entry)
        dest_path = os.path.join(dest_dir, entry)

        if os.path.isfile(full_path) and full_path.endswith(".md"):
            dest_html = os.path.splitext(dest_path)[0] + ".html"
            generate_page(full_path, template_path, dest_html, base_path)

        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, dest_path, base_path)
