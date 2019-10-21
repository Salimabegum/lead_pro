from django.shortcuts import render,redirect
from .models import Register, Joining
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout

# Create your views here.

def homepage(request):
	return render(request,'homepage.html')


def single_data(request):
	data =Register.objects.get(id=id)
	return render(request,'single_data.html',{'details':data})	

def register(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Email = request.POST['Email']
		Phone_no = request.POST['Phone_no']
		Course = request.POST['Course']
		Source = request.POST['Source']
		Leadstatus = request.POST['Leadstatus']
		Date_demo = request.POST['Date_demo']
		Counsler = request.POST['Counsler']
		Remark = request.POST['Remark']
		Register.objects.create(Name=Name,Email=Email,Phone_no=Phone_no,Course=Course,Source=Source,
		Leadstatus=Leadstatus,Date_demo=Date_demo,Counsler=Counsler,Remark=Remark)
		return redirect('walkins')
	return render(request,'Register.html')

def walkins(request):
	data = Register.objects.all()
	return render(request,'walkins.html',{'details':data})

def Calling(request):
	return render(request,'Calling.html')

def Calling1(request):
	if request.method == "POST":
		Course = request.POST['Course']
		Date_demo = request.POST['Date_demo']
		register = Register.objects.filter(Course=Course,Date_demo=Date_demo)
		return render(request, 'Calling1.html', {'details':register})
	return render(request, 'Calling1.html')

def Counselling(request):
	return render(request,'Counselling.html')

def Counselling1(request):
	if request.method == "POST":
		Date_demo = request.POST['Date_demo']
		Course = request.POST['Course']
		regular = Register.objects.filter(Date_demo=Date_demo,Course=Course)
		return render(request, 'Counselling1.html',{'details':regular})
	return render(request, 'Counselling1.html')	

def edit(request, id):  
   form = Register.objects.get(id=id)
   return render(request,'edit.html', {'details':form})

def update(request, id):
    form = Register.objects.get(id=id)
    if request.method == "POST":
    	Name = request.POST['Name']
    	Date_demo = request.POST['Date_demo']
    	form.Name = Name
    	form.Date_demo = Date_demo
    	form.save()
    	return redirect("walkins")
    return render(request, 'edit.html', {'details': form})

def destroy(request, id):
	form = Register.objects.get(id=id)
	form.delete()
	return redirect('walkins')


def join(request):
	if request.method == "POST":
		name = request.POST['name']
		course = request.POST['course']
		Completion_Date = request.POST['Completion_Date']
		Date_joining = request.POST['Date_joining']
		Aadhar_no = request.POST['Aadhar_no']
		Instructor = request.POST['Instructor']	
		Course_fee = request.POST['Course_fee']	
		email = request.POST['email']
		phone_no = request.POST['phone_no']
		remark = request.POST['remark']
		status = request.POST['status']
		Joining.objects.create(name=name,course=course,Completion_Date=Completion_Date,Date_joining=Date_joining,
			Aadhar_no=Aadhar_no,Instructor=Instructor,Course_fee=Course_fee,email=email,phone_no=phone_no,remark=remark,status=status)
		return redirect('current')
	return render(request,'joining.html')

def current(request):
	data = Joining.objects.all()
	return render(request, 'current.html',{'details':data})	

# def status(request,id):
# 	data = Joining.objects.get(id=id)
# 	data.status = 'completed'
# 	data.save()
# 	return render(request, 'current.html',{'details':data})

# def discontinue(request):
# 	data = Joining.objects.get(id=id)

# 	return render(request,'Students.html',{'dis':data})

# def complete(request,id):
# 	data = Joining.objects.get(id=id)
# 	return render(request, 'Students.html',{'com':data})

# def delay(request):
# 	data = 	Joining.objects.get(id=id)
# 	return render(request, 'Students.html',{'del':data})

# def students(request):
# 	if



# def update1(request,id):
# 	data = Joining.objects.all()	
# 	if request.method=="POST":
# 		stud = Joining.objects.get(pk= id)
# 		if request.POST['comp'] == 'COMPLETE':
# 			stud.status='COMPLETE'
# 			stud.save()
# 			return redirect('Students')
# 		elif request.POST['delay'] == 'Delay':
# 			stud.status='Delay'
# 			stud.save()
# 			return redirect('Students')
# 		else:
# 			stud.status='rejoin'
# 			stud.save()
# 			return redirect('Students')	
# 	return render(request,'Students.html',{'details1':stud})


def complete(request,id):
	data=Joining.objects.get(id=id)
	data.status="complete"
	data.save()
	return redirect('Students')

def delay(reques,id):
	data=Joining.objects.get(id=id)
	data.status="delay"
	data.save()
	return redirect('Students')

def rejoin(request,id):
	data = Joining.objects.get(id=id)
	data.status="stoped"
	data.save()
	return redirect('Students')	

def edit1(request,id):
	data=Joining.objects.get(id=id)
	return render(request,'edit1.html',{'details1':data})	

def Students(request):
	cdata = Joining.objects.filter(status='complete')
	ddata = Joining.objects.filter(status='delay')
	sdata = Joining.objects.filter(status='stoped')
	return render(request,'Students.html',{'details1':cdata,'details2':ddata,'details3':sdata})


def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			return redirect('homepage')
		else:
			return HttpResponse('Credentials does not match!')	
	return render(request,'home/login.html')


def logout_user(request):
	logout(request)
	return redirect('login_user')

