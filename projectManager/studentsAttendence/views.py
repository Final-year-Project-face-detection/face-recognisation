from django.core.exceptions import DisallowedRedirect, SuspiciousOperation
from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from .detection import LiveWebCam
from .models import CameraNumbers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm
from CSE.models import FourthYearASec
from studentsAttendence.models import StudentsDetails
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from django.views import View
# Create your views here.

@login_required
def dashboard(request):
    if request.method == 'POST':
        cam = request.POST.get('cameranumber')
        request.session['cam']= cam
        context = {
            'cam': cam,
            'cameras': CameraNumbers.objects.all().order_by('Classroom'),
            'camera': CameraNumbers.objects.get(Cameras=cam),
        }
        return render(request, 'mark/index.html', context)
    elif request.method == 'GET':
        context = {
            'cameras': CameraNumbers.objects.all().order_by('Classroom'),
        }
        return render(request, 'mark/index.html', context)
@login_required
def camselect(request):
    if request.method == 'POST':
        cam = request.POST.get('cameranumber')
        request.session['cam']= cam
        context = {
            'cam': cam,
            'cameras': CameraNumbers.objects.all().order_by('Classroom'),
            'camera': CameraNumbers.objects.get(Cameras=cam),
        }
        return render(request, 'mark/camselect.html', context)
    elif request.method == 'GET':
        context = {
            'cameras': CameraNumbers.objects.all().order_by('Classroom'),
        }
        return render(request, 'mark/camselect.html', context)

@login_required
def markAttendance(request):
    cam = request.session.get('cam')
    
    context ={
        'cam': cam,
        'details'  : StudentsDetails.objects.all(),
        'del' : FourthYearASec.objects.all()
    }
    return render(request, 'captures/index.html', context)


def loginView(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if next == '/mark/':
            # raise DisallowedRedirect(SuspiciousOperation)
            return redirect('dashboard')
        return redirect(next)
    context = {
        'form': form,
    }
    return render(request, 'login/index.html', context)


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


def camNum(request):
    cam = request.session.get('cam')
    return cam


def status(request):
    context = {
        'studdetails' : StudentsDetails.objects.all(),
        'statusdetails' : FourthYearASec.objects.all()
    }
    return render(request, 'status/index.html', context)

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


def ViewPDF(request):
    context = {
        'studdetails' : StudentsDetails.objects.all(),
        'statusdetails' : FourthYearASec.objects.all()
    }
    pdf = render_to_pdf('pdfs/pdf_template.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def DownloadPDF(request):
    context = {
        'studdetails' : StudentsDetails.objects.all(),
        'statusdetails' : FourthYearASec.objects.all()
    }
    pdf = render_to_pdf('pdfs/pdf_template.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Attendance.pdf"
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content
    return response