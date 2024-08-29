from typing import Union
from fastapi import FastAPI
import random
import logging
from utils.extraction.extract import extractTextFromVideo
from fastapi import FastAPI, File, UploadFile


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/extract-text")
async def create_upload_file(file: UploadFile):
    extractedText = extractTextFromVideo(file.filename)
    return {"extractedText": extractedText}
