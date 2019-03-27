import spacy
from newspaper import Article
nlp = spacy.load("en_core_web_sm")

url_1 = 'https://www.wsj.com/articles/u-s-officials-walk-out-of-meeting-at-presidential-palace-in-kabul-11553628051'
url_2 = 'https://www.wsj.com/articles/iran-moves-to-cement-its-influence-in-syria-11553632926'
article_1 = Article(url_1)
article_2 = Article(url_2)
article_1.download()
article_2.download()
article_1.parse()
article_2.parse()

article_stream = [article_1.text, article_2.text]

for doc in nlp.pipe(article_stream, batch_size=50):
    print(doc.vocab)


# for entity in doc.ents:
#     print(entity.text, entity.start_char, entity.end_char, entity.label_)
