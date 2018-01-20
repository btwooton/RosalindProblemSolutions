def expected_offspring(c1, c2, c3, c4, c5, c6):
	"""
	(int, int, int, int, int, int) -> float

	Takes in 6 integer numbers representing the number of couples
	in a population containing a particular genotype

	The genotypes represented by each integer are as follows:

	c1 : AA-AA
	c2 : AA-Aa
	c3 : AA-aa
	c4 : Aa-Aa
	c5 : Aa-aa
	c6 : aa-aa

	return: The expected number of offspring for the population

	assumption: Each couple has exactly two offspring
	
	"""
	prob_c1 = 1
	prob_c2 = 1
	prob_c3 = 1
	prob_c4 = 0.75
	prob_c5 = 0.5
	prob_c6 = 0

	result = 0

	for i in range(1, c1 + 1):
		result = result + prob_c1 * 2
	
	for i in range(1, c2 + 1):
		result = result + prob_c2 * 2
	
	for i in range(1, c3 + 1):
		result = result + prob_c3 * 2

	for i in range(1, c4 + 1):
		result = result + prob_c4 * 2

	for i in range(1, c5 + 1):
		result = result + prob_c5 * 2
	
	for i in range(1, c6 + 1):
		result = result + prob_c6 * 2

	return result


