import base64
import json
import io
from dotenv import load_dotenv
from openai import OpenAI
from werkzeug.datastructures import FileStorage
from pdf2image import convert_from_bytes

load_dotenv()

client = OpenAI()

def classify_file(file: FileStorage, potential_document_classes: list[str], model: str = "gpt-4o-mini"):
    file_name = file.filename

    content_type = file.content_type
    if content_type == "image/jpeg" or content_type == "image/png":
        image_files = [file]
    elif content_type == "application/pdf":
        image_files = pdf_to_jpgs(file)
    else:
        raise ValueError("Unsupported file type") # This should have already been checked, therefore this should not happen

    base64_images = [ base64.b64encode(image_file.read()).decode('utf-8') for image_file in image_files ]
    base64_image_content_dicts = [ { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{base64_image}" } } for base64_image in base64_images ]

    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a diligent assistant with years of experience classifying documents and processing workflows in financial services. Your task is to read documents and correctly classify them."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Please classify this document for me. It might (or might not) help you to know that the file name is {file_name}."
                    },
                    *base64_image_content_dicts
                ]
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "document_classifier",
                "schema": {
                    "type": "object",
                    "properties": {
                        "document_class": {
                            "type": "string",
                            "enum": potential_document_classes
                        }
                    },
                    "required": [
                        "document_class"
                    ],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
    )

    return json.loads(response.choices[0].message.content)["document_class"]

def pdf_to_jpgs(file: FileStorage):
    pdf_bytes = file.read()
    images = convert_from_bytes(pdf_bytes)
    image_files = []

    for i, image in enumerate(images):
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)

        if len(images) == 1:
            image_filename = f"{file.filename.rsplit('.', 1)[0]}.jpg"
        else:
            image_filename = f"{file.filename.rsplit('.', 1)[0]}_page{i + 1}.jpg"

        image_file = FileStorage(img_byte_arr, filename=image_filename, content_type='image/jpeg')
        image_files.append(image_file)

    return image_files