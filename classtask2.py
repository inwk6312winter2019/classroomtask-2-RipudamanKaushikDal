class IP():
	address=[192,168,0,1]
	netmask=[255,255,255,0]
ip=IP()

def get_addr():
	print('Network : {0}.{1}.{2}.{3}'.format(ip.address[0],ip.adress[1],ip.address[2],ip.address[3])) 
get_addr()
