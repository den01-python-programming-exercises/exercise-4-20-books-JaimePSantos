class Book:
  def __init__(self,title,pages,pubYear):
    self.title = title
    self.pages = pages
    self.pubYear = pubYear
  
  def __str__(self):
    return self.title + ", " + self.pages + " pages, " + self.pubYear