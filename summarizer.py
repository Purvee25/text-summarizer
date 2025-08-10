import re
from collections import Counter
import math

class TextSummarizer:
    def __init__(self, language="english"):
        self.language = language
        self.stop_words = {"the","a","an","in","on","at","for","to","of","and","is","it","this","that","with","as","by","from","or","was","were","be","been","being","have","has","had","do","does","did","will","would","could","should","may","might","shall","can","not","but","if","then","else","when","up","out","no","so","its","my","your"}

    def _tokenize_sentences(self, text):
        return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

    def _tokenize_words(self, sentence):
        return [w.lower() for w in re.findall(r"\b\w+\b", sentence) if w.lower() not in self.stop_words]

    def _compute_tf(self, words):
        count = Counter(words)
        total = len(words)
        return {w: c / total for w, c in count.items()} if total > 0 else {}

    def _compute_idf(self, sentences_words):
        n = len(sentences_words)
        df = Counter()
        for words in sentences_words:
            for w in set(words):
                df[w] += 1
        return {w: math.log(n / (1 + freq)) for w, freq in df.items()}

    def _score_sentences(self, sentences, sentences_words, idf):
        scores = []
        for i, words in enumerate(sentences_words):
            tf = self._compute_tf(words)
            score = sum(tf.get(w, 0) * idf.get(w, 0) for w in words)
            scores.append((score, i, sentences[i]))
        return scores

    def summarize(self, text, ratio=0.3, min_sentences=1):
        sentences = self._tokenize_sentences(text)
        if len(sentences) <= min_sentences:
            return text
        sentences_words = [self._tokenize_words(s) for s in sentences]
        idf = self._compute_idf(sentences_words)
        scored = self._score_sentences(sentences, sentences_words, idf)
        n_select = max(min_sentences, int(len(sentences) * ratio))
        selected = sorted(scored, key=lambda x: x[0], reverse=True)[:n_select]
        selected.sort(key=lambda x: x[1])
        return " ".join(s[2] for s in selected)

if __name__ == "__main__":
    sample = "Natural language processing is a field of AI. It deals with the interaction between computers and humans. NLP techniques are used in many applications. Text summarization is one important NLP task. It reduces large texts to shorter versions. This helps users quickly understand key information."
    ts = TextSummarizer()
    print("Summary:", ts.summarize(sample, ratio=0.5))
