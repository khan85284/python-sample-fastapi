import tempfile

from fastapi import UploadFile
from unstructured.partition.pdf import partition_pdf


class PDFProcessorService:
    """Processing the PDF functions"""
    def __init__(self):
        pass

    def process_pdf(self, file: UploadFile) -> str:
        """Process the PDF through Unstructured Package"""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name
        elements = partition_pdf(filename=temp_file_path)
        result = "\n\n".join([str(el) for el in elements])
        print(result)
        return result
