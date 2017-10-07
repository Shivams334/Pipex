# Import the time module, it provides various time-related functions
# Import webbrowser module, which is used to play with our default browser
import time, webbrowser
def websitealarm():
	# First Input: It is the time of the form 'Hours:Minutes:Seconds' that you'll use to set the alarm
	Set_Alarm = raw_input('Set the website alarm as H:M:S:')
	# Second Input: It is the URL that you want to open at the given time
	url = raw_input('Enter the website you want to open:')
	# This is the actual time that we will use to print
	Actual_Time = time.strftime("%I:%M:%S")
	# Constant update to the actual time
	while (Actual_Time != Set_Alarm):
		print ('The time is ' + Actual_Time)
		Actual_Time = time.strftime("%I:%M:%S")
		time.sleep(1)
	# When the actual time is the alarm time
	if (Actual_Time == Set_Alarm):
		print ('You should see your webpage now :-)')
	webbrowser.open(url)