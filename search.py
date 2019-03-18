class Search:
  
  def __init__(self, searchAlgo):
    self.searchAlgo = searchAlgo
  
  def search(self, source, destination, matrix):
    return self.searchAlgo.search(source, destination, matrix)