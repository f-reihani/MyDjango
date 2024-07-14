from django.urls import path
urlpatterns = [
    path('login/',views.Login,name=login)
]
def Login(request):
    return render(request, template_name:'index.html')
