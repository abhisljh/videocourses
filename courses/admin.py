from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning , Video  , UserCourse , Payment
from django.utils.html import format_html

# Register your models here.


class TagAdmin(admin.TabularInline): #registering the model in tabular form here 
    model = Tag

class LearningAdmin(admin.TabularInline): #registering the model in tabular form here 
    model = Learning

class PrerequisiteAdmin(admin.TabularInline): #registering the model in tabular form here 
    model = Prerequisite

class VideoAdmin(admin.TabularInline): #registering the model in tabular form here 
    model = Video

class CourseAdmin(admin.ModelAdmin): #registering the model in tabular form here 
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin] #showing or addig all above tags in tabular form under course table
    list_display = ["name", 'get_price','get_discount','active']
    list_filter = ("discount", "active")
    def get_discount(self, course):
        return f'{course.discount}%'

    def get_price(self, course):
        return f'₹{course.price}'
    
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"


   
class PaymentAdmin(admin.ModelAdmin): #registering the model in tabular form here 
    model = Payment
    list_display = ['order_id' ,'get_user', 'get_course', 'status']
    list_filter = ("status", "course")
    
    def get_user(self , payment):
        return format_html(f"<h><a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</h></a>")

    def get_course(self , payment):
        return format_html(f"<h><a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</h></a>")

    get_user.short_description = "User"
    get_course.short_description = "Course"




class UserCourseAdminModel(admin.ModelAdmin): #registering the model in tabular form here 
    model = UserCourse
    list_display = ['get_user', 'get_course']
    list_filter = ['course']
    
    def get_user(self , usercourse):
        return format_html(f"<h><a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</h></a>")

    def get_course(self , usercourse):
        return format_html(f"<h><a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</h></a>")

    get_user.short_description = "User"
    get_course.short_description = "Course"




admin.site.register(Course, CourseAdmin) #registering the course which is main class and courseadmin which is modified class having tags unde it 
admin.site.register(Video)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(UserCourse , UserCourseAdminModel)