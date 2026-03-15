from django.shortcuts import render, redirect
from .forms import StudentProfileForm
from .models import StudentProfile

def create_profile(request):

    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("/")

    else:
        form = StudentProfileForm(instance=profile)

    return render(request, "profile_form.html", {"form": form})