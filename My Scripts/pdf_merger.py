import os
import PyPDF2

# Function to merge PDF files in a given directory
def merge_pdf_files(directory, output_filename):
    merger = PyPDF2.PdfMerger()

    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            merger.append(filepath)

    output_filepath = os.path.join(directory, output_filename)
    merger.write(output_filepath)
    merger.close()
    print(f"Merged PDF files saved as {output_filename}")

# Usage
directory = '.\Outputs'  # Directory containing the PDF files
output_filename = 'BOB_merged.pdf'  # Output file name for merged PDF

merge_pdf_files(directory, output_filename)
