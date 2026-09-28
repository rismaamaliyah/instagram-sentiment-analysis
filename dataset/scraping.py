from google_play_scraper import Sort, reviews
import pandas as pd

app_id = 'com.instagram.android'

all_reviews = []
count = 0
while count < 10000:
    rvs, _ = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=200,
        filter_score_with=None
    )
    all_reviews.extend(rvs)
    count = len(all_reviews)
    

df = pd.DataFrame(all_reviews)

df.to_csv("dataset/instagram_reviews.csv", index=False)

print("Total data:", len(df))
print(df.head())