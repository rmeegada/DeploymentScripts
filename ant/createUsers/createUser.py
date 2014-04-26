try:
	connect(admin_username, admin_password,url)
except WLSTException:
	print '==> Error Connecting to The URL ' + url
	exit()
try:
	atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
	atnr.createUser(username_param,password_param,description)
	print "Created user successfully"
	#adding user to a group
	try:
		atnr.addMemberToGroup(group,username_param)
		print "Done adding a user to group"
	except WLSTException:
		print "Unable to add user to group"
		exit()
		
	try:
		for kv in property.split(";") :
			property,value=kv.split(":")
			atnr.setUserAttributeValue(username_param,property,value)
			print "Added the attribute"+property
	except WLSTException:
		print "Unable to add attribute"
		exit()
except WLSTException:
	print "Unable to create user"
	exit()
