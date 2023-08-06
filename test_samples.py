def inc(a):
  return a+1

def sum(a, b):
  return a+b

def sub(a, b):
  return a-b

def div(a, b):
  return a

def test_answer():
  assert inc(3) == 4
  assert sum(2,7) == 9
  assert sub(10,5) == 5
  assert div(70, 10) == 7
