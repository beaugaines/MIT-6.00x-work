def radiationExposure(start, stop, step):

  '''fcn to yield radiation exposure at a given point x
  in the radiation exposure curve - as determined by
  the half life of Cobalt-60'''

  def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


  # my own range fcn - to allow the use of fractional stepping

  def myRange(x, y, step):
    while x < y:
      yield x
      x += step


  totalDose = 0


  # iterate over range in steps, accumulate deadly ionizing radiation, and
  # report the damage

  for x in myRange(start, stop, step):
    d = (f(x) * step)
    totalDose += d

  return totalDose
