import PyPDF2

# Open the PDF file
with open('8-Sci-NCERT-Book-Stars-and-The-Solar-System.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages
    num_pages = len(reader.pages)
    print(f"Total pages: {num_pages}")
    
    # Extract text from each page
    all_text = ""
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        all_text += page.extract_text() + "\n\n"
    
    # Print a preview of the text
    print("Text preview (first 1000 characters):")
    print(all_text[:1000])
    
    # Save the text to a file
    with open('ncert_solar_system_text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(all_text)
    
    print("Full text has been saved to 'ncert_solar_system_text.txt'") 