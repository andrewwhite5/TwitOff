import basilica, os
from dotenv import load_dotenv

load_dotenv()

basilica_api_key = os.getenv('basilica_api_key', default='Oops')

sentences = [
    "This is a sentence.",
    "This is a similar sentence.",
    "I don't think this sentence is very similar at all..."
]

with basilica.Connection(basilica_api_key) as c:
    embeddings = c.embed_sentences(sentences)
    print(list(embeddings))

for emb in embeddings:
    print(type(emb))
    print(emb)
    print('-----------------')

connection.close()
