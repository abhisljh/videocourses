from django.shortcuts import render, redirect
from courses.models import Course , Video , UserCourse
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required(login_url ='login'), name='dispatch')
class ProfileList(ListView):
    template_name = 'courses/profile.html'
    queryset  = UserCourse.objects.all()
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)

'''
@method_decorator(login_required(login_url ='login'), name='dispatch')
def Profile(request):
    return render(request , template_name="courses/profile.html")

#def Profile(request, slug):
    course = Course.objects.get(slug = slug)
    print(request.user)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course = course)
    print("Preview Video", video.is_preview)
    if((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect("login")
    #if you are enrllled you can wathc whole video 


    print(video)
    context = {
        "course": course,
        "video": video,
        'videos': videos
    }
   
    return render(request, template_name="courses/coursepage.html", context = context)
'''

