from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
from django.db import connection
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    donor = Donor.objects.raw("select * from donate_donor where user_id = "+str(user.id))
                    args = {'donor':request.user.donor}

                    return render(request, 'donor_dashboard.html',args)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'home.html', {'form': form})
    # return render(request,'home.html')

def donor_reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Donor.objects.create(user=new_user)
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/donor_edit/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
        else:
            return HttpResponse('error')
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)

@login_required
def donor_edit(request):
    if request.method == 'POST':
        donor = Donor.objects.raw("select * from donate_donor where user_id = "+str(request.user.id))
        form = DonorForm(request.POST,instance = request.user.donor)
        # print(form)
        if form.is_valid():
            user = request.user
            form.save()
            return render(request,'donor_dashboard.html',{'donor':request.user.donor})
        else:
            return HttpResponse('Error, Donor not registered')

    else:
        form = DonorForm(instance=request.user.donor)
        args = {'form':form}
        return render(request,'donor_reg.html',args)


def donor_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    donor = Donor.objects.raw("select * from donate_donor where user_id = "+str(user.id))
                    return render(request, 'donor_dashboard.html',{'donor':user.donor})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'donor_login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

def patient_reg(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thankyou.html')
        else:
            return HttpResponse('Error, Donor not registered')

    else:
        form = PatientForm()
        args = {'form':form}
        return render(request,'patient_reg.html',args)

def view_donor(request):
    bloodbanks = BloodBank.objects.raw("select * from donate_bloodbank")
    donors = Donor.objects.raw("select * from donate_donor")
    args = {
        'blood_banks':bloodbanks,
        'donors':donors,
    }
    return render(request,'view_donor.html',args)

def view_donor_bg(request):
    blood_group = request.POST['Blood Groups']
    if blood_group == "all":
        donors = Donor.objects.raw("select * from donate_donor")
    else:
        sql = "select * from donate_donor where blood_group="+"'"+blood_group+"'"
        donors = Donor.objects.raw(sql)

    args = {
        'blood_banks':BloodBank.objects.raw("select * from donate_bloodbank"),
        'donors':donors,
        'selected':blood_group
    }
    return render(request,'view_donor.html',args)