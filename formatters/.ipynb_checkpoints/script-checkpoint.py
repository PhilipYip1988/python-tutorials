import collections
import datetime
import itertools
import os
import string
import sys

import numpy as np
import pandas as pd

var1 = 'Hello'
var2 = "World"
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, "y": y})
now = datetime.datetime(year=2023, month=12, day=1)
hour = datetime.timedelta(hours=1)
counts = collections.Counter([1, 2, 2, 2, 3, 3])
cycle = itertools.cycle([1, 2, 3])
sys.getsizeof(cycle)
os.environ['USERPROFILE']
num1 = 0xabb4ab8a
