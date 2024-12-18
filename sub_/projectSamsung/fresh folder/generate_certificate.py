import pandas as pd
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

# Path to wkhtmltopdf - Adjust this path to your system's wkhtmltopdf installation
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Function to load data from Excel
def load_excel_data(excel_file):
    try:
        data = pd.read_excel(excel_file)
        print("Excel file loaded successfully!")
        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

# Function to generate HTML content from template
def generate_certificate_html(template_dir, template_name, student_data):
    try:
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)
        html_content = template.render(name=student_data['Name'], usn=student_data['USN'])
        return html_content
    except Exception as e:
        print(f"Error generating HTML: {e}")
        return None

# Function to save HTML content as PDF
def save_html_to_pdf(html_content, output_pdf_path, config):
    try:
        pdfkit.from_string(html_content, output_pdf_path, configuration=config)
        print(f"Certificate saved: {output_pdf_path}")
    except Exception as e:
        print(f"Error saving PDF: {e}")

# Function to generate certificates
def generate_certificates(excel_file, template_dir, template_name, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load Excel data
    data = load_excel_data(excel_file)
    if data is None:
        return

    # Configure pdfkit with wkhtmltopdf path
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

    # Generate certificates
    for index, row in data.iterrows():
        print(f"Generating certificate for: {row['Name']}...")
        html_content = generate_certificate_html(template_dir, template_name, row)
        if html_content:
            output_pdf_path = os.path.join(output_dir, f"{row['Name']}.pdf")
            save_html_to_pdf(html_content, output_pdf_path, config)

if __name__ == "_main_":
    # File and folder paths
    excel_file = "students.xlsx"                       # Excel file with data
    template_dir = "."                                 # Directory where HTML template is stored
    template_name = "certificate_template.html"        # HTML template filename
    output_dir = "certificates"                        # Folder to save PDFs

    # Generate certificates
    generate_certificates(excel_file, template_dir, template_name,(output_dir))