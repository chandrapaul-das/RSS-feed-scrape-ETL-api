import sqlite3
from datetime import datetime

def fetch_articles():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM ArticlesCollection''')
    rows = cursor.fetchall()
    conn.close()

    return rows

def insert_new_articles(data):

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    
    insert_sql = '''
        INSERT INTO ArticlesCollection (category, title, link, description, published)
        VALUES (?, ?, ?, ?, ?)
    '''
    
    for article in data:
        title = article['title']
        category = article['category']
        link = article['link']
        description = article['description']
        try:
            published = datetime.strptime(article['published'], '%a, %d %b %Y %H:%M:%S %Z')
        except Exception as e:
            published = None

        cursor.execute('SELECT COUNT(*) FROM ArticlesCollection WHERE title = ?', (title,))
        exists = cursor.fetchone()[0]
        
        if exists == 0:
            cursor.execute(insert_sql, (category, title, link, description, published))
            print(f"Inserted: {title}")
        else:
            print(f"Duplicate title found, not inserting: {title}")

    conn.commit()
    conn.close()