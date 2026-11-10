# using the product list and price dic , create a list of tuples names catalog where each tuple is (product name , price , catagory)
price_dic={
  "del":40000,
  "hp":50000,
  "lenova":35000,
  "macbook":60000,
  "samsung":70000,
  "thinkpad":74000
}

catalog=[
  ("laptop",price_dic["del"],"del"),
  ("hp",price_dic["hp"],"hp"),
  ("lenova",price_dic["lenova"],"lenova"),
  ("macbook",price_dic["macbook"],"macbook"),
  ("samsung",price_dic["samsung"],"samsung"),
  ("thinkpad",price_dic["thinkpad"],"thnkpad")
]
print(catalog)
# created dictniory
catagory_to_products={
  "dell":["laptop"],
  "hp":["phone"],
  "lenova":["watch"],
  "macbook":["computer"],
  "samsung":["speaker"],
  "thinkpad":["cpu"]
}
print(catagory_to_products)

# print all products that belong to the catagory that has maximum number of products 
max_catagory=max(catagory_to_products,key=lambda x: len(catagory_to_products[x]))
print("catagory",max_catagory)
print("products",catagory_to_products[max_catagory])