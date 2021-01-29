from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .models import *
import json
from django.forms.models import model_to_dict
from .forms import StudentForm


def get_student_full_data(data):
    response_data={}

    response_data['name'] = data.__str__()
    
    school_id = data.school_id.school_id
    print("schoolid",school_id)
    book_id = data.book_id.book_id
    print("bookid",book_id)
    response_data['email'] = data.email
    response_data['gender'] = data.gender

    book_data = Book.objects.get(book_id=book_id)
    response_data['book_name'] = book_data.title
    response_data['page_number'] = book_data.pages

    school_data = School.objects.get(school_id=school_id)
    response_data['school_name'] = school_data.school_name
    response_data['school_phone'] = school_data.phone

    return response_data

def get_student_data_by_id(student_id):
    try:
        data = Student.objects.get(id=student_id)
        return data
    except Exception as e:
        print(e)
        return None

def get_student_by_name(fname,lname):
    try:
        data = Student.objects.get(first_name=fname,last_name=lname)
        return data
    except Exception as e:
        print(e)
        return None

def get_student_data(request,student_id:int):
    print("Studentid",student_id)

    data = get_student_data_by_id(student_id)
    if not data:
        return JsonResponse({"message":"Provided Student id does not exist"})
    
    response_data = get_student_full_data(data)
    
    print(response_data)
    return JsonResponse(response_data,content_type="application/json")

def load_search_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print("\n\n\n",form)
    else:
        form = StudentForm()
    
    return render(request,"student_details/student_form.html",{"form":form})

def get_student_data_from_form(request):
    try:
        fname = request.POST['first_name']
    except:
        fname = None
    
    try:
        lname = request.POST['last_name']
    except:
        lname = None
    
    try:
        student_id = request.POST['student_id']
    except:
        student_id = None
    
    if fname:
        data = get_student_by_name(fname,lname)
        if not data:
            if student_id:
                data = get_student_data_by_id(student_id)
                response_data = get_student_full_data(data)
                print(response_data)
                return JsonResponse(response_data,content_type="application/json")
                if not data:
                    return JsonResponse({"message":"Provided Student id's does not exist"})
            else:
                return JsonResponse({"message":"Provided Student Name's data does not exist"})
        else:
            response_data = get_student_full_data(data)
            
            print(response_data)
            return JsonResponse(response_data,content_type="application/json")
    elif student_id:
        data = get_student_data_by_id(student_id)
        if not data:
            return JsonResponse({"message":"Provided Student id's does not exist"})
        else:
            response_data = get_student_full_data(data)
            print(response_data)
            return JsonResponse(response_data,content_type="application/json")

def get_school_by_name(school_name):
    try:
        data = School.objects.get(school_name=school_name)
        return data
    except Exception as e:
        print(e)
        return None

def get_book_by_name(book_name):
    try:
        book = Book.objects.get(title=book_name)
        return book
    except:
        return None
    
def add_student_data(request):
    print(request.POST)
    school_data = get_school_by_name(request.POST['school'])
    
    book_data = get_book_by_name(request.POST['books'])
    

    print("making new entry")
    Student.objects.create(id=request.POST['ID'],
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email=request.POST['email'],
                            gender=request.POST['gender'],
                            book_id=book_data,
                            school_id=school_data)
    print("student created")

    return HttpResponse(request.POST.keys())