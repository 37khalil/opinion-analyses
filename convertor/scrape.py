import pandas as pd
import snscrape.modules.twitter as sntwitter
import os

dirname = os.path.dirname(__file__)
output = os.path.join(dirname, '../data/twitter/arabic.json')

search = 'التنموي# OR النموذج# OR #الديمقراطية_التشاركية OR #النموذج_التنموي_الجديد OR #المغرب_لي_بغينا OR #النموذج_التنموي OR #المواطن_والنموذج_التنموي OR #المجلس_الاقتصادي_والاجتماعي_والبيئي lang:ar include:nativeretweets'

# the scraped tweets, this is a generator
scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()

# convert to a DataFrame and keep only relevant columns
df = pd.DataFrame(scraped_tweets)[['date', 'content']]

print(df.shape)

with open(output, "w", encoding="utf-16") as file:
    file.write("[" +
               df.to_json(orient='records', force_ascii=False)[
                   1:-1].replace('} {', '}, {')+"]"
               )
