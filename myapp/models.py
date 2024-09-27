from django.db import models
from django import forms

#Create your models here.
class Employee(models.Model):
    # id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=50, 
        choices=[('Male', 'Male'), ('Female', 'Female')], 
        default='Male'
        )
    position = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    address = models.TextField()
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=30, unique=True)
    birthday = models.DateField()
    religion = models.CharField(
        max_length=20, 
        choices=[('พุทธ','พุทธ'), ('คริสต์', 'คริสต์'), ('อิสลาม', 'อิสลาม'), ('อื่นๆ', 'อื่นๆ')], 
        default='พุทธ'
        )
    addition_note = models.TextField(null=True, blank=True) 
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'firstname': 'ชื่อ',
            'lastname' : 'นามสกุล',
            'gender' : 'เพศ',
            'position' : 'ตำแหน่งงาน',
            'salary' : 'เงินเดือน',
            'address' : 'ที่อยู่',
            'email' : 'อีเมล',
            'phone' : 'โทรศัพท์',
            'birthday' : 'วันเกิด',
            'religion' : 'ศาสนา',
            'addition_note' : 'บันทึกเพิ่มเติม',
        }

        widgets = {
            'gender' : forms.Select(),
            'birthday' : forms.DateInput(attrs={'type':'date'}),
            'religion' : forms.Select(),
            'address' : forms.Textarea(attrs={'rows':'3'}),
            'addtion_note' : forms.Textarea(attrs={'rows':'3'}),
        }
        
#signin #############
class Member(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
class MemberForm(forms.ModelForm):
    confirm_pasw = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput
    )
    save = forms.BooleanField(required=False)
    
    class Meta:
        model = Member
        fields = '__all__'
        widget = {
            'password': forms.PasswordInput()
        }
    
    