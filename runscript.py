import os
import subprocess
import re
import numpy as np
import xspeed
import dnnf
import time
from prettytable import PrettyTable

#NOTE:
	



example=[]
running_directory = os.getcwd()

#for NAV_3_2
#example.append(['NAV_3_2_P1','runlim -s 4096 -r 600 dnnf NAV_3_2/P1_loc_4_unsafe/property_1_loc_4_unsafe.py --network N NAV_3_2/NAV_3_2_T10_D10_1L.onnx --save-violation violation', './XSpeed-plan -m ../testcases/NAV_3_2.xml -c ../testcases/NAV_3_2.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=4 & 1*x1>=1 & 1*x1<=2 & 1*x2>=0 & 1*x2<=1" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_2_P2','runlim -s 4096 -r 100 dnnf NAV_3_2/P2_loc_7_unsafe/property_2_loc_7_unsafe.py --network N NAV_3_2/NAV_3_2_T10_D10_1L.onnx --save-violation violation', './XSpeed-plan -m ../testcases/NAV_3_2.xml -c ../testcases/NAV_3_2.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=7 & 1*x1>=2 & 1*x1<=3 & 1*x2>=0 & 1*x2<=1" -e simu --simu-algo 1 --simu-init-points 1'])


#example.append(['NAV_3_2_P3','runlim -r 20 dnnf NAV_3_2/P3_loc_9_safe/property_3_loc_9_safe.py --network N NAV_3_2/N_3_2_T10_D10_1L.onnx --save-violation violation', './XSpeed-plan -m ../testcases/NAV_3_2.xml -c ../testcases/NAV_3_2.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=9 & 1*x1>=2 & 1*x1<=3 & 1*x2>=2 & 1*x2<=3" -e simu --simu-algo 1 --simu-init-points 1'])

#for NAV_3_3
#example.append(['NAV_3_3_P1', 'runlim -s 4096 -r 100 dnnf NAV_3_3/P1_loc_7_unsafe/property_1_loc_7_unsafe.py --network N NAV_3_3/NAV_3_3_T10_D10_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_3.xml -c ../testcases/NAV_3_3.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=7 & 1*x1>=0 & 1*x1<=1 & 1*x2>=2 & 1*x2<=3 & 1*x3>=0 & 1*x3<=1" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_3_P2', 'runlim -s 4096 -r 100 dnnf NAV_3_3/P2_loc_8_unsafe/property_2_loc_8_unsafe.py --network N NAV_3_3/NAV_3_3_T10_D10_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_3.xml -c ../testcases/NAV_3_3.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=8 & 1*x1>=0 & 1*x1<=1 & 1*x2>=2 & 1*x2<=3 & 1*x3>=1 & 1*x3<=2" -e simu --simu-algo 1 --simu-init-points 1'])

#example.append(['NAV_3_3_P3', 'runlim -r 300 dnnf NAV_3_3/P3_loc_15_safe/property_3_loc_15_safe.py --network N NAV_3_3/N_3_3_T10_D10_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_3.xml -c ../testcases/NAV_3_3.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=15 & 1*x1>=1 & 1*x1<=2 & 1*x2>=1 & 1*x2<=2 & 1*x3>=2 & 1*x3<=3" -e simu --simu-algo 1 --simu-init-points 1'])

#for Nav3_inst1
#example.append(['NAV_3insta_1_P1' ,'runlim -s 4096 -r 600 dnnf NAV_3Insta_1/P1_loc_6_unsafe/property_1_loc_6_unsafe.py --network N NAV_3Insta_1/NAV3_INSTI1_T10_D3_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/Nav3_inst1.xml -c ../testcases/Nav3_inst1.cfg --time-horizon 10 --time-step 0.01 --depth 3 -o out.txt -v x1,x2 -F "loc=6 & 1*x1>=2 & 1*x1<=3 & 1*x2>=1 & 1*x2<=2" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3insta_1_P2' ,'runlim -s 4096 -r 600 dnnf NAV_3insta_1/P2_loc_5_unsafe/property_2_loc_5_unsafe.py --network N NAV_3insta_1/NAV3_INSTI1_T10_D3_1L.onnx --save-violation violation', './XSpeed-plan -m ../testcases/Nav3_inst1.xml -c ../testcases/Nav3_inst1.cfg --time-horizon 10 --time-step 0.01 --depth 2 -o out.txt -v x1,x2 -F "loc=5 & 1*x1>=1 & 1*x1<=2 & 1*x2>=1 & 1*x2<=2" -e simu --simu-algo 1 --simu-init-points 1'])

