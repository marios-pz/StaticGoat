import os


def extract_title(markdown: str):
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No H1 header found in markdown")


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    # 4. Extract the title
    title = extract_title(markdown_content)

    # 5. Replace placeholders
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    # 6. Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # 7. Write the HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Page successfully written to {dest_path}")
