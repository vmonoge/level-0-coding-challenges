def area_of_a_triangle(side_one, side_two, side_three):
	semi_parameter = (side_one + side_two + side_three) /2

	# reassigned to reduce var name length
	s = semi_parameter
	a = side_one
	b = side_two
	c = side_three

	# Heron's Formula for triangle area calculation
	area =  (s * (s - a) * (s - b) * (s - c)) ** (1/2)

	return print(f"Area of your triangle: {area} sqaure units")

area_of_a_triangle(3, 6, 7)
