from django.shortcuts import render


from app.models import *

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def courses(request):
    return render(request, 'app/courses.html')

def register(request):
    return render(request, 'app/register.html')

def login(request):
    return render(request, 'app/login.html')

def contact(request):
    return render(request, 'app/contact.html')

def firstyear(request):
    return render(request, 'app/firstyear.html')

def ourteam(request):
    return render(request, 'app/ourteam.html')

def IT2(request):
    return render(request, 'app/IT2.html')

def IT3(request):
    return render(request, 'app/IT3.html')

def civil2(request):
    return render(request, 'app/civil2.html')

def civil3(request):
    return render(request, 'app/civil3.html')

def civil4(request):
    return render(request, 'app/civil4.html')

def electrical2(request):
    return render(request, 'app/electrical2.html')

def electrical3(request):
    return render(request, 'app/electrical3.html')

def electrical4(request):
    return render(request, 'app/electrical4.html')

def IT4(request):
    return render(request, 'app/IT4.html')

def IT4(request):
    return render(request, 'app/IT4.html')

def chemistry(request):
    return render(request, 'app/chemistry.html')

def Physics(request):
    return render(request, 'app/Physics.html')

def maths1(request):
    return render(request, 'app/maths1.html')

def maths2(request):
    return render(request, 'app/maths2.html')

def basic_electrical(request):
    return render(request, 'app/basic_electrical.html')

def AI(request):
    return render(request, 'app/AI.html')

def ET(request):
    return render(request, 'app/ET.html')

def mechanical(request):
    return render(request, 'app/mechanical.html')

def softskill(request):
    return render(request, 'app/softskill.html')



def pps(request):
    return render(request, 'app/pps.html')

def electronics(request):
    return render(request, 'app/electronics.html')

def register(request):
    return render(request,'app/register.html')

def ds(request):
    return render(request,'app/ds.html')

def coa(request):
    return render(request,'app/coa.html')

def maths4(request):
    return render(request,'app/maths4.html')

def discrete(request):
    return render(request,'app/discrete.html')

def python(request):
    return render(request,'app/python.html')

def uhv(request):
    return render(request,'app/uhv.html')

def toa(request):
    return render(request,'app/toa.html')

def os(request):
    return render(request,'app/os.html')

def mp(request):
    return render(request,'app/mp.html')

def esc(request):
    return render(request,'app/esc.html')

def css(request):
    return render(request,'app/css.html')


def login(request):
    return render(request,'app/login.html')

#view for registration
def userRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

#first wew will validate that user already exist
user = USER.objects.filter(Email=emails)
