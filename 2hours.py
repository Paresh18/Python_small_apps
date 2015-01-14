#This is a small app which will run this video after every 2 hours for 3 times in a day.

#importing modules
import webbrowser
import time

total_breaks = 3
break_count = 0

print("the program started on " +time.ctime())
#this will run this video after every two hours
while(break_count < total_breaks):
     time.sleep(2*60*60)
     webbrowser.open("https://www.youtube.com/watch?v=VJQtNxyKJhQ")
     
     break_count =break_count + 1

