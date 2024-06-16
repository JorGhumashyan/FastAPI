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
