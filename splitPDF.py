'''
To run the script and split a PDF file into batches, follow these steps:

install the PyPDF2 library using pip:
pip install PyPDF2

open the terminal or command prompt.
run the script by providing the path to the PDF file,
the number of pages per batch and output directory as command-line arguments:
python splitPDF.py path_to_pdf pages_per_batch output_dir

For example, to split a PDF file named input.pdf into batches of 10 pages each and save the output files to a directory named output_dir,
you would run the following command:
python splitPDF.py input.pdf 10 output_dir

'''
import PyPDF2
import sys
import os

def split_pdf_to_batches(pdf_path, pages_per_batch, output_dir):
    '''Function to split a PDF into batches'''
    # Ensure the file exists
    if not os.path.isfile(pdf_path):
        print(f"The file {pdf_path} does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Get the total number of pages
        total_pages = len(reader.pages)

        # Calculate the number of batches
        number_of_batches = total_pages // pages_per_batch + (total_pages % pages_per_batch > 0)

        # Start splitting into batches
        for batch in range(number_of_batches):
            pdf_writer = PyPDF2.PdfWriter()

            # Define the start and end page index for the current batch
            start_page = batch * pages_per_batch
            end_page = start_page + pages_per_batch
            end_page = min(end_page, total_pages)  # Ensure we don't go past the last page

            # Add the pages to the batch
            for page in range(start_page, end_page):
                pdf_writer.add_page(reader.pages[page])
    
            # Save the batch to a new PDF file
            batch_filename = f"{pdf_path.rstrip('.pdf')}_batch_{batch + 1}.pdf"
            batch_filepath = os.path.join(output_dir, batch_filename)
            with open(batch_filepath, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            print(f"Created {batch_filepath}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python split_pdf.py <path_to_pdf> <pages_per_batch> <output_dir>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    batch_size = int(sys.argv[2])
    output_directory = sys.argv[3]

    split_pdf_to_batches(pdf_file_path, batch_size, output_directory)
