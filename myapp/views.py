from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.db.models import Avg, Sum,Q
def test(request):
    return HttpResponse("This is a test view.")
# Create your views here.

def student_list(request):
    #students = Student.objects.all()
    #print(students)
    #for student in students:
    #    print(model_to_dict(student))
    #data=Student.objects.values('cId', 'cName', 'cAddr', 'cHeight', 'cWeight')
    #for student in data:
    #    print(student)
    #data=Student.objects.values('cSex').distinct()
    #for student in data:
    #    print(student)
    #只取一筆資料
    #data=Student.objects.get(cId="2")
    #print(model_to_dict(data))
    #有可能一筆以上資料
    #data=Student.objects.filter(cSex="M")
    
    #__gte 代表大於等於，例如：
    #data=Student.objects.filter(cSex="M", cHeight__gte=170)
   
    ###########################
    #from django.db.models import Q
    #使用 Q 物件進行複雜查詢，例如：
    #data=Student.objects.filter(Q(cId__lt=3) | Q(cId__gte=8))
   
    ###########################
    #介於4到8之間的學生資料
    #data=Student.objects.filter(cId__range=(4, 8))
   
    #IN 查詢，例如：
    #data=Student.objects.filter(cId__in=[1, 3, 5])
    #查詢開頭為 '0918' 的學生資料
    #data=Student.objects.filter(cPhone__startswith='0918')
    #查詢中間有'建國'地址的學生資料
    #data=Student.objects.filter(cAddr__contains='建國')
    #根據生日做遞減排序(-是遞減 沒有 - 是遞增)
    #data=Student.objects.order_by('-cBirthday')
    #根據性別遞增 生日遞減
    #data=Student.objects.order_by('cSex', '-cBirthday') 
    #data=Student.objects.all()[5:]
    #根據學生資料取得成績相加
    #data=Scorelist.objects.aggregate(total_score=Sum('score'))
    #根據學生國文成績做統計
    #data=Scorelist.objects.filter(course='國文').aggregate(total_chinese_score=Sum('score'))
    #根據個別同學的成績做統計
    #data=Scorelist.objects.values('cID').annotate(total_score=Sum('score'))
    #data2=Scorelist.objects.values_list('cID',).annotate(total_score=Avg('score')).filter(total_score__gte=80)
    #data=Scorelist.objects.filter(cID__lte=5).values('cID').annotate(total_score=Sum('score'))
    #for item in data:
    #    print(item)
    #print("-----")
    #顯示小數後兩位
    #for item in data2:
    #    print((item[0], round(item[1], 2)))
    # students = Student.objects.filter(cName__startswith='Bill5').exists()
    # if not students:
    #    Student.objects.create(cName='Bill5', cSex='M', cBirthday='2000-01-01',cPhone='0918123456',cAddr='新竹',cEmail='bill5@example.com', cHeight=180, cWeight=75)
    #    print("Created new student Bill5")
    # else:
    #    print("Student Bill5 already exists.")
    # if not students:
    #     add=Student(cName='Bill3', cSex='M', cBirthday='2000-01-01',cPhone='0918123456',cAddr='新竹',cEmail='bill3@example.com', cHeight=180, cWeight=75)
    #     add.save()
    #     print("Created new student Bill3")
    # else:
    #     print("Student Bill3 already exists.")
    #將cID=11的電子郵件更新為新的地址
    # try:
    #     updata=Student.objects.get(cID=11)
    #     updata.cEmail='new_email@example.com'
    #     updata.save()
    # except Exception as e:
    #     print(f"Error updating student with cID=11: {e}")
    # updata=Student.objects.filter(cName='Bill1').update(cEmail='bill1X_new@example.com')
    # 將ID大於11的學生地址更新為台北
    # try:
    #     updata=Student.objects.filter(cID__gte=11).update(cAddr='台北')
    # except Exception as e:
    #     print(f"Error updating students: {e}")
    #單筆刪除
    # try:
    #     student_to_delete=Student.objects.get(cID=13)
    #     student_to_delete.delete()
    # except Exception as e:
    #     print(f"Error deleting student with cID=13: {e}")
    #多筆刪除
    # try:
    #     students_to_delete=Student.objects.filter(cID__gte=11)
    #     students_to_delete.delete()
    # except Exception as e:
    #     print(f"Error deleting students with cID>=11: {e}")

    ##################
    # one to many
    # add
    # 若學生未建立，一起建立學生與成績
    # try:
    #     # 確認無此人
    #     student_data = Student.objects.get(cName='王大明')
    #     print("already exists.")
    # except:
    #     # 創建新學生資料
    #     student_data = Student.objects.create(
    #         cName='王大明', cSex='M', cBirthday='2020-08-20',
    #         cEmail='wang@yahoo.com.tw', cPhone='09333333', cAddr='新竹',
    #         cHeight=120, cWeight=40
    #     )
    #     print("created successfully.")
        
    #     # 創建成績資料
    #     Scorelist.objects.create(cID=student_data, course='地理', score=60)
    #     Scorelist.objects.create(cID=student_data, course='音樂', score=100)
    #     print("created successfully.")

    # # 若學生已建立，再建立科目成績
    # try:
    #     # 確認有 '王大明'
    #     student_data = Student.objects.get(cName='王大明')
    #     # 檢查是否已經有 '歷史' 科目
    #     geography_exists = Scorelist.objects.filter(cID=student_data, course='歷史').exists()
    #     if not geography_exists:
    #         Scorelist.objects.create(cID=student_data, course='歷史', score=60)
    #         print("History score added successfully.")
    #     else:
    #         print("already has a score for 'History'.")
        
    #     # 檢查是否已經有 '體育' 科目
    #     pe_exists = Scorelist.objects.filter(cID=student_data, course='體育').exists()
    #     if not pe_exists:
    #         Scorelist.objects.create(cID=student_data, course='體育', score=100)
    #         print("PE score added successfully.")
    #     else:
    #         print("already has a score for 'PE'.")
        
    # except:
    #     print("not found.")
    # search
    # 外連鍵的scorelist中s小寫
    # datas = Student.objects.filter(scorelist__course='國文').values(
    #     'cID', 'cName', 'scorelist__course', 'scorelist__score')
    # for data in datas:
    #     print(data)

    # from django.db.models import Sum,Count,Max,Min,Avg
    # datas =  Student.objects.values_list('cID','cName').annotate(Sum('scorelist__score'), Avg('scorelist__score'))
    # for data in datas:
    #     print(data)
    ##################
    # update
    # try:
    #     # 確認是否存在指定名稱的學生
    #     student_data = Student.objects.get(cName='簡奉君')
    #     # 確認是否存在指定的課程並更新分數
    #     course_exists = Scorelist.objects.filter(cID=student_data, course='國文').exists()

    #     if course_exists:
    #         Scorelist.objects.filter(cID=student_data, course='國文').update(score=0)
    #         print("分數更新成功。")
    #     else:
    #         print("未找到該課程，無法更新分數。")
    # except:
    #     print("未找到該學生。")
    # delete
    # 刪除王大明資料與科目所有成績
    # try:
    #     Student.objects.get(cName='王大明').delete()
    #     print("刪除資料成功。")
    # except:
    #     print("未找到該學生。")
    
    # 刪除王大明的某科成績
    # try:
    #     student_data = Student.objects.get(cName='王大明')
    # #     # 確認是否存在指定的課程並刪除該課程成績
    #     course_exists = Scorelist.objects.filter(cID=student_data, course='地理').exists()
    #     if course_exists:
    #         Scorelist.objects.filter(cID=student_data, course='地理').delete()
    #         print("成績刪除成功。")
    #     else:
    #         print("未找到該課程成績，無法刪除。")
    # except:
    #     print("未找到該學生。")

    return HttpResponse("Student list view.")
