
import urllib.request, json
from .models import Source, Article


#api key
api_key = None

#base url
base_url = None

#article url
article_url = None

def configure_request(app):
  global api_key, base_url, article_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config["NEWS_API_BASE_URL"]
  article_url = app.config['ARTICLE_URL']

def get_sources():
  """
  gets the json response to our url request
  """
  get_sources_url = base_url.format('0918c87ec2ab491db72f7f3d897c180b')
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    sources_results = None
    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)
      
  return sources_results
def process_results(sources_list):
  """
  processes sources result and transform them to a list of objects
  """
  sources_results = []
  for source_item in sources_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    
    source_object = Source(id, name, description, url)
    sources_results.append(source_object)
  return sources_results
def get_article():
  """
  get json response to our url request
  """
  get_article_url = article_url.format('0918c87ec2ab491db72f7f3d897c180b')
  
  with urllib.request.urlopen(get_article_url) as url:
    get_article_data = url.read()
    get_article_response = json.loads(get_article_data)
    
    article_results = None
    
    if get_article_response['articles']:
      article_results_list = get_article_response['articles']
      article_results = process_article_results(article_results_list)
  return article_results

def process_article_results(article_results_list):
  article_results = []
  
  for article in article_results_list:
    author = article.get('author')
    title = article.get('title')
    description = article.get('description')
    url = article.get('url')
    urlToImage = article.get('urlToImage')
    publishedAt = article.get('publishedAt')
    content = article.get('content')
    
    article_object = Article(author, title, description, url, urlToImage, publishedAt, content)
    article_results.append(article_object)
    
  return article_results