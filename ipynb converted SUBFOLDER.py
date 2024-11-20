import nbformat
from nbconvert import PDFExporter
import os

def extract_code_from_ipynb(ipynb_path, output_py_path):
    """Extract code cells from a Jupyter Notebook and save as a .py file."""
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    code_cells = [cell['source'] for cell in notebook.cells if cell.cell_type == 'code']
    with open(output_py_path, 'w', encoding='utf-8') as f:
        for cell in code_cells:
            f.write(cell + '\n\n')  # Add spacing between cells

    print(f"Code extracted to {output_py_path}")

def convert_ipynb_to_pdf(ipynb_path, output_pdf_path):
    """Convert a Jupyter Notebook to a PDF file."""
    pdf_exporter = PDFExporter()
    pdf_exporter.template_name = 'classic'  # Optional: Set template

    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    (body, resources) = pdf_exporter.from_notebook_node(notebook)
    with open(output_pdf_path, 'wb') as f:
        f.write(body)
        
    print(f"Notebook converted to PDF: {output_pdf_path}")

def convert_all_ipynb_in_folder(main_folder_path):
    """Convert all .ipynb files in a folder and its subfolders to .py and .pdf formats."""
    # Recursively search for .ipynb files
    for root, dirs, files in os.walk(main_folder_path):
        # Check if the folder contains any .ipynb files
        ipynb_files = [f for f in files if f.endswith('.ipynb')]
        if ipynb_files:
            # Create local py and pdf folders inside the current subfolder
            py_folder = os.path.join(root, "py")
            pdf_folder = os.path.join(root, "pdf")
            os.makedirs(py_folder, exist_ok=True)
            os.makedirs(pdf_folder, exist_ok=True)

            for filename in ipynb_files:
                ipynb_path = os.path.join(root, filename)
                
                # Prepare output paths in the local output folders
                base_name = os.path.splitext(filename)[0]
                output_py_path = os.path.join(py_folder, f"{base_name}.py")
                output_pdf_path = os.path.join(pdf_folder, f"{base_name}.pdf")
                
                # Convert to .py and .pdf
                extract_code_from_ipynb(ipynb_path, output_py_path)
                convert_ipynb_to_pdf(ipynb_path, output_pdf_path)

def main():
    folder_path = input("Enter the path of the main folder containing .ipynb files: ")
    convert_all_ipynb_in_folder(folder_path)
    print("All .ipynb files have been converted to .py and .pdf formats in 'py' and 'pdf' folders within each subfolder.")

if __name__ == "__main__":
    main()
