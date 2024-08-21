from fastapi import Depends, File, HTTPException, UploadFile, status

from .models import ProcessPDF
from .services import PDFProcessorService


async def process_pdf(file: UploadFile = File(...), processor: PDFProcessorService = Depends(PDFProcessorService)) -> ProcessPDF:
    """Convert hexadecimal string input into integer"""
    try:
        return ProcessPDF(
            value=processor.process_pdf(file),
        )
    except ValueError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Invalid hexadecimal input "%s"' % file,
        )
