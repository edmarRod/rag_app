from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import vstack

class Database:
    """
    Database class for storing documents and their vectors using TFIDF. Initializes with a list of documents which define the metrics for the tfidf.
    """
    def __init__(self, documents: list[str], tfidf_params: dict = None):
        self.closest = 5
        self.tfidf_params = {} if tfidf_params is None else tfidf_params
        self.raw_docs = documents
        self.tfidf = TfidfVectorizer(**self.tfidf_params)
        self.tfidf.fit(documents)
        self.vectors = self.tfidf.transform(documents)

    def add_document(self, document: str):
        self.raw_docs.append(document)
        self.vectors = vstack([self.vectors, self.tfidf.transform(document)])

    def remove_document(self, document: str):
        self.raw_docs.remove(document)
        self.vectors.remove(self.tfidf.transform(document)[0])

    def update_document(self, old_document: str, new_document: str):
        self.remove_document(old_document)
        self.add_document(new_document)
    
    def get_vector(self, document: str):
        return self.tfidf.transform(document)
    
    def get_document(self, vector):
        return self.raw_docs[self.vectors.index(vector)]

    def get_vectors(self):
        return self.vectors
    
    def get_raw_documents(self):
        return self.raw_docs

    def refit(self):
        self.tfidf.fit(self.raw_docs)
        self.vectors = self.tfidf.transform(self.raw_docs)

    def get_closest(self, document: str, vector_format: bool = False):
        vector = self.tfidf.transform([document])[0]
        print(vector.shape)
        distance = linear_kernel(vector, self.vectors).flatten()
        closest_idxs = distance.argsort()[-4:]
        print(closest_idxs.shape)
        if vector_format:
            return distance[closest_idxs]
        else:
            return [self.raw_docs[idx] for idx in closest_idxs]
        