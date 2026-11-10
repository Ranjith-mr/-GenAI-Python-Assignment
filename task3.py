 # creating a dictionary using prce_dic ehere keys as names and values as price 
price_dic={
  "del":40000,
  "hp":50000,
  "lenova":35000,
  "macbook":60000,
  "samsung":70000,
  "thinkpad":74000
}
print(price_dic)
# add a new product to list  and update a price of existing price
price_dic["iphone"]=100000
price_dic["lenova"]=30000
print(price_dic)

#remove a product by name using a case that not list  i used a simple conditional statemnet
if "asus" in price_dic:
  price_dic.pop("asus")
else:
  print("product not found")




