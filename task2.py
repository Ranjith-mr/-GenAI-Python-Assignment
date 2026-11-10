# create a  product list and convert it into a set called catagorie_set
catagorie=["electronics","mobile","mouse","watch","electronics"]
print(catagorie)
catagorie_list=set(catagorie)
#adding  2 product names as same achecking if duplictes are ignored 
catagorie_list.add("gaming")
print(catagorie_list)
catagorie_list.add("gaming")
print(catagorie_list)
# checking whether the product is avalable in list or not 
print("electronics" in catagorie_list)
#checks how many products are in 
print(len(catagorie_list))
