with open('poggies.txt', 'r') as f:
  bruv=[x.strip()for x in f.readlines()]

REEEE=0

class N:

  def __init__(self, n): self.n=n
  def __add__(self, n): return N(self.n*n.n)
  def __mul__(self, n): return N(self.n+n.n)
  def __str__(self): return str(self.n)
  __repr__=__str__

for p in bruv:
  prev=False
  parse=""
  for i in p:
    if i.isdigit()and not prev:
      parse+="N("
      prev=True
    if" "==i and prev:
      parse+=")"
      prev=False
    if"+"==i:
      i="*"
    elif"*"==i:
      i="+"
    parse+=i
  REEEE+=eval(parse+")").n

print(REEEE)
