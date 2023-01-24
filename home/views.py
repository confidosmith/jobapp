from django.shortcuts import redirect, render
from email import message
from django.http import HttpResponse
from django.db.models import Q
from home.models import Listjob
from django.contrib import messages
from home.forms import *
from home.models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from userprofile.forms import *
from userprofile.models import *
from home.views import * 
from .forms import *
# Create your views here.

def home(request):
    featured = Listjob.objects.filter(featured=True)

    context = {
        'featured':featured 
    }

    return render(request,'index.html', context)

def search(request):
    if request.method == 'POST':
        item = request.POST['search']
        search = Q(Q(tags__icontains=item)|Q(job_title__icontains=item)|Q(job_location__icontains=item))
        search_item = Listjob.objects.filter(search)

        context = {
            'search_item':search_item,
            'item':item 
        }
        return render(request,'search.html',context)
    else:
        return render(request,'search.html')
    

def job_listing(request):
    published = Listjob.objects.all().filter(published=True).order_by('-posted_at')
    p = Paginator(published, 6)
    page= request.GET.get('page')
    paginate = p.get_page(page)

    context = {
        'paginate':paginate
    }

    return render(request,'joblisting.html', context)


def job_detail(request,id):
    detail = Listjob.objects.get(pk=id)
    # profile = User.objects.get(username = request.user.username)
    # restricted = EmployeeProfile.objects.get(user__username = request.user.username)
    listjab = Listjob.objects.all()

    context = {
        'detail':detail, 
        # 'profile':profile,
        'listjab':listjab,
        # 'restricted':restricted,
    }

    return render(request, 'jobdetail.html', context)



def employer_signup(request):
    employerform = EmployerSignupForm()
    if request.method == 'POST':
        logo = request.POST['logo']
        website = request.POST['website']
        phone = request.POST['phone']
        employerform = EmployerSignupForm(request.POST)
        if employerform.is_valid():
            muser = employerform.save()
            newmuser = EmployerProfile(company = muser)
            newmuser.email = muser.email
            newmuser.logo = logo 
            newmuser.website = website 
            newmuser.phone = phone
            newmuser.save()
            login(request,muser)
            messages.success(request, f'Congratulations {muser.username} Your Registration is Successful')
            return redirect('home')
        else:
            messages.error(request, employerform.errors)
            return redirect('employer_signup')

    return render(request, 'employer_signup.html')

def employee_signup(request):
    employeeform = EmployeeSignupForm()
    if request.method == 'POST':
        gender = request.POST['gender']
        employeeform = EmployeeSignupForm(request.POST)
        if employeeform.is_valid():
            euser = employeeform.save()
            neweuser = EmployeeProfile(user = euser)
            neweuser.gender = gender 
            neweuser.first_name = euser.first_name
            neweuser.last_name = euser.last_name
            neweuser.email = euser.email
            neweuser.save()
            login(request,euser)
            messages.success(request, f'Congratulations {euser.username} Your Registration is Successful')
            return redirect('home')
        else:
            messages.error(request, employeeform.errors)
            return redirect('employee_signup')
    return render(request, 'employee_signup.html')

def signout(request):
    logout(request)
    messages.success(request,'You are now signed out')
    return redirect('signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You are now signed in')
            return redirect('home')
        else:
            messages.info(request, 'The Email/Password is incorrect please try again with the correct details')
            return redirect('signin')
    return render(request, 'login.html')



def post_job(request):
    form = ListjobForm()
    if request.method == 'POST':
        logo = request.POST['logo']
        form = ListjobForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.employer = request.user.employerprofile
            post.logo = logo
            post.save()
            messages.success(request, 'you have successfully posted a job and it is under review')
            return redirect('employer_dashboard')
        else:
            messages.error(request, form.errors)
            return redirect('post_job')

    return render(request, 'postjob.html',{'form':form})



@login_required(login_url='signin')
def job_apply(request,id):
    apply = Listjob.objects.get(pk=id)

    context = {
        'apply':apply 
    }
    return render(request, 'jobapply.html', context)


def newapply(request):
    newform = ApplicantForm()
    if request.method == 'POST':
        newform = ApplicantForm(request.POST, request.FILES)
        if newform.is_valid():
            newapplicant = newform.save(commit=False)
            newapplicant.employee =  request.user.employeeprofile
            newapplicant.save()
            messages.success(request, 'success')
            return redirect('home')
        else:
            messages.error(request, newform.errors)
            return redirect('job_listing')
    return render(request, 'jobdetail.html')



def employer_dashboard(request):
    posting = request.user.employerprofile
    poster = EmployerProfile.objects.get(company__username = request.user.username)
    jobvac = Listjob.objects.filter(employer = posting, display=True).order_by('-posted_at')
    p = Paginator(jobvac, 5)
    page= request.GET.get('page')
    paginate = p.get_page(page)


    context = {
        'jobvac':jobvac,
        'poster':poster,
        'paginate':paginate
    }

    return render(request, 'employer_dashboard.html', context)


def employee_dashboard(request):
    seeking = request.user.employeeprofile
    seeker = EmployeeProfile.objects.get(user__username = request.user.username)
    apply = Application.objects.filter(employee = seeking)

    return render(request, 'employee_dashboard.html', {'seeker':seeker, 'apply':apply})

def delete(request):
    if request.method == 'POST':
        jobpost = request.POST['post_id']
        del_post = Listjob.objects.filter(pk=jobpost)
        for item in del_post:
            item.display = False
            item.save()
        messages.success(request,'one job post successfully deleted')
        return redirect('employer_dashboard')

def employeedelete(request):
    if request.method == 'POST':
        apply_id = request.POST['apply_id']
        del_apply = Application.objects.filter(pk=apply_id).delete()
        messages.success(request,'one job application successfully deleted')
        return redirect('employee_dashboard')

def applicant(request):
    applicant = request.POST['applicant']
    all_apply = Application.objects.filter(listjob__icontains = applicant)
    poster = EmployerProfile.objects.get(company__username = request.user.username)

    context = {
        'all_apply':all_apply,
        'poster':poster
    }
    return render(request,'applicants.html', context)

def application_details(request):
    applydet = request.POST['applicant']
    apply = Application.objects.get(pk = applydet)
    poster = EmployerProfile.objects.get(company__username = request.user.username)

    context = {
        'apply':apply,
        'poster':poster
    }
    return render(request,'application_details.html', context)

def update(request):
    profile = EmployeeProfile.objects.get(user__username=request.user.username)
    form = EmployeeProfileForm(instance=request.user.employeeprofile)
    if request.method == 'POST':
        form =EmployeeProfileForm(request.POST, request.FILES, instance=request.user.employeeprofile)
        if form.is_valid():
            user = form.save()
            new = user.first_name.title()
            messages.success(request, f'Dear {new}, your profile update is successful')
            return redirect('employee_dashboard')
        else:
            new = user.first_name.title()
            messages.error(request,f'Dear {new}, your profile update generated the following errors: {form.errors}')
            return redirect('update')

    context = {
        'form':form,
        'profile':profile
    }

    return render(request, 'update.html', context)