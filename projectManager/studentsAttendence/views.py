from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .detection import LiveWebCam


# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/index.html')


def markAttendence(request):
    return render(request, 'dashboard/attendence.html')


def login(request):
    return render(request, 'login/login.html')


def gen(detection):
    while True:
        frame = detection.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image\r\n\r\n' + frame + b'\r\n\r\n')


def livecam_feed(request):
    return StreamingHttpResponse(gen(LiveWebCam()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
