print "Welcome to Wage Calculator V0"
wage = raw_input("Input your hourly wage: $")
float(wage)
perhour = raw_input("Input how many hours you work in a single day: ")
float(perhour)
days = raw_input("Input how many days your work a week: ")
float(days)
print "\n" * 100
perday = float(wage) * float(perhour)
float(perday)
perweek = float(perday) * float(days)
float(perweek)
permonth = float(perweek) * 4
float (permonth)
peryear = float(permonth) * 12
float(peryear)


print "With a per hourly wage of $%s, you gain:" % (wage)
print "                  $%s Per day." % (perday)
print "                  $%s Per Week." % (perweek)
print "                  $%s Per Month." % (permonth)
print "                  $%s Per Year." % (peryear)
raw_input("Press Enter To Close.")
