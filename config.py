import os

class Config:
  """
  General config parent class
  """
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  ARTICLE_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
  """
  Production configuration child class
  Args:
    Config : The parent configuration class with general configuration settings
  """
  pass
class DevConfig(Config):
  """
  Development configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  """
  DEBUG =  True
config_options = {
  'development': DevConfig,
  'production' : ProdConfig
}
    