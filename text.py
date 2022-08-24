import re
 
line = "===第1章 晋升工程师贾东旭出事==="
line2 = "===第450章 欠债还钱（感谢大佬‘网文小手’的打赏）==="
 
matchObj = re.match( r'===第(.*?)章 (.*?)(\((.*?)\))?===', line2, re.M|re.I)
 
if matchObj:
   print(matchObj.group())
   print(matchObj.group(1))
   print(matchObj.group(2))
else:
   print("No match!!")