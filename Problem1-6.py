import CalibrationClasses as Cls
import calibrationclasses2 as cls2
import CalibrationSettings as CalibSets

import scr.FigureSupport as Fig
from enum import Enum
import numpy as np
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as Stat
from scipy.stats import binom



#Problem2
print('Problem2')
print('Binomial Distribution with p = q, N = N')

#Problem3
print('Problem3')
print(binom.pmf(400, 573,0.5))

# create a calibration object
calibration = Cls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

print('Problem4')
# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))


print("Problem5")
# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)


# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))


print('Problem 6')

calibration2 = cls2.Calibration()
# sample the posterior of the mortality probability
calibration2.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration2.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

calibrated_model2 = cls2.CalibratedModel('CalibrationResults2.csv')
# simulate the calibrated model
calibrated_model2.simulate(CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)


# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model2.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))



print('Both of the CI of the estimated annual mortality probability and in the PI of the mean survival time become narrower.')