#for NAV_3_4
#example.append(['NAV_3_4_P1', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P1_loc_10_unsafe/property_1_loc_10_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 1 -o out.txt -v x1,x2 -F "loc=10 & 1*x1>=0 & 1*x1<=1 & 1*x2>=1 & 1*x2<=2 & 1*x3>=0 & 1*x3<=1 & 1*x4>=0 & 1*x4<=1" -e simu --simu-algo 1 --simu-init-points 1'])
#1*xc2>=-0.5 & 1*xc2<=0.5 &
example.append(['NAV_3_4_P2', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P2_loc_41_unsafe/property_2_loc_41_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 8 -o out.txt -v x1,x2 -F "loc=41 & 1*x1>=1 & 1*x1<=2 & 1*x2>=1 & 1*x2<=2 & 1*x3>=1 & 1*x3<=2 & 1*x4>=1 & 1*x4<=2" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_4_P3', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P3_loc_51_unsafe/property_3_loc_51_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 6 -o out.txt -v x1,x2 -F "loc=51 & 1*x1>=1 & 1*x1<=2 & 1*x2>=2 & 1*x2<=3 & 1*x3>=1 & 1*x3<=2 & 1*x4>=2 & 1*x4<=3" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_4_P4', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P4_loc_61_unsafe/property_4_loc_61_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=61 & 1*x1>=2 & 1*x1<=3 & 1*x2>=0 & 1*x2<=1 & 1*x3>=2 & 1*x3<=3 & 1*x4>=0 & 1*x4<=1" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_4_P5', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P5_loc_68_unsafe/property_5_loc_68_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 9 -o out.txt -v x1,x2 -F "loc=68 & 1*x1>=2 & 1*x1<=3 & 1*x2>=1 & 1*x2<=2 & 1*x3>=1 & 1*x3<=2 & 1*x4>=1 & 1*x4<=2" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_4_P6', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P6_loc_70_unsafe/property_6_loc_70_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=70 & 1*x1>=2 & 1*x1<=3 & 1*x2>=1 & 1*x2<=2 & 1*x3>=2 & 1*x3<=3 & 1*x4>=0 & 1*x4<=1" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_3_4_P7', 'runlim -s 4096 -r 100 dnnf NAV_3_4/P7_loc_71_unsafe/property_7_loc_71_unsafe.py --network N NAV_3_4/NAV_3_4_T10_D15_1L.onnx --save-violation violation','./XSpeed-plan -m ../testcases/NAV_3_4.xml -c ../testcases/NAV_3_4.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=71 & 1*x1>=2 & 1*x1<=3 & 1*x2>=1 & 1*x2<=2 & 1*x3>=2 & 1*x3<=3 & 1*x4>=1 & 1*x4<=2" -e simu --simu-algo 1 --simu-init-points 1'])

#for NAV30
#example.append(['NAV_30_P1', 'runlim -r 600 dnnf NAV_30/P1_loc_532_unsafe/property_1_loc_532_unsafe.py --network N NAV_30/N_30_1000.onnx --save-violation violation','./XSpeed-plan -m ../testcases/30.xml -c ../testcases/30.cfg --time-horizon 10 --time-step 0.01 --depth 2 -o out.txt -v x1,x2 -F "loc=532 & 1*x1>=6 & 1*x1<=7 & 1*x2>=21 & 1*x2<=22" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_30_P2', 'runlim -r 600 dnnf NAV_30/P2_loc_412_unsafe/property_2_loc_412_unsafe.py --network N NAV_30/N_30_1000.onnx --save-violation violation','./XSpeed-plan -m ../testcases/30.xml -c ../testcases/30.cfg --time-horizon 10 --time-step 0.01 --depth 12 -o out.txt -v x1,x2 -F "loc=412 & 1*x1>=11 & 1*x1<=12 & 1*x2>=16 & 1*x2<=17" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_30_P3', 'runlim -s 4096 -r 600 dnnf NAV_30/P3_loc_435_unsafe/property_3_loc_435_unsafe.py --network N NAV_30/N_30_1000.onnx --save-violation violation','./XSpeed-plan -m ../testcases/30.xml -c ../testcases/30.cfg --time-horizon 10 --time-step 0.01 --depth 9 -o out.txt -v x1,x2 -F "loc=435 & 1*x1>=9 & 1*x1<=10 & 1*x2>=17 & 1*x2<=18" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_30_P4', 'runlim -s 4096 -r 600 dnnf NAV_30/P4_loc_436_unsafe/property_4_loc_436_unsafe.py --network N NAV_30/N_30_1000.onnx --save-violation violation','./XSpeed-plan -m ../testcases/30.xml -c ../testcases/30.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=436 & 1*x1>=10 & 1*x1<=11 & 1*x2>=17 & 1*x2<=18" -e simu --simu-algo 1 --simu-init-points 1'])


#for NAV_07
#example.append(['NAV_07_P1', 'runlim -s 4096 -r 100 dnnf NAV_07/P1_loc_208_unsafe/property_1_loc_208_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 10 --time-step 0.01 --depth 10 -o out.txt -v x1,x2 -F "loc=208 & 1*x1>=4 & 1*x1<=5 & 1*x2>=22 & 1*x2<=23" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_07_P2', 'runlim -s 4096 -r 100 dnnf NAV_07/P2_loc_199_unsafe/property_2_loc_199_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 20 --time-step 0.01 --depth 20 -o out.txt -v x1,x2 -F "loc=199 & 1*x1>=3 & 1*x1<=4 & 1*x2>=21 & 1*x2<=22" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_07_P3', 'runlim -s 4096 -r 100 dnnf NAV_07/P3_loc_193_unsafe/property_3_loc_193_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 20 --time-step 0.01 --depth 13 -o out.txt -v x1,x2 -F "loc=193 & 1*x1>=3 & 1*x1<=4 & 1*x2>=20 & 1*x2<=21" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_07_P4', 'runlim -s 4096 -r 100 dnnf NAV_07/P4_loc_181_unsafe/property_4_loc_181_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 20 --time-step 0.01 --depth 15 -o out.txt -v x1,x2 -F "loc=181 & 1*x1>=3 & 1*x1<=4 & 1*x2>=18 & 1*x2<=19" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_07_P5', 'runlim -s 4096 -r 100 dnnf NAV_07/P5_loc_169_unsafe/property_5_loc_169_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 20 --time-step 0.01 --depth 17 -o out.txt -v x1,x2 -F "loc=169 & 1*x1>=3 & 1*x1<=4 & 1*x2>=16 & 1*x2<=17" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['NAV_07_P6', 'runlim -s 4096 -r 100 dnnf NAV_07/P6_loc_163_unsafe/property_6_loc_163_unsafe.py --network N NAV_07/NAV_07_T20_D20_50K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/nav07.xml -c ../testcases/nav07.cfg --time-horizon 20 --time-step 0.01 --depth 18 -o out.txt -v x1,x2 -F "loc=163 & 1*x1>=3 & 1*x1<=4 & 1*x2>=15 & 1*x2<=16" -e simu --simu-algo 1 --simu-init-points 1'])

#for Oscillator
#example.append(['Oscillator' , 'runlim -s 4096 -r 100 dnnf Oscillator/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N Oscillator/Osc_T10_D3_1L.onnx --save-violation violation','./XSpeed-plan  -m ../testcases/FlatFilteredOscillator/Oscillator.xml -c ../testcases/FlatFilteredOscillator/Oscillator.cfg --depth 3 --time-step 0.01 --time-horizon 10 -o out.txt -v p,q -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['F_oscillator_4' , 'runlim -s 4096 -r 100 dnnf OSC_4/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_4/F_OSC_4_T10_D3_10K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/FlatFilteredOscillator/f_osc_4.xml -c ../testcases/FlatFilteredOscillator/f_osc_4.cfg --time-step 0.01 --time-horizon 10 --depth 3 -v p,q -o out.txt -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['F_oscillator_8' , 'runlim -s 4096 -r 100 dnnf OSC_8/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_8/F_OSC_8_T10_D3_10K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/FlatFilteredOscillator/f_osc_8.xml -c ../testcases/FlatFilteredOscillator/f_osc_8.cfg --time-step 0.01 --time-horizon 10 --depth 3 -v p,q -o out.txt -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['F_oscillator_16' , 'runlim -s 4096 -r 100 dnnf OSC_16/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_16/F_OSC_16_T10_D3_10K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/FlatFilteredOscillator/f_osc_16.xml -c ../testcases/FlatFilteredOscillator/f_osc_16.cfg --time-step 0.01 --time-horizon 10 --depth 3 -v p,q -o out.txt -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['F_oscillator_32' , 'runlim -s 4096 -r 100 dnnf OSC_32/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_32/F_OSC_32_T10_D3_10K.onnx --save-violation violation','./XSpeed-plan -m ../testcases/FlatFilteredOscillator/f_osc_32.xml -c ../testcases/FlatFilteredOscillator/f_osc_32.cfg --time-step 0.01 --time-horizon 10 --depth 3 -v p,q -o out.txt -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])
#example.append(['F_oscillator_64' , 'runlim -s 4096 -r 100 dnnf OSC_64/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_64/F_OSC_64_T10_D3_10K.onnx --save-violation violation', './XSpeed-plan -m ../testcases/FlatFilteredOscillator/f_osc_64.xml -c ../testcases/FlatFilteredOscillator/f_osc_64.cfg --time-step 0.01 --time-horizon 10 --depth 3 -v p,q -o out.txt -F "loc=1 & 1*p<=0 & 1*q+0.714286*p>=0" -e simu --simu-algo 1 --simu-init-points 1'])

#for ACC03
#example.append(['ACCS03_1' , 'runlim -s 4096 -r 20 dnnf ACCS03/P1_loc_1_safe/property_1_Loc_1_unsafe.py --network N ACCS03/ACCS03_T5_D7_1L.onnx --save-violation violation ','runlim -r 40 ./XSpeed-plan -m ../testcases/ACCS03/ACCS03.xml -c ../testcases/ACCS03/ACCS03.cfg --time-horizon 5 --time-step 0.1 --depth 9 -o out.txt -v x1,x2 -F "loc=8 & 1*autd201 <= 3" - simu --simu-algo 1 --simu-init-points 1'])



Number_refined = {} # for wwhich purpose i take it?
table_fields = ['Property name','#Experiments', '#Refinements', 'XSpeed_Time', 'Overall_time']
pt = PrettyTable(table_fields)
N = 100 #for taking average falsification time.
for i in range(0,len(example)):
	Number_verified = 0
	Total_verified_xspeed_time = 0
	Total_verified_overall_time = 0
	print('\nrunning '+ example[i][0])
	pt.add_row([example[i][0],"","","",""])
	for how_many in range(N):
		print(how_many)
		start_time = time.time()
		#print(start_time)
		dnnf_cmd = example[i][1]
		xspeed_cmd = example[i][2]
		#print("\n")
		#print(dnnf_cmd)
		#print(os.getcwd())
		refine_counter = 0
		while(True):
			os.chdir(running_directory)
			output = str(subprocess.run(dnnf_cmd, capture_output=True, shell=True))
			#print(output)
			status = output.find("result: sat")
			if(status == -1):
				print("dnnf can't find a counterexample!")
				if(refine_counter != 0):
					dnnf.setInitialProperty(dnnf_cmd)
				break;
			else:
				print("dnnf: falsified")
				res = " result:"
				res_str = output.find(res)
				res_start = int(res_str)+len(res)+0
				res_end = int(res_str)+len(res)+4
				result = output[res_start:res_end];
				#print(result)
				res2 = "falsification time:"
				res2_str = output.find(res2)
				res2_start = int(res2_str)+len(res2)+0
				res2_end = int(res2_str)+len(res2)+16
				result2 = output[res2_start:res2_end];
				result2 = re.sub("[^\d\.]", "", result2)
				#print(result2)
				print(example[i][0] +" is falisifyied with status ("+ result + " ) in time "+ result2)
				#dnnf returns the Input and stored it into the list inputs as per the dimension.
				Input = np.load("violation.npy")
				#print(Input)
				inputs = Input.tolist()[0]
				#print(inputs[4])
				os.remove("violation.npy")


				#call XSpeed to find a trajectory from the returned inputs
				xspeed_time = time.time()
				isReach =  xspeed.simulate(inputs,xspeed_cmd)
				#print(isReach)
				if (isReach):
					print("Found a trajectory after", refine_counter, "refinement in", (time.time() - xspeed_time))
					pt.add_row(["",how_many+1,refine_counter,(time.time() - xspeed_time), (time.time() - start_time)])
					Total_verified_xspeed_time += (time.time() - xspeed_time)
					Total_verified_overall_time += (time.time() - start_time)
					verified_time = time.time()
					#print(verified_time)
					print("Total time spend to falsify by dnnf and verified by xspeed is", (verified_time - start_time))
					Number_verified = Number_verified + 1
					os.chdir(running_directory)
					if(refine_counter != 0):
						dnnf.setInitialProperty(dnnf_cmd)
					break;
				else:
					print("XSpeed Can't find a trajectory, refineing the property and run again dnnf...")
					os.chdir(running_directory)
					refine_counter = refine_counter + 1
					dnnf.refined_property(inputs,dnnf_cmd,refine_counter)
					Number_refined[example[i][0]] = refine_counter # this one
		dnnf.reset()
		if (how_many == N-1):
			pt.add_row([example[i][0], "", "Average time", Total_verified_xspeed_time/Number_verified, Total_verified_overall_time/Number_verified])

	print("Number of instances verified by xspeed is ",Number_verified,"out of",N)
	pt.add_row(["","","","",""])
print(pt)


with open('save1.txt', 'a') as f:
    f.write(str(pt))
