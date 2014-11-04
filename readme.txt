A friend of mine came to me asking if I knew anything about cracking passwords. 
I said that I didn't, and would only be able to do it by brute force if
I had access to the terminal which you typed it in. This method is really slow,
especially since the password he needed was over telnet. 

This didn't seem like an issue, only with time. This utilized the telnetlib
module of python to connect to the server and try password combinations. The
password was created using a python script that took two lowercase ASCII words
from the words file in Linux and concatenated them together with a dash in
between. This program tried every combination, albeit very slowly. 

Will eventually print out the username and password that succeeded. 

To run this: you must change the username variable in the program, and the words
file must be in the same directory. Runs python 3.4 or similar. 