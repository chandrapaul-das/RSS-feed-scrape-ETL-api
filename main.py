from fastapi import FastAPI, HTTPException

from services.scraper_service import article_scraper
from services.news_classification_service import news_classifier
from services.database_service import insert_new_articles
from dto.data_structure import ArticleInput, ScrapedDataInput, DatabaseDataInput

app = FastAPI()


#main ETL pipeline api
@app.post("/article-dump-ETL/")
async def process_articles(input_data: ArticleInput):
    try:
        scrape_response = await scrape_articles(input_data)
        scraped_data = scrape_response['scraped_data']
        
        classify_input = ScrapedDataInput(scraped_data=scraped_data)
        classify_response = await classify_articles(classify_input)
        classified_data = classify_response['classified_data']

        database_input = DatabaseDataInput(data=classified_data)
        await insert_data(database_input)
        
        return {"message": "Articles processed and inserted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

#sub-feature apis
@app.post("feature/scrape-articles/")
async def scrape_articles(input_data: ArticleInput):
    try:
        data = article_scraper(input_data.urls)
        return {"scraped_data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("feature/classify-articles/")
async def classify_articles(input_data: ScrapedDataInput):
    try:
        classified_data = news_classifier(input_data.scraped_data)
        return {"classified_data": classified_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("feature/insert-new-articles/")
async def insert_data(input_data: DatabaseDataInput):
    try:
        insert_new_articles(input_data.data)
        return {"message": "Data inserted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

