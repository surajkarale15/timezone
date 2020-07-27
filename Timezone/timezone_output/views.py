from django.shortcuts import render

# Create your views here.
from Country.models import Country
from Task_Type.models import Task_Type
from User.models import User
from timezone_details.models import Timezone_detail
from datetime import datetime

# def get_active_timezone():
#     timezone = Timezone_detail.objects.filter(active='Y')
#     return timezone

def welcome_timezone_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'timezone_output.html',
                  {"note": "Welcome to Timezone_detail Portal","users":User.objects.all(),
                   "tasktypes": Task_Type.objects.all(),"countries":Country.objects.all()})

'''
def get_list_timezone():
    return Timezone_detail.objects.all()


def dummy_timezone():
    return Timezone_detail(id=0,starttime=0,endtime=0)

'''

def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        taskid=int(req.POST["task"])
        userid=int(req.POST["user"])
        countryid = int(req.POST["country"])
        if taskid==0:
            msg="Task selection is mandetory..."
            return render(req, 'timezone_output.html',
                          {"time": Timezone_detail(id=req.POST["id"]),
                           "note": msg, "users":User.objects.all(),"tasktypes": Task_Type.objects.all(),
                           "countries":Country.objects.all()})
        elif userid==0:
            msg = "User selection is mandetory..."
            return render(req, 'timezone_output.html',
                          {"time": Timezone_detail(id=req.POST["id"]),
                           "note": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all()})
        elif countryid==0:
            msg = "Country selection is mandetory..."
            return render(req, 'timezone_output.html',
                      {"time": Timezone_detail(id=req.POST["id"]),
                       "note": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                       "countries": Country.objects.all()})


        starttime=Timezone_detail.objects.filter(tasktype_id=taskid,user_id=userid,country_id=countryid).values('starttime')
        endtime = Timezone_detail.objects.filter(tasktype_id=taskid, user_id=userid, country_id=countryid).values('endtime')

        start=0
        end=0
        if starttime and endtime:

            for i in starttime:
                 print(i['starttime'])
                 start=i['starttime']

            for i in endtime:
                 print(i['endtime'])
                 end=i['endtime']
                # print()

        current_time = datetime.now().time()  # time object

        print("now =", current_time)
        print("type(now) =", type(current_time))

        if current_time>start and current_time<end:
            msg='True'
        elif current_time<start:
            msg=start
        else:
            msg='False'








    return render(req, 'timezone_output.html',
                  {
                   "disp": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all()})
