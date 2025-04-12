#writing a program on the auction bid
import os

print("WELCOME TO AUCTION BID")
auction_dict = {}
value = True

while value:
    name = input("enter the name ? ")
    bid = int(input("Enter your bid amount? $"))
    auction_dict[name] = bid
    choice = input("Type \"Yes\" if there are other bidders or \"No\" : ")
    if choice.lower() == "yes":
        os.system('clear')
        value = True
    elif choice.lower() == "no":
        value = False
        os.system('clear')

cost_list=[]
name_list=[]
for i in auction_dict.values():
    cost_list.append(i)
for j in auction_dict.keys():
    name_list.append(j)

maximum_bid = max(cost_list)

index_value = cost_list.index(maximum_bid)

print(f"{name_list[index_value]} won the bid of ${maximum_bid}")













    

