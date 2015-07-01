#!/usr/bin/python

# 8 - 9 = dark blue		"darkblue"
# 7 - 8 = blue			"mediumblue"
# 6 - 7 = medium blue		"blue"
# 5 - 6 = light blue		"#3366FF"
# 0, 5  = gray			"gray"
# 4 - 5 = light red		"#FF5050"
# 3 - 4 = medium red		"red"
# 2 - 3 = red				"mediumred"
# 1 - 2 = dark red		"darkred"

def colorPicker(scores):
	colors = []
	for score in scores:
		if score == 0 or score == 5:
			colors.append("gray")
		elif score < 5 and score > 4:
			colors.append("#FF5050")
		elif score <= 4 and score > 3:
			colors.append("red")
		elif score <= 3 and score > 2:
			colors.append("mediumred")
		elif score <= 2 and score >= 1:
			colors.append("darkred")
		elif score < 6 and score > 5:
			colors.append("#3366FF")
		elif score <= 7 and score > 6:
			colors.append("blue")
		elif score <= 8 and score > 7:
			colors.append("mediumblue")
		elif score <= 9 and score >= 8:
			colors.append("darkblue")
	return colors