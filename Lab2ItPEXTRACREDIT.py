"""
Lab 2 Extra Credit
Sucheer Maddury
6/30/2021
Run Starting & Ending Time Calculator (Military Time)
Calculates when the run will end in hours, minutes, then seconds on a 24 hour day, after recieving use input about the starting time of the run.
NOTES: If the number of any of the hours, minutes, or seconds is a single digit, that represents the units digit, ex. 10:20:9 = 10:20:09
"""

hour_start=eval(input("Enter Starting Hour: "))
minute_start=eval(input("Enter Starting Minute: "))
start_time_in_seconds=(hour_start*3600)+(minute_start*60)
easy_pace_in_seconds=(8*60)+15
tempo_pace_in_seconds=(7*60)+12
running_total_time_in_seconds=(3*tempo_pace_in_seconds)+(2*easy_pace_in_seconds)
ending_total_time_in_seconds=start_time_in_seconds+running_total_time_in_seconds
hourhand_ending_time=(ending_total_time_in_seconds%86400)//3600
minutehand_ending_time=(ending_total_time_in_seconds%3600)//60
secondhand_ending_time=ending_total_time_in_seconds%60
print("You will finish at",str(hourhand_ending_time)+":"+str(minutehand_ending_time)+":"+str(secondhand_ending_time))

"""
RESULT:
____________________________________________________________________________________________________________________________________________________________________________________
PS C:\Windows\System32\work> & C:/Users/sumad/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/sumad/Lab2ItPEXTRACREDIT.py
Enter Starting Hour: 6
Enter Starting Minute: 52
You will finish at 7:30:6
____________________________________________________________________________________________________________________________________________________________________________________
"""