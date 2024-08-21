from fastapi import UploadFile
from pydantic import BaseModel


class ProcessPDF(BaseModel):
    """Input value of PDF"""
    value: str
