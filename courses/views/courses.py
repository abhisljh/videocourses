from django.shortcuts import render, redirect
from courses.models import Course , Video, UserCourse
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url ='login'), name='dispatch')
class MyCoursesList(ListView):
    template_name = 'courses/my_courses.html'
    queryset  = UserCourse.objects.all()
    context_object_name = 'user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)


def coursePage(request, slug):
    course = Course.objects.get(slug = slug)
    print(request.user)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course = course)
    print("Preview Video", video.is_preview)

    if(video.is_preview is False): 

        if(request.user.is_authenticated is False):
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user , course = course)
                
                
            except:
                return redirect("checkout", slug = slug)
        #if you are enrllled you can wathc whole video 


    print(video)
    context = {
        "course": course,
        "video": video,
        'videos': videos
    }
   
    return render(request, template_name="courses/coursepage.html", context = context)
'''
@login_required(login_url="login")
def my_courses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user = user)
    context = {
        'user_courses': user_courses
    }
    return render(request= request , template_name="courses/my_courses.html", context = context)
'''

