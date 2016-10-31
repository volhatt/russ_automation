#return digtionary


def toDict(file):
    with open(file) as f:
        # using python dictionary comprehension
        d_temp = dict([line.split('=') for line in f])
    return d_temp
"""
finction takes parameter file, splits by "=" sign
every string and return digtionary,
where keys are left columns and values are right column
"""


"""
    d_temp = {}
    
    with open(file) as f:
        for line in f:
            key,val = line.split('=')
            d_temp[key] = val
"""
    



file = 'C:\\test\\russian\\file_prop.txt'
test = toDict(file)
for i in test:
    print(i+' : '+test[i])
    
"""
for 2.7 python
with open('infile.txt') as f:
  {int(k): v for line in f for (k, v) in (line.strip().split(None, 1),)}
  """
