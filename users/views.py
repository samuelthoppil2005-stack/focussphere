from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        # ✅ Check empty fields
        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect("signup")

        # ✅ Check password match
        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        # ✅ Check duplicate user
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        try:
            # ✅ Create user safely
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()

            messages.success(request, "Account created successfully!")
            return redirect("login")

        except Exception as e:
            print(e)  # 👈 shows real error in terminal
            messages.error(request, "Something went wrong")
            return redirect("signup")

    return render(request, "registration/signup.html")