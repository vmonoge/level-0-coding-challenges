def number_to_time(number):
	hours = number // 60
	minutes = number - hours * 60

	if hours == 0 or hours > 1:
		hour_output = f"{hours} hours"
	else:
		hour_output = f"{hours} hour"

	if minutes == 0 or minutes > 1:
		minute_output = f", {minutes} minutes"
	else:
		minute_output = f", {minutes} minute"

	return print(hour_output + minute_output)

number_to_time(0)
number_to_time(60)
number_to_time(61)
number_to_time(62)
number_to_time(120)
number_to_time(121)
number_to_time(122)
