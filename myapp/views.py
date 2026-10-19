from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from myapp.models import *
from django.forms.models import model_to_dict
# Create your views here.
def search_list(request):
    errormessage = ""
    if 'cname' in request.GET:
        name = request.GET.get('cname', '')
        print(name)
        result = Students.objects.filter(cName__icontains=name).order_by('-cID')

    else:
        result = Students.objects.all().order_by('-cID')
    if not result:
        errormessage = "查無資料"
    return HttpResponse(render(request, 'search_list.html', locals()))
def search_name(request):
    return HttpResponse(render(request, 'search_name.html', locals()))
def index(request):
    if 'search' in request.GET:
        name = request.GET.get('search', '')
        name = name.strip()
        key = name.split()
        #搜尋所有關鍵字在cname,cbirthday,cemail,cphone,caddr欄位
        from django.db.models import Q
        query = Q()
        for k in key:
            query |= (Q(cName__icontains=k) | Q(cBirthday__icontains=k) | Q(cEmail__icontains=k) | Q(cPhone__icontains=k) | Q(cAddr__icontains=k))
        result = Students.objects.filter(query).order_by('cID')
    else:
        result = Students.objects.all().order_by('cID')

    data_count = result.count()

    #分頁
    from django.core.paginator import Paginator
    paginator = Paginator(result, 3)  # 每頁顯示3筆資料
    page = request.GET.get('page')
    result = paginator.get_page(page)

    for student in result:
        if student.cSex == 'M':
            student.cSex = '男'
        elif student.cSex == 'F':
            student.cSex = '女'

    errormessage = ""
    if data_count == 0:
        errormessage = "查無資料"

    return HttpResponse(render(request, 'index.html', locals()))
def post(request):
    if request.method == "POST":
        cname = request.POST.get('cname', '')
        csex = request.POST.get('csex', '')
        cbirthday = request.POST.get('cbirthday', '')
        cemail = request.POST.get('cemail', '')
        cphone = request.POST.get('cphone', '')
        caddr = request.POST.get('caddr', '')
        student = Students(
            cName=cname,
            cSex=csex,
            cBirthday=cbirthday,
            cEmail=cemail,
            cPhone=cphone,
            cAddr=caddr
        )
        student.save()
        # 處理表單提交
        return redirect('index')
    else:
        return render(request, 'post.html')
def edit(request, cid):
    student = Students.objects.get(cID=cid)
    if request.method == "POST":
        student.cName = request.POST.get('cname', '')
        student.cSex = request.POST.get('csex', '')
        student.cBirthday = request.POST.get('cbirthday', '')
        student.cEmail = request.POST.get('cemail', '')
        student.cPhone = request.POST.get('cphone', '')
        student.cAddr = request.POST.get('caddr', '')
        student.save()
        return redirect('index')
    else:
        student = model_to_dict(student)
        return render(request, 'edit.html', locals())

def delete(request, cid):
    # 確認學生是否存在
    if not Students.objects.filter(cID=cid).exists():
        return redirect('index')
    student = Students.objects.get(cID=cid)
    if request.method == "POST":   
        student.delete()
        return redirect('index')
    else:
        return render(request, 'delete.html', locals())

def getAllItems(request):
    result = Students.objects.all().order_by('cID')
    for student in result:
        print(model_to_dict(student))
    result = list(result.values())
    return JsonResponse(result, safe=False)
#safe=False 允許返回非字典的 JSON 資料
#safe=True 允許返回字典的 JSON 資料

def getItem(request, id):
    try:
        student = Students.objects.get(cID=id)
        result = model_to_dict(student)
        return JsonResponse(result, safe=True)
    except Students.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, safe=True)
    
from django.views.decorators.csrf import csrf_exempt
#取消csrf驗證
@csrf_exempt
def createItem(request):
    try:
        if request.method == "GET":
            cname = request.GET.get('cname', '')
            csex = request.GET.get('csex', '')
            cbirthday = request.GET.get('cbirthday', '')
            cemail = request.GET.get('cemail', '')
            cphone = request.GET.get('cphone', '')
            caddr = request.GET.get('caddr', '')
            print("Received GET request with parameters:")
            print(cname, csex, cbirthday, cemail, cphone, caddr)
        elif request.method == "POST":
            cname = request.POST.get('cname', '')
            csex = request.POST.get('csex', '')
            cbirthday = request.POST.get('cbirthday', '')
            cemail = request.POST.get('cemail', '')
            cphone = request.POST.get('cphone', '')
            caddr = request.POST.get('caddr', '')
            print("Received POST request with parameters:")
            print(cname, csex, cbirthday, cemail, cphone, caddr)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=True, status=400)
    try:
        student = Students(
            cName=cname,
            cSex=csex,
            cBirthday=cbirthday,
            cEmail=cemail,
            cPhone=cphone,
            cAddr=caddr
            )
        student.save()
        return JsonResponse({'success': 'Student created successfully'}, safe=True)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=True, status=400)
@csrf_exempt
def updateItem(request, id):
    try:
        student = Students.objects.get(cID=id)
    except Students.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, safe=True, status=404)
    try:
        if request.method == "GET":
             
            cname = request.GET.get('cname', student.cName)
            csex = request.GET.get('csex', student.cSex)
            cbirthday = request.GET.get('cbirthday', student.cBirthday)
            cemail = request.GET.get('cemail', student.cEmail)
            cphone = request.GET.get('cphone', student.cPhone)
            caddr = request.GET.get('caddr', student.cAddr)
        elif request.method == "POST":
            cname = request.POST.get('cname', student.cName)
            csex = request.POST.get('csex', student.cSex)
            cbirthday = request.POST.get('cbirthday', student.cBirthday)
            cemail = request.POST.get('cemail', student.cEmail)
            cphone = request.POST.get('cphone', student.cPhone)
            caddr = request.POST.get('caddr', student.cAddr)
        student.cName = cname
        student.cSex = csex
        student.cBirthday = cbirthday
        student.cEmail = cemail
        student.cPhone = cphone
        student.cAddr = caddr
        student.save()
        return JsonResponse({'success': 'Student updated successfully'}, safe=True)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=True, status=400)
@csrf_exempt
def deleteItem(request, id):
    try:
        student = Students.objects.get(cID=id)
    except Students.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, safe=True, status=404)
    try:
        student.delete()
        return JsonResponse({'success': 'Student deleted successfully'}, safe=True)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=True, status=400)