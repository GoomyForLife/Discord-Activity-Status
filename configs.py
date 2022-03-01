import rpc
import time
from time import mktime

print("========================================")
print("Discord Activity Status by GoomyForLife"
print("========================================")
client_id = ''  # Your Discord Application's Client ID
rpc_client = rpc.DiscordIpcClient.for_platform(client_id) #Sends the client to the Remote Procedure Call
print("The Remote Procedure Call connection is active.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            #Your Application Name will be on the first line of your activity status.
            "state": "",  # This will be on the third line of your activity status.
            "details": "",  # This will be on the second line of your activity status.
            "assets": {
                "small_text": "",  #This will be the text when you hover the small image
                "small_image": "",  # Insert the image key of the image you uploaded here.
                "large_text": "",  #This will be the text when you hover the large image
                "large_image": ""  # Insert the image key of the image you uploaded here.
            }
        }
    rpc_client.set_activity(activity)
    time.sleep(900)
