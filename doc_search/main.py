from fastapi import FastAPI

from client import init_db

app = FastAPI()

db = init_db(documents=None, tfidf_params={"ngram_range": (1, 1), "stop_words": "english", "use_idf": True, "smooth_idf": True, "sublinear_tf": True})

@app.post("/add_document")
async def add_document(document: str):
    db.add_document(document)
    return {"message": "successfully added document"}


@app.post("/remove_document")
async def remove_document(document: str):
    db.remove_document(document)
    return {"message": "successfully removed document"}


@app.post("/update_document")
async def update_document(old_document: str, new_document: str):
    db.update_document(old_document, new_document)
    return {"message": "successfully updated document"}


@app.get("/get_document/{vector}")
async def get_document(vector):
    document = db.get_document(vector)
    return {"document": document}


@app.get("/get_vector/{document}")
async def get_vector(document: str):
    vector = db.get_vector(document)
    return {"vector": vector.tolist()}


@app.get("/get_raw_documents")
async def get_raw_documents():
    documents = db.get_raw_documents()
    return {"documents": documents}


@app.get("/get_vectors")
async def get_vectors():
    vectors = db.get_vectors()
    return {"vectors": [v.tolist() for v in vectors]}


@app.post("/refit")
async def refit():
    db.refit()
    return {"message": "successfully refitted"}

@app.get("/get_closest")
async def get_closest(document: str):
    closest = db.get_closest(document)
    return {"closest": closest}


