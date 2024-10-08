import joblib

model = joblib.load('news_classifier_model.joblib')

def classify_news_title(title):
    return model.predict([title])[0]

def news_classifier(data_ls):
    for data in data_ls:
        data['category'] = classify_news_title(data['title'])
    
    return data_ls