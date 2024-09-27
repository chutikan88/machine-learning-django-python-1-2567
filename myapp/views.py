from django.shortcuts import render, HttpResponseRedirect
from joblib import load

model = load(r'D:\BigData2\mydata (2)\mydata\heart_model.pkl')

def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak	= request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
        y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]) 
        return render(request, 'heart/result.html', {'result':y_pred})
    return render(request, 'heart/forms.html')

#การสร้างฟอร์ม
from myapp.models import EmployeeForm
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    
    return render(request, './database/employee_create.html', {'form': form})

# การสร้างฟอร์มด้วย crispy form
def createcrispy(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    
    return render(request, './database/createcrispy.html', {'form': form})

from myapp.models import Employee

def employee_read(request):
    data = Employee.objects.all()
    return render(request, './database/employee-read.html', {'data': data})

#การค้นหาข้อมูล
from django.shortcuts import render
from myapp.models import Employee, EmployeeForm
from .forms import SearchForm, SearchRead
from django.db.models import Q

def employee_search(request):
    if request.method =='POST':
        kw = request.POST.get('name','')
        form = SearchForm(request.POST, initial={'name':kw})
    else:
        kw = request.GET.get('name','')
        form = SearchForm(initial={'name':kw})
        
    data = Employee.objects.filter(Q(firstname__contains=kw)|Q(lastname__contains=kw))[:10]
    
    return render(request,'./database/employee-search.html', { 'form' : form, 'data' : data })

#การสร้างเมนูค้นหาที่ไฟล์ employee-read.html
def search_read(request):
    if request.method =='POST':
        kw = request.POST.get('name','')
        form = SearchRead(request.POST, initial={'name':kw})
    else:
        kw = request.GET.get('name','')
        form = SearchRead(initial={'name':kw})
        
    data = Employee.objects.filter(Q(firstname__contains=kw)|Q(lastname__contains=kw))[:10]
    
    return render(request,'./database/employee-read.html', { 'form' : form, 'data' : data })

#การแก้ไขข้อมูล
from django.shortcuts import HttpResponseRedirect

def employee_edit(request):
    data = Employee.objects.all()
    return render(request, 'database/employee-edit.html', {'data': data})

def employee_update(request, id):
    if request.method == 'POST':
        row = Employee.objects.get(id=id)
        
        form = EmployeeForm(instance=row, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/employee_search")
            
    else:
        #วิธีที่ 1
        row = Employee.objects.get(id=id)
        form = EmployeeForm(initial=row.__dict__)
        
        #วิธีที่ 2
        # row = Employee.objects.filter(id=id).values()
        # form = EmployeeForm(instance=row[0])
        return render(request, 'database/employee_update.html', {'form': form})

#การลบข้อมูล
def employee_delete(request, id):
    Employee.objects.get(id=id).delete()
    
    data = Employee.objects.filter()[:10]
    return render(request, 'database/employee-edit.html', {'data': data})

#signin การลงทะเบียนยื่นยันรหัสผ่าน
from myapp.models import Member, MemberForm

def member_signin(request):
    if request.method == 'POST':
        confirm_pswd = request.POST.get('confirm_pswd', '')
        save = request.POST.get('save', False)
        
        #นำค่าไปใช้งานตามต้องการ
        form = MemberForm(request.POST)
        # if form.is_valid():
        #     form.save()
    else:
        form = MemberForm()
    
    return render(request, 'database/member_signin.html', {'form': form})





#pagination
# from django.core.paginator import Paginator
# def pagination_bs(request, pg):
#     if pg == None:
#         pg = 1
        
#     rows = Employee.objects.all().order_by('id')
#     pgn = Paginator(rows, 2)
#     page = pgn.get_page(pg)
#     return render(request, 'database/employee-search.html', {'page': page})
    