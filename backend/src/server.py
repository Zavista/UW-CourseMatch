from fastapi import FastAPI


app = FastAPI(
    version="0.1.0",
    title="UW CourseMatch API",
    description="A simple API to match students with courses"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the UW CourseMatch API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)