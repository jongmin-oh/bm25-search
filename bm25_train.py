from rank_bm25 import BM25Okapi
import pickle
from korean_tokenizer import tokenizer
import pandas as pd

df = pd.read_pickle('./data/base_datasets.pkl')

corpus = df['user'].tolist()
tokenized_corpus = [tokenizer(doc) for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

# To save bm25 object
with open('bm25result', 'wb') as bm25result_file:
    pickle.dump(bm25, bm25result_file)
