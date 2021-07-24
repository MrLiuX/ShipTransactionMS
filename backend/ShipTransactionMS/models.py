from django.db import models


class Personnel(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=11)
    teleNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE)


class Department(models.Model):
    department = models.CharField(max_length=255, primary_key=True)
    minister = models.CharField(max_length=255, default="none")
    note = models.CharField(max_length=255, default="无")


class Ship(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    manufactureTime = models.CharField(max_length=255)
    manufactureDress = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    tonnageTotal = models.CharField(max_length=255)
    tonnageNet = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Inventory(models.Model):
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255, primary_key=True)
    specification = models.CharField(max_length=255)  # 规格
    unit = models.CharField(max_length=255)  # 单位
    location = models.CharField(max_length=255)  # 存放位置
    accumulativeStorage = models.IntegerField()  # 累计入库
    accumulativeUnStorage = models.IntegerField()  # 累计出库
    inventory = models.IntegerField()  # 库存量
    inventoryUpperLimit = models.IntegerField()  # 库存上限
    inventoryLowerLimit = models.IntegerField()  # 库存下限
    note = models.CharField(max_length=255)


class Application(models.Model):
    applicant = models.CharField(max_length=255)  # 申请人
    date = models. DateTimeField(auto_now_add=True)
    Material = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    agreePersonnel = models.CharField(
        max_length=255, default="", blank=True, null=True)
    isAgree = models.BooleanField(default=False)
    applicationsQuantity = models.IntegerField()
    OperationType = models.BooleanField()  # 操作类型，True为购入，False为领用
    note = models.CharField(max_length=255, default="", blank=True, null=True)
    suppliers = models.CharField(
        max_length=255, default="", blank=True, null=True)
    orderId = models.CharField(
        max_length=255, default="", blank=True, null=True)


class Certificate(models.Model):
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE)
    variety = models.CharField(max_length=255)  # 种类
    date = models. DateField(auto_now_add=True)
    indate = models. DateField()
    inspectionContent = models.CharField(max_length=255)  # 下次检验内容
    inspectionDate = models.DateField()#下次检验日期
    certificate = models.CharField(max_length=255)# 证书名称及编号
    registrationId = models.CharField(max_length=255)#船检登记号
    unit = models.CharField(max_length=255) #发证单位
    note = models.CharField(max_length=255,default="", blank=True, null=True)
    location = models.CharField(max_length=255) #存放位置