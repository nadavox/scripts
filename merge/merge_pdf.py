import argparse
import PyPDF2

def merge_pdfs(pdf_list, output):
    if ".pdf" not in output:
        output += ".pdf"
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through all PDFs
    for pdf in pdf_list:
        # Open the PDF file
        with open(pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Add each page to the writer object
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    # Save the merged PDF to the output file
    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

    print(f"Merged PDF saved as '{output}'")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into a single PDF.')
    # Add the arguments
    parser.add_argument('--files', nargs='+', help='List of PDF files to merge', required=True)
    parser.add_argument('--name', type=str, help='Name of the output PDF file', required=True)

    # Parse the arguments
    args = parser.parse_args()

    # Call the merge function
    merge_pdfs(args.files, args.name)

if __name__ == "__main__":
    main()
