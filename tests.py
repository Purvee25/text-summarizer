from summarizer import TextSummarizer

def test_basic_summarize():
    ts = TextSummarizer()
    text = "AI is transforming industries. Machine learning is a subset of AI. Deep learning uses neural networks. NLP processes human language. Computer vision analyzes images. Reinforcement learning trains agents."
    summary = ts.summarize(text, ratio=0.3)
    assert len(summary) < len(text)
    assert len(summary) > 0

def test_empty_text():
    ts = TextSummarizer()
    assert ts.summarize("Hello.") == "Hello."

def test_ratio():
    ts = TextSummarizer()
    text = "First sentence. Second sentence. Third sentence. Fourth sentence. Fifth sentence."
    s1 = ts.summarize(text, ratio=0.2)
    s2 = ts.summarize(text, ratio=0.8)
    assert len(s1) <= len(s2)

if __name__ == "__main__":
    test_basic_summarize()
    test_empty_text()
    test_ratio()
    print("All tests passed!")
