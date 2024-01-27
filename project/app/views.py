from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.

def home(request):
    # images = Image.objects.all()
    images = Image.objects.exclude(img__exact='').all()
    return render(request, "gallery.html", {'images': images})


def home2(request):
    videos = Video.objects.all()
    return render(request, "videos.html", {'videos': videos})


def add(request):
    images = Image.objects.exclude(img__exact='').all()
    videos = Video.objects.all()
    return render(request, "add.html", {'images': images, 'videos': videos})


def addim(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        img = Image(img=image)
        img.save()
        return redirect('app:add')
    return render(request, "add.html")


def addv(request):
    if request.method == 'POST':
        video = request.FILES.get('video')
        vid = Video(vid=video)
        vid.save()
        return redirect('app:add')
    return render(request, "add.html")


def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        image.delete()
    return redirect('app:add')


def delete_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        video.delete()
    return redirect('app:add')
