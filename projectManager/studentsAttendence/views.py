from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from .detection import LiveWebCam
from .models import CameraNumbers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm
# Create your views here.

@login_required
def dashboard(request):
    context = {
        'cameras': CameraNumbers.objects.all(),
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def markAttendance(request):
    return render(request, 'dashboard/attendence.html')


def loginView(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'login/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('/')


def gen(detection):
    while True:
        frame = detection.get_frame()
        yield b'--frame\r\n' b'Content-Type: image\r\n\r\n' + frame + b'\r\n\r\n'


def livecam_feed(request):
    return StreamingHttpResponse(gen(LiveWebCam()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
