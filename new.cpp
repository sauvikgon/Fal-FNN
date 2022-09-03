#include <boost/process.hpp>

#include <string>
#include <iostream>
#include <cstring>
//using namespace std2;
//using namespace boost::process;

int main()
{
    using namespace boost::process;
    boost::process::pstream pipe_stream, pipe_stream2;
    boost::process::child c("runlim -s 4096 -r 100 dnnf OSC_16/P1_loc_1_unsafe/property_1_Loc_1_unsafe.py --network N OSC_16/F_OSC_16_T10_D3_10K.onnx --save-violation violation", std_out > pipe_stream);
    std::string line, line2;
    bool flag;
    while(pipe_stream, std::getline(pipe_stream, line))
    {
	if(line.find("result: sat") != -1)
		std::cerr << line << std::endl;
		flag = true;
	}

    c.wait();
    if(flag)
    {
       boost::process::child c1("python3 try.py", std_out > pipe_stream2);
       std::getline(pipe_stream2, line2);
       std::cerr << line2 <<std::endl;
       c1.wait();
    }
   
      //ToDo: Find all the substring[floating-point number] in line2 and stored in an integer array.

   //To remove extra brackets
   int len=0;
   len=line2.length();
   if(line2[1]=='[')
   	line2=line2.substr(2,len-1);
   len=line2.length();
   if(line2[len-2]==']')
   	line2=line2.substr(0,len-3);
   
   len=line2.length();
   
   std::string string;
   int i=0;
   
   char *ptr;
   ptr = strtok(line2.data(), " ");
   
   int size;
   float stn=0.0;
   
   while (ptr != NULL)  
   {
      //To convert character pointer to string
      size=strlen(ptr);
      string.assign(ptr,size);
      
      //To print the numbers which have a . in last digit in integer format
      if(string[string.length()-1]=='.')
      {
      	sscanf(string.data(),"%f", &stn);
      	std::cerr << stn << std::endl;
      }
      
      //To print the normal numbers
      else
      	std::cerr << string << std::endl;
      
      ptr = strtok (NULL, " ");  
      
   }
}
