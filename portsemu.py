import netifaces

portinfo=dict()
maxport = 0
commandstorun=[]
explain=[]
with open("/etc/cumulus/ports.conf") as f:
	for line in f:
		line=line.rstrip('\n')
		#print(line)
		if line[0:1] != '#' and len(line)>0:
			#print('lll:' + line + 'fff')
			(numb, content)=line.split('=')
			numb=int(numb)
			#print(numb + '::' + content)
			maxport=max(maxport,numb)
			portinfo[numb]=content
			
offsetstart=maxport +1 
#print (maxport)
interface_list = netifaces.interfaces()

#print(interface_list)


for key in portinfo:
	#print(portinfo[key][0:2])
	portn='swp'+str(key)
	if portinfo[key][0:2] == '4x':
		#print(portinfo[key])# split
		if portn in interface_list:
			#need to do split
			if maxport>32:
				key = key - 48
			command='ip link set ' + portn + ' down'
			commandstorun.append(command)
			command='ip link set ' + portn + ' name ' + portn + 's0'
			commandstorun.append(command)
			explain.append("Port " + portn + " is now " + portn + 's0')
			offset=((key - 1) *3 ) + offsetstart
			command='ip link set swp' + str(offset) + ' down'
			commandstorun.append(command)
			command='ip link set swp' + str(offset) + ' name ' + portn + 's1'
			commandstorun.append(command)
			explain.append("Port " + str(offset) + " is now " + portn + 's1')
			offset=offset+1
			command='ip link set swp' + str(offset) + ' down'
			commandstorun.append(command)
			command='ip link set swp' + str(offset) + ' name ' + portn + 's2'
			commandstorun.append(command)
			explain.append("Port " + str(offset) + " is now " + portn + 's2')
			offset=offset+1
			command='ip link set swp' + str(offset) + ' down'
			commandstorun.append(command)
			command='ip link set swp' + str(offset) + ' name ' + portn + 's3'
			commandstorun.append(command)
			explain.append("Port " + str(offset) + " is now " + portn + 's3')
			x=1
	else:
		# not split
		x=1
		ports=portn + 's0'
		if ports in interface_list:
			# port is split and it shouldnt be
			if maxport>32:
				key = key - 48
			command='ip link set ' + portn + 's0 down'
			commandstorun.append(command)
			command='ip link set ' + portn + 's0' + ' name ' + portn
			commandstorun.append(command)
			offset=((key - 1) *3 ) +  offsetstart
			command='ip link set ' + portn + 's0 down'
			commandstorun.append(command)
			command='ip link set ' + portn + 's1' + ' name swp' + str(offset)
			commandstorun.append(command)
			offset=offset+1
			command='ip link set ' + portn + 's0 down'
			commandstorun.append(command)
			command='ip link set ' + portn + 's2' + ' name swp' + str(offset)
			commandstorun.append(command)
			offset=offset+1
			command='ip link set ' + portn + 's0 down'
			commandstorun.append(command)
			command='ip link set ' + portn  + 's3' + ' name swp' + str(offset)
			commandstorun.append(command)
		
for a in commandstorun:
	print('sudo ' + a)

print(' ')
print(' explaination ')
for a in explain:
	print('' + a)


#print(commandstorun)


