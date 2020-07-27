from django.shortcuts import render

# Create your views here.
from Country.models import Country
from Task_Type.models import Task_Type
from User.models import User
from timezone_details.models import Timezone_detail

def get_active_timezone():
    timezone = Timezone_detail.objects.filter(active='Y')
    return timezone

def welcome_timezone_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'timezone.html',
                  {"note": "Welcome to Timezone_detail Portal", "time": dummy_timezone(),"users":User.objects.all(),
                   "tasktypes": Task_Type.objects.all(),"countries":Country.objects.all(),"timezones": get_active_timezone()})


def get_list_timezone():
    return Timezone_detail.objects.all()


def dummy_timezone():
    return Timezone_detail(id=0,starttime=0,endtime=0)


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        taskid=int(req.POST["task"])
        userid=int(req.POST["user"])
        countryid = int(req.POST["country"])

        if taskid==0:
            msg="Task selection is mandetory..."
            return render(req, 'timezone.html',
                          {"time": Timezone_detail(id=req.POST["id"],starttime=req.POST["starttime"],endtime=req.POST["endtime"]),
                           "note": msg, "users":User.objects.all(),"tasktypes": Task_Type.objects.all(),
                           "countries":Country.objects.all(),"timezones": get_active_timezone()})
        elif userid==0:
            msg = "User selection is mandetory..."
            return render(req, 'timezone.html',
                          {"time": Timezone_detail(id=req.POST["id"], starttime=req.POST["starttime"],endtime=req.POST["endtime"]),
                           "note": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all(), "timezones": get_active_timezone()})
        elif countryid==0:
            msg = "Country selection is mandetory..."
            return render(req, 'timezone.html',
                      {"time": Timezone_detail(id=req.POST["id"], starttime=req.POST["starttime"],endtime=req.POST["endtime"]),
                       "note": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                       "countries": Country.objects.all(), "timezones": get_active_timezone()})

        if int(req.POST["id"]) > 0:
            timezone = Timezone_detail(id=req.POST["id"], starttime=req.POST["starttime"],endtime=req.POST["endtime"], tasktype=Task_Type.objects.get(id=taskid),
                                       country=Country.objects.get(id=countryid),user=User.objects.get(id=userid))
            msg = "Updation Operation Successfully...!"
            timezone.save()
        else:
            timezone = Timezone_detail(starttime=req.POST["starttime"],endtime=req.POST["endtime"], tasktype=Task_Type.objects.get(id=taskid),
                                       country=Country.objects.get(id=countryid),user=User.objects.get(id=userid))
            msg = "Add Operation Successfully...!"
            timezone.save()

    return render(req, 'timezone.html',
                  {"time": dummy_timezone(),
                   "note": msg, "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all(), "timezones": get_active_timezone()})


def delete_timezone(req, pid):
    timeobj = Timezone_detail.objects.get(id=pid)
    timeobj.active = 'N'
    timeobj.save()
    return render(req, 'timezone.html',
                  {"time": dummy_timezone(),
                   "note": "Timezone_detail Removed Successfully...!",
                   "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all(),
                   "timezones": get_active_timezone()})


def fetch_timezone(req, pid):
    timeobj = Timezone_detail.objects.get(id=pid)
    return render(req, 'timezone.html',
                  {"time": timeobj,
                   # "cat":prodob,
                   "note": "Timezone_detail Fetched Successfully...!",
                   "users": User.objects.all(), "tasktypes": Task_Type.objects.all(),
                           "countries": Country.objects.all(),"timezones": get_active_timezone() })
