from django.shortcuts import render

# Create your views here.

from Country.models import Country

def get_active_country():
    country = Country.objects.filter(active='Y')
    return country

def welcome_country_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'country.html',
                  {"note": "Welcome to Country Portal", "country": dummy_country(), "countries": get_active_country()})


def get_list_country():
    return Country.objects.all()


def dummy_country():
    return Country(id=0, country_name='')


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        if int(req.POST["id"]) > 0:
            country = Country(id=req.POST["id"], country_name=req.POST["country_name"])
            msg = "Updation Operation Successfully...!"
            country.save()
        else:
            country = Country(country_name=req.POST["country_name"])
            msg = "Add Operation Successfully...!"
            country.save()

    return render(req, 'country.html',
                  {"country": dummy_country(),
                   "note": msg, "countries": get_active_country()})


def delete_country(req, cid):
    countryobj = Country.objects.get(id=cid)
    countryobj.active = 'N'
    countryobj.save()
    return render(req, 'country.html',
                  {"country": dummy_country(),
                   "note": "Country Removed Successfully...!",
                   "countries": get_active_country()})


def fetch_country(req, cid):
    countryobj = Country.objects.get(id=cid)
    return render(req, 'country.html',
                  {"country": countryobj,
                   "note": "Country Fetched Successfully...!"
                      , "countries": get_active_country()})
