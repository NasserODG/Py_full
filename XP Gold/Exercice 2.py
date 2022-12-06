#Ask the user to input a month (1 to 12).
#Display the season of the month received:

month = input("Enter the month between Jan-Dec (1-12)")

if month in ('December', 'January', 'February', 12, 1, 2):
	season = 'Winter'
if month in ('March', 'April', 'May', 3, 4, 5):
	season = 'Spring'
if month in ('June', 'July', 'August', 6, 7, 8):
	season = 'Summer'
if month in ('September', 'October', 'November', 9, 10, 11):
	season = 'Autumn'

print("Season is ", season)