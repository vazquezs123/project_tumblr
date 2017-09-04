#!/usr/bin/python

for i in range(1,51):
	file = open('source_code/' + str(i) + '.txt')
	# stores individual individual posts to write to file by post date

	preDate = ""
	count = 0
	# get each line in file
	for line in file: 
		if "is_regular" in line or "is_conversation" in line:
			# get date
			date = line.split('post_date\">')
			if len(date) > 1:
				date = date[1].split('<')
			else:
				date = date[0].split('<')
			date = date[0] + ".txt"
			if date == preDate:
				date = date + "_" + str(count) + ".txt"
				count = count + 1
			preDate = date
			with open(date, "w") as outFile:
				outFile.write(line)
