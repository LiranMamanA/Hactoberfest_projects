import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "NeutraL"


def main():
    nltk.download('vader_lexicon')
    print("Sentiment Analysis Tool")
    print("-----------------------")
    text = input("Enter text to analyze sentiment: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)


if __name__ == "__main__":
    main()