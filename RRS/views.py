from django.shortcuts import render,HttpResponse,redirect
from RRS.models import Contact,LYF
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request , "RRS/index.html")
def lyf(request):
    if request.method == 'POST':
        OwnerName = request.POST['OwnerName']
        RoomTitle = request.POST['RoomTitle']
        OwnerNumber = request.POST['OwnerNumber']
        OwnerEmail = request.POST['OwnerEmail']
        OwnerPostalCode = request.POST['OwnerPostalCode']
        OwnerAddress = request.POST['OwnerAddress']
        OwnerPrice = request.POST['OwnerPrice']
        OwnerRooms = request.POST['OwnerRooms']
        Flooring = request.POST['Flooring']
        Floor = request.POST['Floor']
        TOB = request.POST['TOB']
        Hall = request.POST['Hall']
        Bedroom_1 = request.POST['Bedroom_1']
        Bedroom_2 = request.POST['Bedroom_2']
        Bedroom_3 = request.POST['Bedroom_3']
        Kitchen = request.POST['Kitchen']
        Bathroom = request.POST['Bathroom']
        print(OwnerName,OwnerEmail,OwnerNumber,OwnerAddress,OwnerPrice,OwnerRooms,Hall, TOB, Flooring , Bedroom_1, Bedroom_2, Floor, Bedroom_3, Kitchen,Bathroom)
        if len(OwnerPostalCode)>6:
            messages.error(request, 'Incorrect Postal Code')
            return redirect('/')
        else:
            lyf= LYF(OwnerName=OwnerName,RoomTitle=RoomTitle, OwnerEmail=OwnerEmail, OwnerNumber=OwnerNumber, OwnerPostalCode = OwnerPostalCode,OwnerAddress= OwnerAddress, OwnerPrice=OwnerPrice,OwnerRooms=OwnerRooms,Flooring=Flooring, Floor=Floor, TOB=TOB, Hall=Hall, Bedroom_1=Bedroom_1,Bedroom_2=Bedroom_2, Bedroom_3=Bedroom_3, Kitchen=Kitchen, Bathroom=Bathroom)
            lyf.save()                
            messages.success(request, 'Thanks For Upload Your Flat Or Room Here')
        return redirect('/')
    return HttpResponse("Not Working or Coming from ")
def search(request):
    return render(request , "RRS/search.html")
def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Checksome
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exist')
            return redirect('/')
        if len(username)>15:
            messages.error(request, 'Username must be less than 15 character')
            return redirect('/')
        if not username.isalnum():
                messages.error(request, 'Username must be only contain letters and number')
                return redirect('/')
        
        if len(pass1) < 6 or len(pass1) > 15:
            messages.error(request, 'Please enter a password that is between 6 to 15 character')
            return redirect('/')
        if pass1.isalnum():
            messages.error(request, 'please enter a password that contains atleast 1 symbol(ex: @!#$%^&*)')
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, 'Your Password does not match please try again')
            return redirect('/')
        # create the user
        myuser = User.objects.create_user(username, email , pass1 )
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your TechBhaiya account has been created successfully ' + myuser.username)
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')

def handleLogIn(request):
    if request.method == 'POST':
        logInusername = request.POST['logInusername']
        logInpass = request.POST['logInpass']

        user = authenticate(username=logInusername, password=logInpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('/')

        else:
            messages.error(request, 'Your Username and Password doesnot match')
            return redirect('/')
def handleLogOut(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')

def wishlist(request):
    return render(request , "RRS/wishlist.html")
def services(request):
    return render(request , "RRS/services.html")
def about(request):
    return render(request , "RRS/about.html")
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10 or len(phone)>13:
            messages.error(request, 'Please Enter The Correct Details')

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Thanks For Your Valuable Openion')

    return render(request , "RRS/contact.html")
def help(request):
    return render(request , "RRS/help.html")
def logOut(request):
    return HttpResponse("logOut")