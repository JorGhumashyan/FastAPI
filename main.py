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




####################################################### 


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



# ########################################################################### 





from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str


tasks_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI To-Do List Application!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    for existing_task in tasks_db:
        if existing_task.id == task.id:
            raise HTTPException(status_code=400, detail="Task ID already exists")
    
    tasks_db.append(task)
    return task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            tasks_db.remove(task)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



# uvicorn main:app --reload (how to run)
#  curl -X 'GET' \
# 'http://127.0.0.1:8000/tasks' \
# -H 'accept: application/json'   (get all tasks)


# curl -X 'POST' \
# 'http://127.0.0.1:8000/tasks' \
#-H 'accept: application/json' \
#-H 'Content-Type: application/json' \
#-d '{
#"id": 1,
#"title": "Buy groceries",
#"description": "Milk, Bread, Cheese"
#}'     (create new list)





