from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import StudentProfileForm
from .models import StudentProfile
from recommendations.ml_engine import recommend_career
from recommendations.project_engine import recommend_projects
from recommendations.skill_gap import analyze_skill_gap

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_profile(request):

    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            careers = recommend_career(profile.skills, profile.interests)

            combined_input = f"{profile.branch}, {profile.skills}, {profile.interests}"

            projects = recommend_projects(combined_input)
            if careers:
                skill_gap = analyze_skill_gap(
                    profile.skills,
                    careers[0]["tools"]
                )
            else:
                skill_gap = {"known": [], "missing": []}

            return render(
                request,
                "results.html",
                {
                    "careers": careers,
                    "projects": projects,
                    "skill_gap": skill_gap
                }
            )

    else:
        form = StudentProfileForm(instance=profile)

    return render(request, "profile_form.html", {"form": form})