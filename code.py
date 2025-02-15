# Step 1 IMPORT THE MOTIFICATION CLASS FROM THE PLYER MODULE
from plyer import notification
# Step 2 After that you just need to call the notifoy method of this class.
##Parameters:


#title (str) – Title of the notification
#message (str) – Message of the notification
#app_name (str) – Name of the app launching this notification
#app_icon (str) – Icon to be displayed along with the message
#timeout (int) – time to display the message for, defaults to 10
#ticker (str) – text to display on status bar as the notification arrives
#toast (bool) – simple Android message instead of full notification


import time
from player import notification

if __name__=="__main__":

  notification.notify(
    title = "HEADING HERE",
    message="Description Here",

    # displaying time 
    timeout=2

  #waiting time
    time.sleep(7)
