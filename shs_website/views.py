from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from datetime import datetime
from .models import NotificationsModel, EventDetail, AddFacultyModel, \
    Post



# Create your views here.

def index(request):
    obj_notification = NotificationsModel.objects.all()
    obj_EventDetail = EventDetail.objects.all()
    CurrentDate = datetime.now()
    EventDetail.objects.filter(EventDate__lt=CurrentDate).delete()
    context = {
        'Notifications': obj_notification,
        'EventDetail': obj_EventDetail
    }
    return render(request, 'home.html', context)

def aboutus(request):
    return render(request, 'aboutus.html')

def ChairmenDesk(request):
    return render(request, 'ChairmenDesk.html')

def PrincipalDesk(request):
    return render(request, 'PrincipalDesk.html')

def admission_procedure(request):
    return render(request, 'admission_procedure.html')

def faculty(request):
    ObjStaffData = AddFacultyModel.objects.all()
    context = {
        'StaffData': ObjStaffData
    }
    return render(request, 'faculty.html', context)

def AddNewFaculty(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Name = request.POST.get("name")
            Qualification =  request.POST.get("qualification")
            Subject = request.POST.get("subject")
            objAddFaculty = AddFacultyModel(StaffName=Name, StaffQualification=Qualification, Subject=Subject)
            objAddFaculty.save()
            return redirect(faculty)
        else:
            return render(request, 'AddNewFaculty.html')
    else:
        return redirect(log_in)

def EditFaculty(request):
    if request.method == "GET" and request.GET.get('id'):
        id = request.GET.get('id')
        ObjStaffData = AddFacultyModel.objects.get(id=id)
        context = {
            'OStaffData': ObjStaffData
        }
        return render(request, 'EditFaculty.html', context)
    else:
        return redirect(faculty)

def DeleteFaculty(request):
    id = request.GET.get('id')
    objDeleteFaculty = AddFacultyModel.objects.get(id=id)
    objDeleteFaculty.delete()
    return redirect(faculty)

def UpdateRecord(request):
    if request.method == "POST":
        id = request.POST.get('update_id')
        OStaffData = AddFacultyModel.objects.get(id=id)
        OStaffData.StaffName = request.POST.get("name")
        OStaffData.StaffQualification = request.POST.get("qualification")
        OStaffData.Subject = request.POST.get("subject")
        OStaffData.save()
    return redirect(faculty)



def admission_enquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ChildName = request.POST.get("ChildName")
        ChildAge = request.POST.get("ChildAge")
        Class = request.POST.get("class")
        # contact_detail = [name, phone, email, message]
        # contact_detail = list(contact_detail[0])
        enquiry_detail = 'Name: ' + name + '\n' + 'Phone: ' + str(phone) + '\n' + 'Email: ' + str(
            email) + '\n' + 'Child Name:' + ChildName + '\n' + 'Child Age:' + ChildAge + '\n' + 'Class:' + Class + '\n' 'message: ' + message
        send_mail(
            'Enquiry For Admission',
            enquiry_detail,
            'highschoolsarvodaya@gmail.com',
            ['pankajtewatia1982@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Enquiry details Sent Successfully.')
        return render(request, 'enquiry_form.html', {})
    else:
        return render(request, 'enquiry_form.html', {})

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # contact_detail = [name, phone, email, message]
        # contact_detail = list(contact_detail[0])
        contact_detail = 'Name: ' + name + '\n' + 'Phone: ' + str(phone) + '\n' + 'Email: ' + str(
            email) + '\n' + 'Message: ' + message
        send_mail(
            'Contact Detail of Visitor',
            contact_detail,
            'highschoolsarvodaya@gmail.com',
            ['pankajtewatia1982@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Profile details Sent Successfully.')
        return render(request, 'contactus.html', {})
    else:
        return render(request, 'contactus.html', {})

def log_in(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # return render(request, 'index.html')
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Invalid Credentials!!!!")
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

def log_out(request):
    auth.logout(request)
    return render(request, 'login.html')

def notifications(request):
    if request.method == "POST":
        Notifications = request.POST.get("Notification")
        NotificationsDetail = NotificationsModel(notifications=Notifications)
        NotificationsDetail.save()
        return HttpResponseRedirect('/')

def DeleteNotification(request):
    N_ID = request.GET.get('id')
    ObjNotification = NotificationsModel.objects.get(id=N_ID.strip())
    ObjNotification.delete()
    return HttpResponseRedirect('/')

def event_detail(request):
    if request.method == "POST":
        EventName = request.POST.get("EventName")
        EventDate = request.POST.get("EventDate")
        Event_Detail = EventDetail(EventName=EventName, EventDate=EventDate)
        Event_Detail.save()
    return HttpResponseRedirect('/')

def DeleteEvent(request):
    id = request.GET.get('id')
    ObjDeleteEvent = EventDetail.objects.get(id=id)
    ObjDeleteEvent.delete()
    return redirect(index)

def AddPost(request):
    if request.method == "POST" and request.FILES:
        Title = request.POST.get("title")
        Body = request.POST.get("body")
        Images = request.FILES.getlist("img[]")
        EventDetail = Post(Title=Title, Body=Body, Images=Images)
        EventDetail.save()
        return redirect(gallery)
    return render(request, 'AddPost.html')

def gallery(request):
    GalleryData = Post.objects.all()
    context = {
        'Data': GalleryData
    }
    return render(request, 'gallery.html', context)

def career(request):
    if request.method == 'POST' and request.FILES:
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        PostA = request.POST.get('post')
        Qual = request.POST.get('qualification')
        Exp = request.POST.get('exp')
        AS = request.POST.get('as')
        resume = request.FILES['resume']
        pankaj = 'pankajtewatia1982@gmail.com'
        Application = 'Name: '+Name+'\n'+'Email: '+Email+'\n'+'Phone: '+Phone+'\n'+'Applied for: '+PostA+'\n'+'Qualification: '+Qual+'\n'+'Total Experience: '+Exp+'\n'+'Area of Specialization: '+AS
        Subject = 'Application for Job!!!'
        mail = EmailMessage(Subject, Application, settings.EMAIL_HOST_USER, [pankaj])
        mail.attach(resume.resume, resume.read(), resume.content_type)
        mail.send()

    return render(request, "career.html")

def Test(request):
    if request.method == "POST" and request.FILES:
        Title = request.POST.get("title")
        Body = request.POST.get("body")
        Images = request.FILES.getlist("img[]")
        EventDetail = Post(Title=Title, Body=Body)
        EventDetail.save()
        for i in Images:
            images = Post(Images=i)
            images.save()
        return redirect(Test)
    ObjPost = Post.objects.all()
    ObjImage = Post.objects.only('Images')
    context = {
        'Post': ObjPost,
        'Images': ObjImage
    }
    return render(request, 'Test.html', context)
