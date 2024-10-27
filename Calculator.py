print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people=int(input("How many people to split the bill?"))
calc = (total_bill * tip) / 100
final_result = total_bill + calc
each_people = final_result/people
final_estimate = round(each_people,2)
print("Each person should pay: " + "$" + str(final_estimate))