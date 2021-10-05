#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class" 		: 	"Astr 119",
	"prof" 			: 	"Brant",
	"awesomeness" 	: 	10
}
print(type(example_dict)) 	#will say dict

#get a value via key
course = example_dict["class"] #will go through every element untill it find the string "class", will place it into the new variable astr119
print(course)

#change a value via key
example_dict["awesomeness"] += 1 	#increase awesomeoness

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys(): #makes a list of the keys and make x equal to each key
	print(x, example_dict[x])
	