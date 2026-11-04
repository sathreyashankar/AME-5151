from builtins import Exception
import os
import numpy as np
from gensim.models import KeyedVectors

"""
Using word2vec model to illustrate linear algebra operations
on word vectors, such as computing similarity and inner products.
"""

def load_model(word2vec_model_path:str) -> KeyedVectors:
    try:
        fast_model_path = os.path.expanduser(word2vec_model_path)
        return KeyedVectors.load(fast_model_path, mmap='r')
    except Exception as e:
        print(f"Failed to load model in word2vec format: {e}")
    return None


if __name__ == "__main__":
    word2vec_model_path = "../glove50/glove_50_fast.wordvectors"
    model = load_model(word2vec_model_path)
    assert model is not None, "Model loading failed."


TAG_WORDS = [
    'research', 'innovation', 'education', 'university', 'students',
'faculty', 'campus', 'engineering', 'medicine', 'technology', 'curriculum', 'collaboration', 'publication',
'laboratory', 'scholarship', 'mentorship', 'internship', 'entrepreneurship', 'accreditation', 'alumni'
]


# `tags` - list of words
# get_word_vectors is a function to get the vectors
def get_word_vectors(models, tags): 
    word_vectors = []
    dropped_words = [] # list of words not found in the model

    for tag in tags:
        try:
            tv = models[tag]
            word_vectors.append(tag)  # List of all the vectors that are present in models
        except:
            # pass
            dropped_words.append(tag) # List of all the vectors that are NOT present in models
            word_vectors.append(None)
    return ((word_vectors, dropped_words))


# Unit Test : To check for the Empty Tag
def test_empty_tags():
    model = load_glove_50_model()
    result = get_word_vectors(model, [])
    assert result == ([], [])

# Unit Test : To check for tag containing only 1 word, that does NOT exist in the given model
def test_one_word_tag_not_in_model():
    model = load_glove_50_model()
    one_word = '####&&&&$$$$'
    result = get_word_vectors(model, one_word)
    assert result == ([], [one_word])





