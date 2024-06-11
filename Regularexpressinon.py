import re
# text ="Welcome to regex"# compile and search method working
# result= re.compile("regex")# assigning what to be searched
# answer= result.search(text)# searching that word is available r not in
# print(answer)
#
#  #  FIND ALL METHOD WORKING
#
# result= re.findall("to",text)
# print(result)
# mypattern="Welcome"
# result=re.findall(mypattern,text)
# print(result)
#        # SEARCH METHOD working in 3 ways
# result=re.search("regex",text)
# print(result)
# print(result.start())# 1. START METHOD
# print(result.span()) #2. SPAN METHOD
# print(result.string) #2. STRING METHOD

def phone_number(number):
    pattern1=r"^[789]\d{9}$"# with r
    pattern2 ="^[88]\\d{9}$"# with \\
    if re.match(pattern2,number):
       return f"valid :{number}"
    else:
        return f"invalid:{number}"

print(phone_number(number="8876543210"))
