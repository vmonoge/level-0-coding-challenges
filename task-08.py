def number_to_time(number):
    hours = number // 60
    minutes = number - hours * 60

    if hours == 0 or hours > 1:
        hour_name = f"{hours} hours"
    else:
	hour_name = f"{hours} hour"

    if minutes == 0 or minutes > 1:
        minute_name = f"{minutes} minutes"
    else:
        minute_name = f"{minutes} minute"

    return print(f"{hour_name}, {minute_name}")

number_to_time(0)
number_to_time(60)
number_to_time(61)
number_to_time(62)
number_to_time(120)
number_to_time(121)
number_to_time(122)
