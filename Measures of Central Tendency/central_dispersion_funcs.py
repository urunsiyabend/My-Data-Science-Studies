import math
from central_tendency_funcs import *


def get_range(values):
    return max(values)- min(values)


def standard_deviation(values):
    mean = arithmetic_mean(values)
    values_len = len(values)
    dvt_sum = 0
    for value in values:
        dvt_sum += (value - mean) ** 2
    std_dvt = math.sqrt(dvt_sum / values_len)
    return std_dvt


def get_variation(values):
    return standard_deviation(values) ** 2


def pearson_skewness(values):
    mean = arithmetic_mean(values)
    std_dvt = standard_deviation(values)
    median = get_median(values)
    skw = 3 * (mean - median) / std_dvt
    return skw


def get_mean_moment(values, moment):
    mean = arithmetic_mean(values)
    values_len = len(values)
    mmt_sum = 0
    for value in values:
        mmt_sum += (value - mean) ** moment

    return mmt_sum / values_len


def get_kurtosis_coefficient(values):
    fourth_moment = get_mean_moment(values, 4)
    std_dvt_4 = standard_deviation(values) ** 4
    return fourth_moment / std_dvt_4


def main():
    m_list = sorted([12, 15, 20, 30, 45, 22])
    print(m_list)
    print(get_kurtosis_coefficient(m_list))


if __name__ == main():
    main()
