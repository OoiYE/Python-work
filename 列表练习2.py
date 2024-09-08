shop=["手机","电脑","鼠标垫","游艇"]
print("现在商店里有：",shop)
a=(str(input("请输入是否要添加商品（Yes or No)")))
print(a)
if a=="Yes":
    b=(input("请输入你想要添加的商品："))
    shop.append(b)
print("商品现有",(shop))
c=(str(input("请输入是否要删除某商品(Yes or No)")))
if c=="Yes":
    d=(input("请输入你想要删除的商品："))
    shop.remove(d)
print("商品现有",(shop))
e=int(input("请输入序号："))
print(shop[e])