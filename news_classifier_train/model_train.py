import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

from synthetic_data import data

df = pd.DataFrame(data)
X_train, X_test, y_train, y_test = train_test_split(df['title'], df['category'], test_size=0.2, random_state=42)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

joblib.dump(model, 'news_classifier_model.joblib')



