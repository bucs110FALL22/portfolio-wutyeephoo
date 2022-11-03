class Graph:

  def_init_(self):
    self.points = []
    self.plotter = turtle.Turtle()

  def add_point(self, spoint):
    self.points.append(spoint)

  def plot(self):
    for p in self.points:
      self.plotter.color(p.color)
      self.plotter.goto(p.x, p.y)
      self.plotter.dot(1, p.color)