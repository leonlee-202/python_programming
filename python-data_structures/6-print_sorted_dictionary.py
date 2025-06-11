def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
my_dict = {
  "name" : "Leon",
  "age"  : "19",
  "city" : "Kisumu",
  "occupation" :"student",
    }
print_sorted_dictionary(my_dict)