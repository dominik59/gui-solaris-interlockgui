class Base_connection(object):
    def __init__(self,model):
      #if not '_instancja' in type.__dict__:
        #type._instancja = object.__new__(type)
	#return type._instancja
    	try:
      		return PyTango.DeviceProxy(model)
    	except PyTango.DevFailed, e:
      		print 'Prepare Model ---> Received a DevFailed exception:',e
		
