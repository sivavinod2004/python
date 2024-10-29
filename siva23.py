#sivapriya A V
#CSE B
#PROGRAM TO FIND NUMBER OF VOWELS IN A STRING
string_input=input("enter a string")
vowels="aeiouAEIOU"
vowels_count=0
for character in string_input:
    if character in vowels:
        vowels_count+=1
print(f"number of vowels in {string_input}={vowels_count}")