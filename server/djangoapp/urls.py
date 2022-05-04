from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),
    # path for registration
    path('registration/', views.registration_request, name='registration'),
    # path for login
    path('login/', views.login_request, name='login'),
    # path for logout
    path('logout/', views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path(route='dealer_reviews/', view=views.dealer_reviews, name='reviews'),

    # path for add a review view
    path('add_review/', view=views.add_review, name='review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)