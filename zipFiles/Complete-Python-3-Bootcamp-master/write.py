import scipy
from scipy import special
from scipy import intigrade
b = scipy.intigrade.quad(lambda x:special.exp10(x),0,1)
print(b)