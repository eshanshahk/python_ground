print("Hey Guys!!")# to print anythin in python
print("""Hello
              world!!!!""") #""" used for printing multiple lines
print(f"There are {365/7:.0f} weeks in a year") #formated string and decimal places
from helper_functions import print_llm_response #use this to do llm prompting using variables
print_llm_response("What is the capital of France?") #eg
hey_list=["a","b","c"] #list datatype
hey_list.append("d") #to add onw element
hey_list.remove("a") #to remove
for task in list_of_task:
  print task() #for loop 
