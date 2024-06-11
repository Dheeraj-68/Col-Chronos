from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import connection
# Create your views here.

def table_detail(request, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    context = {'table_name': table_name, 'rows': rows, 'column_names': column_names}
    if request.method == 'POST':
        # Handle form submission here to add or drop rows
        # You can use the Django ORM to insert or delete rows in the table
        messages.success(request, 'Changes saved successfully!')
    return render(request, 'table_detail.html', context)

def home(request):
    return render(request,'login.html')

@login_required(login_url='/')
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='/')
def viewinfo(request):
    tables = [table_name for table_name in connection.introspection.table_names() if table_name.startswith('scheduler_')]
    return render(request, 'viewinfopage.html', {'tables': tables})

@login_required(login_url='/')
def createtable(request):
    return render(request,"createtimetable.html")






# loginlogout stuff
def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.success(request, 'Both Username and Password are required.')
                return redirect('/')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/')
        
        
            user = authenticate(username = username , password = password)
            
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/')
        
            login(request , user)
            return redirect('homepage')

                
            
            
    except Exception as e:
        print(e)
    return render(request , '/')




@login_required(login_url='/')
def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def prebuildinfo(request):
    if request.method == 'POST':
        batch = request.POST.get('batch')
        school = request.POST.get('school')
        division = request.POST.get('division')
        semester = request.POST.get('semester')
        nsubs = request.POST.get('nsubs')
        if not batch or not school or not semester or not nsubs or not division:
            messages.success(request, 'All fields are required.')
            return redirect('createtable')
        else:
            running_batch = runningbatches(batch=batch, school=school, division=division, semester=semester, nsubs=nsubs)
            running_batch.save()
            subs = []
            for i in range (int(nsubs)):
                subs.append(i)
            return render(request , 'prebuildinfo.html', {'subs': subs})
    return render(request , 'prebuildinfo.html')
        
@login_required(login_url='/')
def tablebuilder(request):
    if request.method == 'POST':
            # extract subject data from form
            n = (len(request.POST))//5
            subs = []
            fac1s = []
            fac2s = []
            fac3s = []
            rooms = []
            for i in range(int(n)):
                subs.append(request.POST.get(f'sub_code_{i}'))
                fac1s.append(request.POST.get(f'fac1_{i}'))
                fac2s.append(request.POST.get(f'fac2_{i}'))
                fac3s.append(request.POST.get(f'fac3_{i}'))
                rooms.append(request.POST.get(f'fac4_{i}'))
            # redirect to the subject list page
            return render(request , 'tablebuilder.html',{'subs':subs})
    return render(request , 'tablebuilder.html')