"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog import views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.blog_list,name="blog_list"), 
    path('',views.BlogListView.as_view(),name="blog_list"),   
    path('add_new/',views.CreateBlogView.as_view(),name="add_new"),
    # path('blog_detail/<int:pk>/',views.blog_detail, name="blog_detail"),
    path('blog_detail/<int:pk>/',views.BLogDetailView.as_view(), name="blog_detail"),
    # path('blog_update/<pk>/',views.blog_update, name="blog_update"),
    path('blog_update/<pk>/',views.UpdateBlogView.as_view(), name="blog_update"),
    path('blog_delete/<pk>/',views.blog_delete, name="blog_delete"),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('signup/',accounts_views.signup, name='signup'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('reset/',auth_views.PasswordResetView.as_view(
        template_name = 'password_reset.html',
        email_template_name = 'password_reset_email.html',
        subject_template_name = 'password_reset_subject.txt'
    ),name='reset'),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html')),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
    path('settings/password/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    path('settings/password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
    path('account/',accounts_views.account_detail,name="account"),
    path('edit_user/<int:pk>/',accounts_views.UpdateAccountView.as_view(),name="edit_user"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
