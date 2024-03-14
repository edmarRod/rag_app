# Rag App

Implementation of a raw RAG App using a TFIDF vectorized database, llamafile to host a model and a main backend to connect both

## Quickstart

### Model Serving

To run the model server, just run the shell command in model_serve/tiny_llama.sh

```sh
sh tiny_llama.sh
```

This will boot up a localhost server in port 8080.

### Database

To start the database server, go cd into the directory and run the command using poetry.
```sh
cd doc_search
poetry run uvicorn main:app
```

This will boot up a localhost server in port 8000 and will init the database with imdb movie reviews.

### RAG

To have a RAG backend running, cd into the rag directory and start the server also using poetry.

```sh
cd rag
poetry run uvicorn main:app --port 9000
```

This will boot up a localhost backend in port 9000, where you will be able to request and generate response based on a query.