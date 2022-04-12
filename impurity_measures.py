from math import log2
def compute_entropy(class_frequencies):
  '''Function to compute the entropy when different class along with the 
     frequency of each class is given.

     Parameters
     ----------
      class_frequencies : list
        Contains frequency of unique labels
     Returns
     ---------
     entropy : float
        Entropy for the given input parameters.
  '''
  try: 
    entropy = 0
    if 0 in class_frequencies:
      return entropy
    total = sum(class_frequencies)
    for x in class_frequencies:
      p_k = x/total
      entropy -= p_k * log2(p_k)
    return entropy
  except ZeroDivisionError:
    return 0


def compute_gini(class_frequencies):
  '''Function to compute the gini index.

     Parameters
     ----------
      class_frequencies : list
        Contains frequency of unique labels
     Returns
     ---------
     gini : float
        gini index for the given data.
  '''
  try:
    total = sum(class_frequencies)
    p_i = sum((x/total)**2 for x in class_frequencies)
    return 1-p_i

  except ZeroDivisionError:
    return 0
