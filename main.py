from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def text_to_pdf(input_file, output_file, cover_image=None, book_title=None, author_name=None):
    c = canvas.Canvas(output_file, pagesize=letter)

    # Add cover image if provided
    if cover_image:
        c.drawImage(cover_image, 0, 0, width=8.5 * inch, height=11 * inch)
        c.showPage()

    # Start from the second page if there's a cover image
    c.setPageSize(letter)

    # Write book title and author's name on the second page if provided
    if book_title and author_name:
        c.setFont("Helvetica-Bold", 40)
        c.drawCentredString(letter[0] / 2, letter[1] / 2, book_title)
        c.setFont("Helvetica", 20)
        c.drawCentredString(letter[0] / 2, letter[1] / 2 - 30, author_name)
        c.showPage()

    with open(input_file, 'r', encoding='utf-8') as file:  # Specify encoding
        lines = file.readlines()
        y = 750
        line_number = 1
        line_height = 20  # Adjust this value to increase/decrease line height
        word_spacing = 5  # Adjust this value to increase/decrease space between words
        for line in lines:
            words = line.strip().split()  # Split line into words
            x = 50  # Initial x-coordinate for each line
            remaining_words = words[:]
            while remaining_words:
                line_words = remaining_words[:15]  # Get up to 15 words for each line
                remaining_words = remaining_words[15:]  # Remove the words that have been processed
                line_text = ' '.join(line_words)
                c.drawString(x, y, line_text)  # Draw the line
                y -= line_height
                if y < 50:
                    c.drawString(550, 30, f"{line_number}")
                    c.showPage()
                    line_number += 1
                    y = 750
        c.drawString(550, 30, f"{line_number}")  # Add page number for the last page
    c.save()


if __name__ == "__main__":
    input_file = "input.txt"  # Change this to your input text file
    output_file = "output.pdf"  # Change this to the desired output PDF file name
    cover_image = "image.png"  # Change this to the path of your cover image, if any
    book_title = "Autobiography Moonlight"  # Change this to the title of your book
    author_name = "Tran_GCD"  # Change this to the author's name
    text_to_pdf(input_file, output_file, cover_image, book_title, author_name)
