#!/usr/bin/env python

import re

class Post(object):
	def __init__(self, line):
		strippedLine = line.split(":")
		unparsedDate = strippedLine[0]
		content = strippedLine[1:]
		
		self.date = self.parseDate(unparsedDate)
		self.content = content

	def parseDate(self, unparsedDate):
		strippedDate = re.sub('[\s+]', '', unparsedDate)
		monthDay, year = strippedDate.split(",")
		monthDay = monthDay.split("/")[5]
		self.year = year.split(".")[0]
		self.month = monthDay[0:3]
		self.day = monthDay[3:]
		parsedDate = self.year

		if self.month == "Jan":
			parsedDate = parsedDate + "01"
		elif self.month == "Feb":
			parsedDate = parsedDate + "02"
		elif self.month == "Mar":
			parsedDate = parsedDate + "03"
		elif self.month == "Apr":
			parsedDate = parsedDate + "04"
		elif self.month == "May":
			parsedDate = parsedDate + "05"
		elif self.month == "Jun":
			parsedDate = parsedDate + "06"
		elif self.month == "Jul":
			parsedDate = parsedDate + "07"
		elif self.month == "Aug":
			parsedDate = parsedDate + "08"
		elif self.month == "Sep":
			parsedDate = parsedDate + "09"
		elif self.month == "Oct":
			parsedDate = parsedDate + "10"
		elif self.month == "Nov":
			parsedDate = parsedDate + "11"
		elif self.month == "Dec":
			parsedDate = parsedDate + "12"		
		else:
			print("Month not recognized.")
			return
		
		# account for days less than 10
		if len(self.day) > 1:
			parsedDate = parsedDate + self.day
		else:
			parsedDate = parsedDate + "0" + self.day
		return parsedDate
		
	def getYear(self):
		return self.year
	
	def getMonth(self):
		return self.month

	def getDay(self):
		return self.day			
		

	def getDate(self):
		return self.date
	
	def getContent(self):
		return self.content
