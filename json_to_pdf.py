import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# TODO:
#   1) Create PDF object
#   2) Transform JSON to usable output
#   3) Write JSON to PDF object
#   4) Save PDF to Location

def add_header(pdf_file: canvas, header_text: str) -> int:
    """
    Adds a header to a PDF document.
    Returns the last y-position written to the canvas.
    """
    # set header font
    pdf_file.setFont("Helvetica", 14)

    # set margins
    top_margin = 72
    left_margin = 72

    # header position
    y_position = letter[1] - top_margin

    # Add the header text
    pdf_file.drawString(left_margin, y_position, header_text)
    y_position -= 20
    return y_position


def json_to_pdf(json_obj, save_path: str) -> None:
    """
    Converts and saves a JSON string to a PDF.
    """
    # create PDF using the American standard page size
    pdf_file = canvas.Canvas(save_path, pagesize=letter)

    # add header to PDF
    y_position = add_header(pdf_file, "Expense Report")

    width, height = letter  # get page width and height

    left_margin = 72  # set left margin

    pdf_file.setFont("Helvetica", 10)  # set font

    # draw each JSON item to the PDF
    for item in json_obj:
        pdf_file.drawString(left_margin, y_position, item)
        y_position -= 20


    pdf_file.save()
    print(f"PDF file saved to: {save_path}")


def main():
    
    return

if __name__ == "__main__":
    main()