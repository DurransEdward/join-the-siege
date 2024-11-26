import os
from werkzeug.datastructures import FileStorage
from io import BytesIO

file_path = os.path.join(os.path.dirname(__file__), f'./files')

def create_file_storage(file_name, content_type):
    return FileStorage(stream=BytesIO(open(f"{file_path}/{file_name}", 'rb').read()), filename=file_name, content_type=content_type)

TEST_DATA = [
    {
        "file_name": "bank_statement_1.pdf",
        "content_type": "application/pdf",
        "document_class": "bank_statement",
        "file": create_file_storage("bank_statement_1.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf bank statement"
    },
    {
        "file_name": "bank_statement_2.pdf",
        "content_type": "application/pdf",
        "document_class": "bank_statement",
        "file": create_file_storage("bank_statement_2.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf bank statement"
    },
    {
        "file_name": "bank_statement_3.pdf",
        "content_type": "application/pdf",
        "document_class": "bank_statement",
        "file": create_file_storage("bank_statement_3.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf bank statement"
    },
    {
        "file_name": "drivers_licence_1.jpg",
        "content_type": "image/jpeg",
        "document_class": "drivers_licence",
        "file": create_file_storage("drivers_licence_1.jpg", "image/jpeg"),
        "allowed_file": True,
        "description": "A rendered jpeg mock drivers licence"
    },
    {
        "file_name": "drivers_licence_2.jpg",
        "content_type": "image/jpeg",
        "document_class": "drivers_licence",
        "file": create_file_storage("drivers_licence_2.jpg", "image/jpeg"),
        "allowed_file": True,
        "description": "A standard jpeg drivers licence"
    },
    {
        "file_name": "drivers_licence_3.jpg",
        "content_type": "image/jpeg",
        "document_class": "drivers_licence",
        "file": create_file_storage("drivers_licence_3.jpg", "image/jpeg"),
        "allowed_file": True,
        "description": "A standard jpeg drivers licence"
    },
    {
        "file_name": "invoice_1.pdf",
        "content_type": "application/pdf",
        "document_class": "invoice",
        "file": create_file_storage("invoice_1.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf invoice"
    },
    {
        "file_name": "invoice_2.pdf",
        "content_type": "application/pdf",
        "document_class": "invoice",
        "file": create_file_storage("invoice_2.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf invoice"
    },
    {
        "file_name": "invoice_3.pdf",
        "content_type": "application/pdf",
        "document_class": "invoice",
        "file": create_file_storage("invoice_3.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf invoice"
    },
    {
        "file_name": "invoice_4.pdf",
        "content_type": "image/png",
        "document_class": "invoice",
        "file": create_file_storage("invoice_4.png", "image/png"),
        "allowed_file": True,
        "description": "A standard png invoice"
    },
    {
        "file_name": "resume_1.pdf",
        "content_type": "application/pdf",
        "document_class": "CV",
        "file": create_file_storage("resume_1.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf CV"
    },
    {
        "file_name": "invoice_5.pdf",
        "content_type": "application/pdf",
        "document_class": "bank_statement",
        "file": create_file_storage("invoice_5.pdf", "application/pdf"),
        "allowed_file": True,
        "description": "A standard pdf bank statement BUT with the name invoice_5.pdf"
    },
    {
        "file_name": "cat.jpg",
        "content_type": "image/jpeg",
        "document_class": "unknown file",
        "file": create_file_storage("cat.jpg", "image/jpeg"),
        "allowed_file": True,
        "description": "An image of a cat"
    }
]