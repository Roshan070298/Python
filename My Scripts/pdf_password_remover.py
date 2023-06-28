import PyPDF2
import os

def remove_password(input_path, output_path, password):
    try:
        with open(input_path, 'rb') as input_file, \
                open(output_path, 'wb') as output_file:
            pdf = PyPDF2.PdfReader(input_file)
            if pdf.is_encrypted:
                pdf.decrypt(password)
            writer = PyPDF2.PdfWriter()
            for page_num in range(len(pdf.pages)):
                page=pdf.pages[page_num]
                writer.add_page(page)
            writer.write(output_file)
    except Exception as e:
        print(f"could not decrypt the file {input_file} {e}")
# Usage
# input_file_path = '.\Statement_MAR2023_705339579.pdf'
# output_file_path = '.\Outputs\Statement_MAR2023_705339579.pdf'
# password = ''

folder_path = os.path.join('.\Inputs')
files = os.listdir(folder_path)
for file in files:
    input_file_path = f".\Inputs\{file}"
    output_file_path = f".\Outputs\{file}"
    password = '07021998BHIPC0256N'
    remove_password(input_file_path, output_file_path, password)



