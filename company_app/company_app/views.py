from django.shortcuts import render
from home.models import AddEmployee
from device.models import Device
from django.template import loader
def homePage(request):
    employees = AddEmployee.objects.all()
    return render(request,"index.html",{'employees':employees})

def addEmployee(request):
    if request.method == "POST":
        name = request.POST['name']
        employee_id = request.POST['employee_id']
        ins = AddEmployee(name = name, employee_id = employee_id)
        ins.save()
        print("The data has been saved")
    return render(request,"addEmployee.html")

def addDevice(request):
    if request.method == "POST":
        employee_id = request.POST['employee_id']
        employee_name = request.POST['employee_name']
        device_name = request.POST['device_name']
        issue_date = request.POST['issue_date']
        return_date = request.POST['return_date']
        ins = Device(employee_id = employee_id, 
                     employee_name = employee_name,
                     device_name = device_name,
                     issue_date = issue_date,
                     return_date = return_date,
                     )
        ins.save()
        print("The data has been saved")
    return render(request,"addDevice.html")

def viewDevice(request):
    devices = Device.objects.all()
    return render(request,"viewDevice.html",{'devices':devices})