from dataclasses import dataclass
from textblob import TextBlob

@dataclass
class Senti:
    face: str
    polarity: float
    subjectivity: float

def get_sentiment(inputxt: str, *, rnge: float) -> Senti:
    polarity : float = TextBlob(inputxt).sentiment.polarity
    subjectivity : float = TextBlob(inputxt).sentiment.subjectivity
    is_good: float = rnge
    is_bad: float = -rnge

    if polarity >= is_good:
        return Senti('positive', polarity, subjectivity)
    elif polarity <= is_bad:
        return Senti('negative', polarity, subjectivity)
    else:
        return Senti('neutral', polarity, subjectivity)


if __name__ == '__main__':
    while True:
        text: str = input('Insert Text:')
        feels: Senti = get_sentiment(text, rnge = 0.1)
        print(f'{feels.face}, {feels.polarity}, {feels.subjectivity}')