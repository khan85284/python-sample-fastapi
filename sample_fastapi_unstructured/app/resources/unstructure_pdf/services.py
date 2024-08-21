from fastapi import UploadFile
from unstructured.partition.pdf import partition_pdf


class PDFProcessorService:
    """Processing the PDF functions"""
    def __init__(self):
        pass

    def process_pdf(self, file: UploadFile) -> str:
        """Process the PDF through Unstructured Package"""
        elements = partition_pdf(filename=file.filename)
        result = "\n\n".join([str(el) for el in elements])
        print(result)
        return result
