

# class employee:
#
#     def __init__(self,empid,name,sal):
#         self.empid = empid
#         self.name = name
#         self.sal = sal
#
#     def get_einfo(self):
#         print('employee details are', self.empid, self.name, self.sal)
#
# madhu = employee(100,'madhu nettam',10000)
# b1 = madhu.get_einfo()
#
# class Employee:
#
#     # 1. STATE
#     def __init__(self, empid, name, sal):
#         self.empid = empid
#         self.name = name
#         self.sal = sal
#
#
#     # 2. BEHAVIOR
#     def get_einfo(self):
#         print("Employee details are ", self.empid, self.name, self.sal)
#
# # object creation
# # madhu.get_einfo()
# madhu = Employee(100, 'Madhu Nettem', 15000)    # x = 10
# d1 = madhu.get_einfo()


# class employee:
#     def __init__(self,empid,name,sal):
#         self.empid = empid
#         self.name = name
#         self.sal = sal
#
#     def get_einfo(self):
#         print('employee details are',self.empid,self.name,self.sal)
#
# madhu = employee(100,'madhu nettam',15000)
# b1 = madhu.get_einfo()

class car:
    def __init__(self,name,model,cost):
        self.name = name
        self.model = model
        self.cost = cost

    def car_einfo(self):
        print('car price details are ',self.name,self.model,self.cost)

kia = car('seltos',2022,500000)
m1 = car_einfo()                                        # car_einfo showing error


class bankdetails:
    def __init__(self,name,account,sal):
        self.name = name
        self.account = account
        self.sal = sal

    def banke_info(self):
        print('bank details ',self.name,self.account,self.sal)

icic = bankdetails
m = banke_info()

