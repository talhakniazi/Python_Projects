import nbformat
from nbconvert import HTMLExporter
import os
import json
from nbformat.reader import NotJSONError

def extract_code_from_ipynb(ipynb_path, output_py_path):
    """Extract code cells from a Jupyter Notebook and save as a .py file."""
    try:
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        code_cells = [cell['source'] for cell in notebook.cells if cell.cell_type == 'code']
        with open(output_py_path, 'w', encoding='utf-8') as f:
            for cell in code_cells:
                f.write(cell + '\n\n')  # Add spacing between cells

        print(f"Code extracted to {output_py_path}")

    except (json.JSONDecodeError, NotJSONError):
        print(f"Skipped non-JSON or corrupted file: {ipynb_path}")

def convert_ipynb_to_html(ipynb_path, output_html_path):
    """Convert a Jupyter Notebook to an HTML file."""
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic'  # Optional: Set template

    try:
        with open(ipynb_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        (body, resources) = html_exporter.from_notebook_node(notebook)
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(body)

        print(f"Notebook converted to HTML: {output_html_path}")

    except (json.JSONDecodeError, NotJSONError):
        print(f"Skipped non-JSON or corrupted file: {ipynb_path}")

def convert_all_ipynb_in_folder(main_folder_path):
    """Convert all .ipynb files in a folder and its subfolders to .py and .html formats."""
    # Recursively search for .ipynb files
    for root, dirs, files in os.walk(main_folder_path):
        # Check if the folder contains any .ipynb files
        ipynb_files = [f for f in files if f.endswith('.ipynb')]
        if ipynb_files:
            # Create local py and html folders inside the current subfolder
            py_folder = os.path.join(root, "py")
            html_folder = os.path.join(root, "html")
            os.makedirs(py_folder, exist_ok=True)
            os.makedirs(html_folder, exist_ok=True)

            for filename in ipynb_files:
                ipynb_path = os.path.join(root, filename)
                
                # Prepare output paths in the local output folders
                base_name = os.path.splitext(filename)[0]
                output_py_path = os.path.join(py_folder, f"{base_name}.py")
                output_html_path = os.path.join(html_folder, f"{base_name}.html")
                
                # Convert to .py and .html
                extract_code_from_ipynb(ipynb_path, output_py_path)
                convert_ipynb_to_html(ipynb_path, output_html_path)

def main():
    folder_path = input("Enter the path of the main folder containing .ipynb files: ")
    convert_all_ipynb_in_folder(folder_path)
    print("All .ipynb files have been converted to .py and .html formats in 'py' and 'html' folders within each subfolder.")

if __name__ == "__main__":
    main()
