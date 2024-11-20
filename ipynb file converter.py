import nbformat
from nbconvert import PDFExporter
import sys
import os

def extract_code_from_ipynb(ipynb_path, output_py_path):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    code_cells = [cell['source'] for cell in notebook.cells if cell.cell_type == 'code']
    with open(output_py_path, 'w', encoding='utf-8') as f:
        for cell in code_cells:
            f.write(cell + '\n\n')  # Add some spacing between cells

    print(f"Code extracted to {output_py_path}")

def convert_ipynb_to_pdf(ipynb_path, output_pdf_path):
    pdf_exporter = PDFExporter()
    pdf_exporter.template_name = 'classic'  # Optional: Set template

    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    (body, resources) = pdf_exporter.from_notebook_node(notebook)
    with open(output_pdf_path, 'wb') as f:
        f.write(body)
        
    print(f"Notebook converted to PDF: {output_pdf_path}")

def main():
    ipynb_path = input("Enter the path of the .ipynb file: ")
    
    # Extract code and save as .py file
    output_py_path = ipynb_path.replace('.ipynb', '.py')
    extract_code_from_ipynb(ipynb_path, output_py_path)

    # Optional: Convert to PDF
    convert_to_pdf = input("Do you want to convert the notebook to PDF as well? (y/n): ").lower()
    if convert_to_pdf == 'y':
        output_pdf_path = ipynb_path.replace('.ipynb', '.pdf')
        convert_ipynb_to_pdf(ipynb_path, output_pdf_path)

if __name__ == "__main__":
    main()
