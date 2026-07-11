#!/usr/bin/env python3
"""
Script to remove the first 20 pages from a PDF document.
"""

import sys
from PyPDF2 import PdfReader, PdfWriter


def remove_first_20_pages(input_pdf_path, output_pdf_path):
    """
    Remove the first 20 pages from a PDF and save the result.
    
    Args:
        input_pdf_path: Path to the input PDF file
        output_pdf_path: Path to save the output PDF file
    """
    try:
        # Read the input PDF
        reader = PdfReader(input_pdf_path)
        total_pages = len(reader.pages)
        
        print(f"Input PDF has {total_pages} pages")
        
        # Check if PDF has more than 20 pages
        if total_pages <= 25:
            print(f"Warning: PDF has only {total_pages} pages. Cannot remove 20 pages.")
            print("No output file will be created.")
            return
        
        # Create a PDF writer
        writer = PdfWriter()
        
        # Add pages starting from page 21 (index 20)
        for page_num in range(20, total_pages):
            writer.add_page(reader.pages[page_num])
        
        # Write the output PDF
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Successfully created output PDF with {total_pages - 20} pages")
        print(f"Output saved to: {output_pdf_path}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_pdf_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing PDF: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python remove_first_20_pages.py <input_pdf> [output_pdf]")
        print("\nExample:")
        print("  python remove_first_20_pages.py document.pdf")
        print("  python remove_first_20_pages.py document.pdf output.pdf")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    
    # If output file is not specified, create a default name
    if len(sys.argv) >= 3:
        output_pdf = sys.argv[2]
    else:
        # Create output filename by adding suffix
        if input_pdf.lower().endswith('.pdf'):
            output_pdf = input_pdf[:-4] + '_without_first_20.pdf'
        else:
            output_pdf = input_pdf + '_without_first_20.pdf'
    
    remove_first_20_pages(input_pdf, output_pdf)


if __name__ == "__main__":
    main()
