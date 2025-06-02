#import numpy
import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 45678]

sorted_values = sorted(values)

#print("The mean is", numpy.mean(values))
#print("The median is", numpy.median(sorted_values))

print("The mean is", statistics.mean(values))
print("The median is", statistics.median(sorted_values))
print("The mode is", statistics.mode(values))




"""
mean is by far the central tendency most affected by outliers because even though outliers are out of the ordinary, they have to be computed no matter how absurd their values are, which skews the mean too far from the ordinary values

mode is the central tendency least affected by outliers because due to how out of the ordinary they are, it is rare for more than one occurrence of said outlier to happen, this not affecting the mode

"""
