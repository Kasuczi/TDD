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


