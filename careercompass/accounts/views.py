from django.shortcuts import render, redirect
from .forms import StudentProfileForm
from .models import StudentProfile
from recommendations.ml_engine import recommend_career
from recommendations.project_engine import recommend_projects
from recommendations.skill_gap import analyze_skill_gap

def home(request):
    return render(request, "home.html")
def create_profile(request):

    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            careers = recommend_career(profile.skills, profile.interests)

            projects = recommend_projects(profile.skills)

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