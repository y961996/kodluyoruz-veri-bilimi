import itertools

def flatten(l):
  if type(l) is list:
    return [x for i in l for x in flatten(i)]
  return [l]

def reverse(l):
  if type(l) is list:
    l.reverse()
    return [reverse(i) for i in l]
  return l

if __name__ == "__main__":
  input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
  output1 = [1,'a','cat',2,3,'dog',4,5]

  input2 = [[1, 2], [3, 4], [5, 6, 7]]
  output2 = [[7, 6, 5], [4, 3], [2, 1]]

  ret1 = flatten(input1)
  print(ret1)
  print(ret1 == output1)

  ret2 = reverse(input2)
  print(ret2)
  print(ret2 == output2)
