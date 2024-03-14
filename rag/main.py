from fastapi import FastAPI
import json
import requests

app = FastAPI()

@app.get("/query")
async def query(query:str):
    context = requests.get("http://127.0.0.1:8000/get_closest", params={"document": query})
    context = json.loads(context.text)['closest']
    context = '\n'.join([str(i)+": "+content for i, content in enumerate(context)][:1])
    prompt = f"""Answer this query:
    {query}
    Given this context:
    {context}"""

    response = requests.post("http://127.0.0.1:8080/completion", json={"prompt": prompt[:2048]})
    return {'response:': response.json()}
    

