# generate 10 x random decimal values

import random
import decimal

for x in range(10):
  print(float(decimal.Decimal(random.randrange(155, 389))/100))
