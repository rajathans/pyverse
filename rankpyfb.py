import facebook
from sys import argv

page_id = argv

def get_fb_page_like_count(page_id):
    graph = facebook.GraphAPI(access_token='CAAWIdyCx6egBAM7OmJNv5JeUlloamnTcl9tlTQcgcPONhLEBu0qeZAZCZBj2Ct5viOZBYqqu8PXtG2vCftzA1PLKDIz8J0phrAE70VIFlIbfSXLT2tuo8SiUrv47pMZAltD4H55wvCKKfJJVIZBkxvrkQKeHNlSH3LUWaMX1WoDYHfAlGfsEbZAUZBq3zWakSEWF5BFZC7QZCd1AZDZ')
    args = {'fields': 'likes'}
    page = graph.get_object(page_id, **args)
    return page.get('likes', 0)

print get_fb_page_like_count(page_id)