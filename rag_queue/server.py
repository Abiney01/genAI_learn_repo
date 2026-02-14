from fastapi import FastAPI,Query
from .client.rq_client import queue
from .queues.worker import process_query

# creating app via fastapi
app = FastAPI()
# creating a get route
@app.get("/")
def root():
    return {"status": "Server is up and running"}

# creating a post chat route to ask query and enqueue into the queue along with we pass the process query(for similarity search and getting the result) and query
@app.post("/chat")
def chat (
        query : str = Query(...,description="The chat query of user")
):
    job = queue.enqueue(process_query,query)
    return {"status":"queued","job_id":job.id}

# creating a get route to get the status with the help of job id given by the post route
@app.get('/job-status')
def get_result(
        job_id : str = Query(...,description="Job Id")
):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()
    return {"result":result}