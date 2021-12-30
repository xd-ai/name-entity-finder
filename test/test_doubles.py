class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ent(self, ents):
        self.ents = ents

    def __call__(self, sentence):
        return DocTestDouble(sentence, self.ents)

class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sentence, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

    def patch_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self

class SpanTestDouble:
    """
    Test double for spaCy Span
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label
