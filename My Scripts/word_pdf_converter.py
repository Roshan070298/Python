import win32com.client as win32

def convert_word_to_pdf(input_file, output_file):
    # Create an instance of the Word application
    word_app = win32.Dispatch('Word.Application')
    
    try:
        # Open the input Word document
        doc = word_app.Documents.Open(input_file)
        
        # Save the document as PDF
        doc.SaveAs(output_file, FileFormat=17)  # 17 represents PDF format
        
        # Close the document
        doc.Close()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        # Quit the Word application
        word_app.Quit()

# Usage
input_file = 'C:\PYTHON\My Scripts\Inputs\Roshan Chandel_SE.docx'
output_file = 'C:\PYTHON\My Scripts\Outputs\Roshan Chandel_SE.pdf'
convert_word_to_pdf(input_file, output_file)
