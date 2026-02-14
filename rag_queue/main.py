# this project is same as the rag_project but with efficient utilization of resources using redis queue 
# 1. We create the redis queue setup
# 2. adding the post query into the queue which in turn gives job id
# 3. fetching the result with the help of job id
# with this we have efficiently used our resource from blocking the resource 

from .server import app
import uvicorn

def main():
    uvicorn.run(app,port=8080,host="0.0.0.0")

main()