def equal(a, b):
  return (a[0] == b[0] and a[1] == b[1])

def printPath(source, destination, path):
  tmp = []
  current = destination
  i = 0
  while (not equal(current, source)):
    tmp.append(current)
    i += 1
    current = path[current]
  tmp.append(current)
  tmp.reverse()
  return tmp