from django.shortcuts import render

# Create your views here.

from Task_Type.models import Task_Type

def get_active_tasktype():
    tasktype = Task_Type.objects.filter(active='Y')
    return tasktype

def welcome_tasktype_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'tasktype.html',
                  {"note": "Welcome to Task_Type Portal", "task": dummy_tasktype(), "tasktypes": get_active_tasktype()})


def get_list_tasktype():
    return Task_Type.objects.all()


def dummy_tasktype():
    return Task_Type(id=0, type='')


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        if int(req.POST["id"]) > 0:
            tasktype = Task_Type(id=req.POST["id"], type=req.POST["type"])
            msg = "Updation Operation Successfully...!"
            tasktype.save()
        else:
            tasktype = Task_Type(type=req.POST["type"])
            msg = "Add Operation Successfully...!"
            tasktype.save()

    return render(req, 'tasktype.html',
                  {"task": dummy_tasktype(),
                   "note": msg, "tasktypes": get_active_tasktype()})


def delete_tasktype(req, cid):
    taskobj = Task_Type.objects.get(id=cid)
    taskobj.active = 'N'
    taskobj.save()
    return render(req, 'tasktype.html',
                  {"task": dummy_tasktype(),
                   "note": "Task_Type Removed Successfully...!",
                   "tasktypes": get_active_tasktype()})


def fetch_tasktype(req, cid):
    taskobj = Task_Type.objects.get(id=cid)
    return render(req, 'tasktype.html',
                  {"task": taskobj,
                   "note": "Task_Type Fetched Successfully...!"
                      , "tasktypes": get_active_tasktype()})
