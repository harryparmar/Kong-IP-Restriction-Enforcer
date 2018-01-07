from slackclient import SlackClient


def slack(token, channel_id, message): 
	
   slack_client = SlackClient(token)



   
   slack_client.api_call( 
         "chat.postMessage", 
         channel=channel_id, 
         text=message, 
         username='Kong-IP-Restriction-Enforcer', 
         icon_emoji=':getkong:' 
   )