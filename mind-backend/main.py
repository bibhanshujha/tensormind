from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/query")
def query():
    return {"message": "Hello from mind-backend!"}

if __name__ == "__main__":
    main()
