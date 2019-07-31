import unittest
from models import Source, Article


class SourceTest(unittest.TestCase):
  """
  Test behaviour of our class
  """
  def setUp(self):
    """
    set up method that runs before test
    """
    self.new_source = Source("", "", "", "")
    
    def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_source,Source))
    
class ArticleTest(unittest.TestCase):
  """
  Test behaviour of our Article class
  """
  def setUp(self):
    """
    set up method that runs before test
    """
    self.new_article= Article("", "", "", "", "", "", "")
    
    def test_instance(self) :
    '''
    Test if the self.new_source object is an instance of the Source class
    '''
    self.assertTrue(isinstance(self.new_article,Article))
if __name__ == '__main__':
  unittest.main()