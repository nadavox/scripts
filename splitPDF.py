import PyPDF2
import os
import sys
# Users/nadavox/Downloads/threejs_tutorial.pdf
def split_pdf_to_batches(pdf_path, pages_per_batch):
    # Ensure the file exists
    # if not os.path.isfile(pdf_path):
    #     print(f"The file {pdf_path} does not exist.")
    #     return

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
            with open(batch_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            print(f"Created {batch_filename}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_pdf.py <path_to_pdf> <pages_per_batch>")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    batch_size = int(sys.argv[2])

    split_pdf_to_batches(pdf_file_path, batch_size)
