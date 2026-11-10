# creating list of prducts 
products=["laptop","phone","watch","computer","speaker","cpu"]
#creating tuple names as sample_product and stores product name , catagory and price
sample_products=("laptop",50000,"dell")
#print second and last product in the list
print(products[1],products[-1])
# append two new products to the list and print the list 
products.append("mouse")
products.append("keyboard")
print(products)

sample_products=list(sample_products)
sample_products[1]=60000
sample_products=tuple(sample_products)
print(sample_products)