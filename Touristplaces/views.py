
from django.shortcuts import render
from Touristplaces.models import aboutap,aboutimages
from Touristplaces.models import place1,place1images,place1video
from Touristplaces.models import place2,place2images,place2video
# Create your views here.
def welcome(request):
    return render(request,'home.html')
def main(request):
    return render(request,'main.html')
def about(request):
    data=aboutap.objects.all()
    imgdata1=aboutimages.objects.all()

    my_dict={'data':data,'imgdata1':imgdata1}
    return render(request,'about.html',context=my_dict)
def tplace1(request):
    data2=place1.objects.all()
    image1=place1images.objects.all()
    videodata2=place1video.objects.all()
    my_dict1={'data2':data2,'image1':image1,'videodata2':videodata2}
    return render(request,'places/place1.html',context=my_dict1)
def tplace2(request):
    data2=place2.objects.all()
    image1=place2images.objects.all()
    videodata2=place2video.objects.all()
    my_dict1={'data2':data2,'image1':image1,'videodata2':videodata2}
    return render(request,'places/place2.html',context=my_dict1)
def aboutme(request):
    return render(request,'aboutme.html')
