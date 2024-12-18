
import pdfkit

# Specify the input HTML file and output PDF file
input_html_file = 'example.html'  # Replace with your HTML file path
output_pdf_file = 'output.pdf'   # Desired output PDF file name

# Convert HTML file to PDF
try:
    pdfkit.from_file(input_html_file, output_pdf_file)
    print(f"Successfully converted {input_html_file} to {output_pdf_file}")
except Exception as e:
    print("An error occurred while converting the file:", e)
