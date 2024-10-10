from get_topstories import get_top_news_from_india
from get_comment import return_comment
from post_to_twitter import post_tweet
from get_joke_potential import get_joke_potential_score

articles = get_top_news_from_india()

for article in articles:
    headline = article['title']
    humour_potential = get_joke_potential_score(headline)
    if len(headline)<80: #and humour_potential>=5:
        url = article['url']
        comment = return_comment(headline)
        tweet = comment+' '+url
        post_tweet(tweet)
