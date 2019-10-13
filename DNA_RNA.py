"""
hamming metric
"""

def hamming_metric(dna_c, dna_f):
    """
    Return hamming metric value
    :param dna_c:
    :param dna_f:
    :return:
    """
    metric_value = 0
    for c, f in zip(dna_c, dna_f):
        if c == f:
            metric_value += 1
    return metric_value

def i_am_your_father(fathers, child):
    f_list = []
    for key, father in fathers:
        f_list.append(hamming_metric((father, child)))
    if f_list.count(min(f_list)) > 1:
        raise ValueError('Somebody is chetaing')
    return f_list.index(min(f_list))

if __name__ == '__main__':
    pass
