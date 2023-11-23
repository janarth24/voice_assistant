# Install required libraries
# pip install gensim nltk

import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

nltk.download("stopwords")
nltk.download("punkt")

# Load and preprocess the text
def read_article(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    
    sent1 = [word.lower() for word in sent1]
    sent2 = [word.lower() for word in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in sent1:
        if word in stopwords:
            continue
        vector1[all_words.index(word)] += 1

    for word in sent2:
        if word in stopwords:
            continue
        vector2[all_words.index(word)] += 1

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stop_words)

    return similarity_matrix

def generate_summary(text, num_sentences=5):
    stop_words = stopwords.words('english')
    sentences = read_article(text)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)

    # Rank sentences based on their similarity scores
    sentence_scores = np.array(sentence_similarity_matrix).sum(axis=1)

    # Get the top N sentences as the summary
    ranked_sentences = [sentences[i] for i in np.argsort(sentence_scores)[::-1][:num_sentences]]

    return " ".join(ranked_sentences)

# Example usage
# document = """
# Text summarization is the process of generating a concise and coherent 
# summary of a longer text document while preserving its most important information. 
# There are two main approaches to text summarization: extractive and abstractive summarization.
#  Extractive summarization involves
#    selecting and rearranging sentences or phrases from the original text, while abstractive
#      summarization generates summaries by paraphrasing and rephrasing the content.
# """
import transcript
document=transcript.text

summary = generate_summary(document, num_sentences=2)
print(summary)
