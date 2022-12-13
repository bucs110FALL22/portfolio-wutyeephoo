class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = (0, x)
    self.y = (0, y)
    self.height = (0, h)
    self.width = (0, w)

  def __str__(self):
    print("x: " + self.x + "y: " + self.y + "width: " + self.w + "height: " + self.h)