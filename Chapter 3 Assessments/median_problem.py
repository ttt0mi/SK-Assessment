#import numpy
import statistics

values = [9, 11, 60, 22, 35, 70, 17, 22, 35, 50, 22, 40]


sorted_values = sorted(values)

#print("The mean is", numpy.mean(values))
#print("The median is", numpy.median(sorted_values))

print("The mean is", statistics.mean(values))
print("The median is", statistics.median(sorted_values))
print("The mode is", statistics.mode(values))


"""
i noticed no problem with the median
"""

