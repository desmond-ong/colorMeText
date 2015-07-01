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
	for score in scores:
		if score == 0 or score == 5:
			return "gray"
		elif score < 5 and score > 4:
			return "#FF5050"
		elif score <= 4 and score > 3:
			return "red"
		elif score <= 3 and score > 2:
			return "mediumred"
		elif score <= 2 and score >= 1:
			return "darkred"
		elif score < 5 and score > 6:
			return "#3366FF"
		elif score <= 6 and score > 7:
			return "blue"
		elif score <= 7 and score > 8:
			return "mediumblue"
		elif score <= 8 and score >= 9:
			return "darkblue"