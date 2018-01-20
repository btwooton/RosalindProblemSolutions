def probability_dominant_offspring(k, m, n):
    """
    Takes in three positive integers representing a population
    containing k + m + n organisms: k individuals are homozygous
    dominant for a factor, m are heterozygous, and n are homozygous
    recessive for the factor

    Returns: The probability that two randomly selected mating organisms
    will produce an individual possessing a dominant allele
    """

    total_population = k + m + n
    p_select_dominant = k / total_population
    p_select_hetero = m / total_population
    p_select_recessive = n / total_population

    p_select_dominant_succ = (k / total_population) * ((k - 1) / (total_population - 1))
    p_select_hetero_succ = (m / total_population) * ((m - 1) / (total_population - 1))
    p_select_recessive_succ = (n / total_population) * ((n - 1) / (total_population - 1))
    p_select_dominant_heter = (k / total_population) * (m / (total_population - 1))
    p_select_dominant_recess = (k / total_population) * (n / (total_population - 1))
    p_select_heter_recess = (m / total_population) * (n / (total_population - 1))

    p_offspring_dd = 1
    p_offspring_dh = 1
    p_offspring_dr = 1
    p_offspring_hh = 0.75
    p_offspring_hr = 0.5
    p_offspring_rr = 0

    result = (
            p_select_dominant_succ + 
            2 * p_select_dominant_heter + 
            2 * p_select_dominant_recess +
            p_select_hetero_succ * p_offspring_hh +
            2 * p_select_heter_recess * p_offspring_hr
            )

    return result

