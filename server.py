from fastapi import FastAPI, UploadFile
from fastapi.logger import logger

app = FastAPI()


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    name = file.filename
    data = file.file.read()
    logger.debug(f"filename: {name}, filedata:{data}")
    return {"filename": name, "filedata": data}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("server:app")
