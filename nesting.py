#nesting lists in a dictionary

dict = {"name":['saiteja','chaitanya','ramteja','amanullah']}

print(dict['name'][0])
print(dict['name'][3])

nested_list = [1,2,3,4,[0,-1,-2]]

print(nested_list[4][2])

#nested list accessing

travel_log = {"France":{"cities_visited":["paris","lille","dijion"],"total_visited": 12},"Germany":{"cities_visited":["Berlin","Hambug","stuttgrat"],"total_visited":9}}

print(travel_log["Germany"]["cities_visited"][2])



