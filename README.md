# Text Summarizer

A Python-based text summarization tool that supports both extractive and abstractive summarization methods.

## Features
- Extractive summarization using TF-IDF scoring
- Sentence ranking and selection
- Configurable summary length
- Support for multiple document formats

## Usage
```python
from summarizer import TextSummarizer

ts = TextSummarizer()
summary = ts.summarize(text, ratio=0.3)
```

## License
MIT License
