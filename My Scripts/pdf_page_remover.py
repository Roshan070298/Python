from PyPDF2 import PdfReader, PdfWriter
import os

def delete_pages(input_path, output_path, pages):
    # Open the input PDF file
    with open(input_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Create a new PDF writer
        pdf_writer = PdfWriter()

        # Add pages to the new PDF writer except the ones to be deleted
        for page_number in range(total_pages):
            if page_number + 1 not in pages:
                page = pdf_reader.pages[page_number]
                pdf_writer.add_page(page)

        # Write the new PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print('Pages deleted successfully.')

# # Specify the input and output file paths
# input_file = 'input.pdf'
# output_file = 'output.pdf'

# # Specify the pages to be deleted (e.g., [1, 3, 5])
# pages_to_delete = [1, 3, 5]

# # Delete the specified pages
# delete_pages(input_file, output_file, pages_to_delete)


folder_path = os.path.join('.\Inputs')
files = os.listdir(folder_path)
for file in files:
    input_file_path = f".\Inputs\{file}"
    output_file_path = f".\Outputs\{file}"
    pages_to_delete = [1]
    delete_pages(input_file_path, output_file_path, pages_to_delete)