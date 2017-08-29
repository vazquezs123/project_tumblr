import os

# convert date to format yyyymmddpp
# yyyy = year
# mm = month
# dd = day
# pp = post number
def convertDate(date):
	# get month
	month = date[0:3]
	day = date[3:5].strip(',')
	year = date.split(',')[1].split('.')[0]
	
	# convert date to integer value
	date_int = str(year)
	
	if month == 'jan':
		date_int = date_int + '01'
	elif month == 'feb':
		date_int = date_int + '02'
	elif month == 'mar':
		date_int = date_int + '03'
	elif month == 'apr':
		date_int = date_int + '04'
	elif month == 'may':
		date_int = date_int + '05'
	elif month == 'jun':
		date_int = date_int + '06'
	elif month == 'jul':
		date_int = date_int + '07'
	elif month == 'aug':
                date_int = date_int + '08'
        elif month == 'sep':
                date_int = date_int + '09'
        elif month == 'oct':
                date_int = date_int + '10'
        elif month == 'nov':
                date_int = date_int + '11'
	elif month == 'dec':
		date_int = date_int + '12'
	else:
		print("invalid month")
		return -1
	if len(day) < 2:
		day = '0' + day	
	date_int = date_int + day
	return date_int



file='all_posts.txt'
date_post_map = {}
with open(file) as f:
	for line in f:
		# get date:post map
		date = line.split(':')[0]
		date = date.replace(" ", "")
		date = date.lower()
		print(date)
		date = convertDate(date)
		post = line.split(':')[1:]
		post_num = ''
		if '_' in line:
			line = line.strip('^')
			post_num = line.split('_')[1]
			post_num = post_num.split('.')[0]
			if len(str(post_num)) < 2:
				post_num = '0' + post_num
		else:
			post_num = '00'
		#print(" ... " + post_num)
		date = date + post_num
		print(date)
		date_post_map[date] = post
