
from text_synonym import base


class Leadsynonymr(base.Basesynonymr):
    def __init__(
        self,
        language="english",
        preprocess_type="nltk",
        length_limit=10,
        stopwords_remove=True,
        debug=False,
    ):
        super().__init__(
            language, preprocess_type, stopwords_remove, length_limit, debug
        )
        return

    def synonym(self, text, limit_type="word", limit=100):
        raw_sentences = self.sent_tokenize(text)
        count = 0
        sentences_summary = []
        for s in raw_sentences:
            if count > limit:
                break
            sentences_summary.append(s)
            print("adding ", s)
            if limit_type == "word":
                count += len(s.split())
            else:
                count += len(s)

        summary = "\n*\n".join([s for s in sentences_summary])
        return summary
