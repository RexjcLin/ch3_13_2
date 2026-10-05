""" from django.db import models

# Create your models here.
class Student(models.Model):
    cId = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=28,blank=False)
    cSex = models.CharField(max_length=1,blank=False,default="M")
    cBirthday = models.DateField(blank=False)
    cEmail = models.EmailField(blank=False)
    cPhone = models.CharField(max_length=15,blank=False)
    cAddress = models.CharField(max_length=100,blank=False)
    cHeight = models.IntegerField(blank=True)
    cWeight = models.IntegerField(blank=True)

    #建立時會自動填入當前日期
    #cCreateDate = models.DateField(auto_now_add=True)
    #修改時會自動填入當前日期
    #cUpdateDate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.cId) """
from django.db import models

# Create your models here.
class Student(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField(max_length=20, blank=False)
    cSex =  models.CharField(max_length=1, blank=False, default='F')
    # cBirthday = models.DateField(auto_now_add=True, null=False)
    #這個參數的預設值也為False，設定為True時，會在model物件第一次被建立時，
    #將欄位的值設定為建立時的時間，以後修改物件時，欄位的值不會再更新。
    #cBirthday = models.DateField(auto_now=True, null=False)
    #這個參數的預設值為false，當設定為true時，能夠在儲存該欄位時，
    #將其值設為目前時間，並且每次修改model，都會自動更新
    cBirthday = models.DateField(null=True, blank=True)
    cEmail = models.CharField(max_length=100, blank=False)
    cPhone = models.CharField(max_length=50, blank=False)
    cAddr = models.CharField(max_length=255, blank=False)
    cHeight = models.IntegerField(blank=True, null=True) 
    cWeight = models.IntegerField(blank=True, null=True)

#一個學生有多個成績(one to many)(students to scorelist)
class Scorelist(models.Model):
    id = models.AutoField(primary_key=True)
    #外來鍵，Scorelist 表中的 cID 欄位會連到 Student 表的主鍵 cID，刪除學生時一起刪除資料
    cID = models.ForeignKey('Student', on_delete=models.CASCADE, null=True) 
    course = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(blank=False)
    
#一個學生有一個密碼與權限(one to one)(students to permissions)
class Permissions(models.Model):
    id = models.AutoField(primary_key=True)
    cID = models.OneToOneField('Student', on_delete=models.CASCADE, null=True)
    passwd = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False) #0管理者 #1一般使用者

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)
    authors = models.ManyToManyField(to='Author')

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    aID = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=32, blank=False)
