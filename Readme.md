Firstly we need the download library
** IMPORTANT :** Plyer module is used to acces the features of the hardware. This module does not comes built-in with Python. We need to install it externally. To install this module type the command : pip install plyer
 # if you use macOS YOU NEED DOWNLOAD ANOTHER LIBRARY ---- **pip install pyobjus pyjnius**



#title (str) – Title of the notification
#message (str) – Message of the notification
#app_name (str) – Name of the app launching this notification
#app_icon (str) – Icon to be displayed along with the message
#timeout (int) – time to display the message for, defaults to 10
#ticker (str) – text to display on status bar as the notification arrives
#toast (bool) – simple Android message instead of full notification
