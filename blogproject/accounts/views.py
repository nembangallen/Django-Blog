from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, UserProfileForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            auth_login(request,user)
            return redirect('blog_list')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    context = {'form':form,'profile_form':profile_form}
    return render(request, 'signup.html',context)

def account_detail(request):
    return render(request, 'account.html')