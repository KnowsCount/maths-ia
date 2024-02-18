import os
import subprocess

def convert_md_to_docx(md_file, docx_file):
    try:
        # Run the pandoc command in the shell
        subprocess.run(["pandoc", md_file, "-o", docx_file], check=True)
        print(f"Converted {md_file} to {docx_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {md_file} to {docx_file}")
        print(f"Error: {e}")

# Use the function
convert_md_to_docx("paper.md", "output.docx")
