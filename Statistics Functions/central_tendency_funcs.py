from central_dispersion_funcs import *
from collections import defaultdict


def arithmetic_mean(values):
    values_len = len(values)
    values_sum = sum(values)
    return values_sum / values_len


def get_median(values):
    values_len = len(values)
    if values_len % 2:
        median_operand = (values_len + 1) // 2
        median = values[median_operand - 1]
        return median
    else:
        median_operand_1 = values_len // 2
        median_operand_2 = median_operand_1 + 1
        mean_of_medians = (values[median_operand_1 - 1] + values[median_operand_2 - 1]) / 2
        return mean_of_medians


def get_mod(values):
    count_dict = defaultdict(lambda: 0)
    for value in values:
        count_dict[value] += 1

    return max(count_dict, key=count_dict.get)


def main():
    m_list = sorted([8, 6, 4, 9, 72, 15, 6, 2])
    print(m_list)
    print(get_mod(m_list))


if __name__ == "__main__":
    main()
