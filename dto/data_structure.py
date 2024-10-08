from pydantic import BaseModel
from typing import List

class ArticleInput(BaseModel):
    urls: List[str]

class ScrapedDataInput(BaseModel):
    scraped_data: List[dict]

class DatabaseDataInput(BaseModel):
    data: List[dict]