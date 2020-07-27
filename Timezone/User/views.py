from django.shortcuts import render

# Create your views here.

from User.models import User

def get_active_user():
    user = User.objects.filter(active='Y')
    return user

def welcome_user_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'user.html',
                  {"note": "Welcome to User Portal", "user_nm": dummy_user(), "users": get_active_user()})


def get_list_user():
    return User.objects.all()


def dummy_user():
    return User(id=0, name='')


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        if int(req.POST["id"]) > 0:
            user = User(id=req.POST["id"], name=req.POST["name"])
            msg = "Updation Operation Successfully...!"
            user.save()
        else:
            user = User(name=req.POST["name"])
            msg = "Add Operation Successfully...!"
            user.save()

    return render(req, 'user.html',
                  {"user_nm": dummy_user(),
                   "note": msg, "users": get_active_user()})


def delete_user(req, cid):
    user = User.objects.get(id=cid)
    user.active = 'N'
    user.save()
    return render(req, 'user.html',
                  {"user_nm": dummy_user(),
                   "note": "User Removed Successfully...!",
                   "users": get_active_user()})


def fetch_user(req, cid):
    user = User.objects.get(id=cid)
    return render(req, 'user.html',
                  {"user_nm": user,
                   "note": "User Fetched Successfully...!"
                      , "users": get_active_user()})
