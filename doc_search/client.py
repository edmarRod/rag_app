from database import Database

import subprocess
import os
import glob

def init_db(documents: list[str], tfidf_params: dict):
    if documents is None:
        documents = _cold_init_docs()
    db = Database(documents, tfidf_params)
    return db


def _cold_init_docs():
    # Downloads and unpacks the imdb reviews dataset, then joins all the reviews, separates into train and validation sets and cleans up
    if not os.path.exists('data/imdb.txt'):
        if not os.path.exists('data'): 
            os.makedirs('data')
        subprocess.run('wget -nc http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'.split())
        subprocess.run('tar -zxvf aclImdb_v1.tar.gz -C data'.split())

        #reads all reviews from file and randomly assigns to train or validation

        with open('data/imdb.txt', 'w') as imdb:
            for file in glob.glob('data/aclImdb/*/*/*.txt'):
                with open(file, 'r') as cur_text_file:
                    for line in cur_text_file:
                        imdb.write(line)
                        imdb.write('\n')



        subprocess.run('rm aclImdb_v1.tar.gz'.split())
        subprocess.run('rm -r data/aclImdb'.split())

    docs = open('data/imdb.txt', 'r').read().split('\n')
    return docs