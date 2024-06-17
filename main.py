from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    content = """
    <html>
        <head>
            <title>FastAPI Client-Server Example</title>
        </head>
        <body>
            <h1>Welcome to FastAPI!</h1>
            <form action="/greet" method="get">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name">
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)







from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.get("/")
def read_root():
    content = """
    <html>
        <head>
            <title>FastAPI Client-Server Example</title>
        </head>
        <body>
            <h1>Welcome to FastAPI!</h1>
            <form action="/greet" method="get">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name">
                <input type="submit" value="Submit">
            </form>
            <br><br>
            <h2>OCR Upload</h2>
            <form action="/upload-image/" enctype="multipart/form-data" method="post">
                <label for="file">Upload an image:</label>
                <input type="file" id="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(image)
    return {"extracted_text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
