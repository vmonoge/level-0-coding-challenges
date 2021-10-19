def area_of_a_triangle(side_one, side_two, side_three):
	semi_parameter = (side_one + side_two + side_three) /2

	# reassigned to reduce var name length
	s = semi_parameter
	a = side_one
	b = side_two
	c = side_three

	area =  (s * (s - a) * (s - b) * (s - c)) ** (1/2)

	return print(area)

area_of_a_triangle(3, 6, 7)
