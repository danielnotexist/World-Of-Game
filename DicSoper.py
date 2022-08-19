""""
soper_list = {"milk": 9.99}
print(soper_list["milk"])
markets = {"rami levi": "netanya", "osher ad": "tel aviv"}
print(markets["osher ad"])
"""
test = {"kfar yona": "9.99", "netanya": "8.99"}
new = open("test.txt", "w")
new.write(test["kfar yona"])
new.close()
new = open("test.txt", "r")
print(new.read(),)
