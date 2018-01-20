def dna_substr(s, t):
	"""
	(str, str) -> [int]

	Takes in two DNA strings s and t (each of length at most 1 kbp)
	Returns a list of integers representing all locations of t as a substring of s

	>>> dna_substr("GATATATGCATATACTT", "ATAT")
	[2, 4, 10]

	"""

	result = []
	trim = 0

	if s.find(t) == -1:
		return result
	
	while len(s) > len(t):
		if s.find(t) == -1:
			break
		next_index = s.find(t) + 1
		result.append(next_index + trim);
		s = s[next_index::]
		trim += next_index

	return result
	

