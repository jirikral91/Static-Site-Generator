import os
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} with base_path '{base_path}'")

    # Read markdown file
    with open(from_path, 'r') as f:
        markdown = f.read()

    # Read template file
    with open(template_path, 'r') as f:
        template = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown)

    # Replace placeholders and fix base paths
    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    page_content = page_content.replace('href="/', f'href="{base_path}')
    page_content = page_content.replace('src="/', f'src="{base_path}')

    # Create destination directory if needed
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the generated HTML
    with open(dest_path, 'w') as f:
        f.write(page_content)

    print(f"Page generated: {dest_path}")

