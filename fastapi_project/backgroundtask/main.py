from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def process_data():
    # Simulate a long-running process
    import time
    time.sleep(20)
    print("Background task executed.")

@app.post("/submit-task/")
async def submit_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_data)
    return {"message": "Task submitted."}
