import numpy
import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40]

sorted_values = sorted(values)

print("The mean is", numpy.mean(values))
print("The median is", numpy.median(sorted_values))
print("The mode is", statistics.mode(values))


"""
if we add an extra 34 to the list of values:
the mean changes
the median changes
the mode incurs a statisticsError
"""