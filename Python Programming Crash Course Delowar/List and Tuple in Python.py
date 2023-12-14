# List and Tuple in Python 

my_list = [] #empty list
my_list = [1,2,3] # list of integer
my_list = [1,"Delowar",3,4,True] # list with mixed data type


pest = ["dog","cat",2,True]
# indexing 0 1 2 3 negotive indexing -4 -3 -2 -1
print(pest)
print(type(pest))
# print the first element
print(pest[0])
# print the fourth element
print(pest[3])
#negativ indexing
print(pest[-3])

fav_language = ["java","C","php","C++"]
print(fav_language)
#append method to add python
fav_language.append("Python")
print(fav_language)
fav_language.extend(["Python","jabascript","dart"])
print(fav_language)

#The list is concatenated
fav_fruit = ["mango","apple","pranges"]
#concatention
print(fav_fruit + ["bannas","lemons","guava"])
#repeating a list
print(["Banglades"] * 5)
country = ["Banglades"] * 4
print(country)
fav_fruit.insert(0,"Delowar")
print(fav_fruit)

#Delete or remove methods
country = ["Bangladesh","india","pakistan"]
country.pop()
print("PoP",country)
country = ["Bangladesh","india","pakistan"]
country.remove("india")
print("Remove",country)
country = ["Bangladesh","india","pakistan"]
country.clear()
print("Clear",country)
country = ["Bangladesh","india"]
print(len(country))


#Tuple in python
my_tuple = (1,2,"string",True,3.5)
print(my_tuple)
print(my_tuple[4])
