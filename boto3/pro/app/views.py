from multiprocessing import context
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Profile, TextCapForm,Mask
from .face import compare_faces
from .textcap import detect_text
from .mask import detect_labels
from .models import ProfileFace
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES)  
        if form.is_valid():  
            
            picture1=form.cleaned_data['picture1']
            picture2=form.cleaned_data['picture2']
            source_file = picture1
            # target_file='aws.jpg'
            target2_file = picture2

            face_matches = compare_faces(source_file, target2_file)
            print("Face matches: " + str(face_matches))
            print("here is picture 1 input :" , picture1)
            output=int(face_matches)
            # obj=ProfileFace(picture1=picture1,picture2=picture2)
            # obj.save()
            return render(request, 'result.html',{'res':output})
          
    else:  
        form = Profile()  
  
    return render(request, 'home.html', {'form': form})

def text_capture(request):
    if request.method=="POST":
        form=TextCapForm(request.POST, request.FILES)
        if form.is_valid():
            pic1=form.cleaned_data['pic1']
            bucket=''
            photo=pic1
            text_count=detect_text(photo,bucket)
            print("Text detected: " + str(text_count))
            text_count=str(text_count)
            list1=detect_text.list1

            
            return render(request,'textcapture/textresult.html',{'output':text_count,'list1':list1})
        
    else:
        form=TextCapForm()
    return render(request,'textcapture/textcap.html',{'form':form})

def maskdetect(request):
    if request.method=="POST":
        form=Mask(request.POST, request.FILES)
        if form.is_valid():
            pic1=form.cleaned_data['pic1']
            
            photo=pic1
            bucket=''
            person_count=detect_labels(photo)
            # response=detect_labels.resp
            #test
            list1=detect_labels.informations
            return render(request,'maskdetect/result.html',{'list1':list1})
        
    else:
        form=Mask()
    return render(request,'maskdetect/mask_home.html',{'form':form})