my_dict={"Helen":1992,"Michael":1995,"Herman":1996}
print(my_dict)
print(my_dict["Helen"])
my_dict["Herman"]=1997
my_dict.update({"Jack":2000,
                "Daniel":2004})
print(my_dict)
del my_dict["Michael"]
print(my_dict.get("Michael", "Ключ отсутствует"))
print(my_dict)

my_set={10,11,12,13,10,11,12,13,"real","unreal","real",True,(13,12,11)}
print(my_set)
my_set.add(14)
my_set.add(15)
my_set.discard(10)
print(my_set)