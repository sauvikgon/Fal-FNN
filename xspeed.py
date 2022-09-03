import os
import subprocess
import re

#XSpeed-plan must be installed in this directory.

def setDimesion(xspeed_cmd):
	state = os.getcwd()
	os.chdir(str(os.getcwd()) + "/XSpeed-plan/Dim")
	output = str(subprocess.run(xspeed_cmd, capture_output=True, shell=True))
	#print(output)
	os.chdir(state)
def set_initial(inputs,xspeed_cmd):
	config_dir = xspeed_cmd.split()[4]
	config_file = open(config_dir,"a+")
	#config_file.write("Atanu")
	config_file.seek(0)
	#initial_exp = []
	initial_loc = []
	replacable_line = ""
	for line in config_file.readlines():
		if(line.find("initially") == 0):
			#print(line)
			replacable_line = line
			initial_exp = str(line).split('"')[1].split('&')
			for loc in range(len(initial_exp)):
				if (initial_exp[loc].find("loc(") != -1):
					#print(initial_exp[loc])
					initial_loc = initial_exp[loc].split('==')
	dim_file = open("../Dim/dimension")
	dimline = dim_file.readline().split()
	dim_file.close()
	#print(initial_loc)
	#print(dimline)
	#print(inputs)
	#config_file.write('initially = "' + initial_loc[0].replace(" ","") + "=="+ initial_loc[1].replace(" ",""))
	replace='initially = "' + initial_loc[0].replace(" ","") + "=="+ initial_loc[1].replace(" ","")
	for i in range(len(dimline)):
		replace=replace+" & " + dimline[i] + "==" + str(inputs[i])
	replace=replace+'"'+"\n"
	print(replace)
	#config_file.write('"\n')
	config_file.seek(0)
	data = config_file.read()
	#print(data)
	data = data.replace(replacable_line,replace)
	#print(data)
	config_file.close()
	config_file = open(config_dir,"w")
	config_file.write(data)
	config_file.close()
	#print(os.getcwd())
def simulate(inputs,xspeed_cmd):
	#print(os.getcwd())
	setDimesion(xspeed_cmd)
	#print(os.getcwd())
	os.chdir(str(os.getcwd()) + "/XSpeed-plan/build")
	set_initial(inputs,xspeed_cmd)
	output1 = str(subprocess.run(xspeed_cmd, capture_output=True, shell=True))
	#print(output1)
	violated = "Number of violated trajectories:"
	vio_traj = output1.find(violated)
	vio_traj_start = int(vio_traj)+len(violated)+0
	vio_traj_end = int(vio_traj)+len(violated)+16
	vio_traj = output1[vio_traj_start:vio_traj_end];
	vio_traj = re.sub("[^\d\.]", "", vio_traj)
	#print(vio_traj)
	if (int(vio_traj) > 0):
		return True
	else:
		return False
