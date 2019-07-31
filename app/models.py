class Source:
  """
  class to define news objects
  """
  def __init__(self, id, name, description, url):
    self.id = id
    self.name = name 
    self.description = description
    self.url = url
    
class Article:
  '''
  class to define Articles Objects
  '''
  def __init__(self, author, title, description, url, urlToImage, publishedAt, content) :
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content    
    