import numpy as np
from scipy import stats

data = np.array([4, 7, 2, 9, 4, 5, 4, 8])

print("საშუალო:", np.mean(data))
print("მოდა:", stats.mode(data, keepdims=True).mode[0])
print("მედიანა:", np.median(data))
print("სტანდარტული გადახრა:", np.std(data))
print("25%-იანი პროცენტილი:", np.percentile(data, 25))
print("75%-იანი პროცენტილი:", np.percentile(data, 75))