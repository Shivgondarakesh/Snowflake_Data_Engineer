# "Malayalam" reverse the string and chek for the palindrome and convert to list
string="Malayalam"
lower=string.lower()
reversed_lower=lower[::-1]
if lower==reversed_lower:
    print(f"string is palindrome: {reversed_lower}")
else:
    print(f"string is not palindrome: {reversed_lower}")
char_list= list(string)
print("converted list",char_list)

# reading csv file
import pandas as pd
df=pd.DataFrame("data/employee.csv")
print(df)

