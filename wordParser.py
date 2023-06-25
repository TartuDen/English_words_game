from docx import Document

def parse_word_table(file_path):
    # Load the Word document
    doc = Document(file_path)

    # Access the first table in the document
    table = doc.tables[0]

    # Iterate through each row in the table
    for row in table.rows:
        # Access the cells in the row
        cells = row.cells

        # Check if the row has at least 4 cells
        if len(cells) >= 4:
            try:
                # Extract the word and description from the 2nd column
                word, description = cells[1].text.split('-')
            except ValueError:
                word = cells[1].text.split('-')
                description = " "
                

            # Remove leading/trailing whitespaces from the word and description
            if isinstance(word, str):
                word = word.strip()
            if isinstance(description, str):
                description = description.strip()

            # Move the description to the 4th column
            cells[3].text = description

    # Save the modified document
    doc.save(file_path)

# Provide the file path of your Word document
file_path = 'wordFiles\\MainEnglish - test.docx'

# Call the function to parse the Word table and move descriptions
parse_word_table(file_path)
