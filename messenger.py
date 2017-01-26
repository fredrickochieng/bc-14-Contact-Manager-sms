

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# importation from the provided sms gateway file




def send_message(tonumber, message):
	username = "fredrickochieng"
	apikey   = "f1f420c63e231c9e7c3713c9e2e010419973a8f688cf67f4c8357b3681eedc60"
	to      = tonumber
	message = message
	gateway = AfricasTalkingGateway('fredrickochieng', 'f1f420c63e231c9e7c3713c9e2e010419973a8f688cf67f4c8357b3681eedc60')
	try:
		results = gateway.sendMessage(tonumber,message)
		for recipient in results:
			print ('tonumber=%s;status=%s;messageId=%s;cost=%s') % (recipient['number'],
	                                                            recipient['status'],
	                                                            recipient['messageId'],
	                                                            recipient['cost'])
	except AfricasTalkingGatewayException as e:
	    print ('Encountered an error while sending: %s' )% str(e)

	
if __name__ == '__main__':
	send_message("0702006545",'hi')