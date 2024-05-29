
ADDITIONAL_INCLUDES_TEXT = """
## Additional Includes
This is usually included libraries needed as context to write better tests:
======
{included_files}
======
"""

included_files_content = "file1.py, file2.py, file3.py"

formatted_text = ADDITIONAL_INCLUDES_TEXT.format(included_files=included_files_content)

print(formatted_text)
