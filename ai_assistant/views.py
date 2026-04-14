from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from .document_reader import read_file
from groq import Groq
import os

API_KEY = os.environ.get("API_KEY")



def ai_chat_page(request):
    return render(request, "ai_chat.html")



from .document_reader import read_file

@csrf_exempt
def ai_chat(request):

    if request.method == "POST":

        user_message = request.POST.get("message")

        uploaded_file = request.FILES.get("file")

        document_text = ""

        if uploaded_file:

            file_path = f"media/{uploaded_file.name}"

            with open(file_path, "wb+") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            document_text = read_file(file_path)

        prompt = user_message + "\n\nDocument Content:\n" + document_text

        completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role":"system","content":
"""You are an AI tutor for students.

Always format responses clearly using this structure:

Title

Short introduction

Step-by-step explanation

Key points

Example (if applicable)

Keep answers clear, structured, and easy to read.
"""},
        {"role": "user", "content": prompt}
    ],
    stream=True
)

        reply = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                reply += chunk.choices[0].delta.content

        return JsonResponse({"reply": reply})

@csrf_exempt
def explain_document(request):

    if request.method == "POST":

        uploaded_file = request.FILES.get("file")

        file_path = uploaded_file.temporary_file_path()

        text = read_file(file_path)

        return JsonResponse({
            "text": text[:500]
        })