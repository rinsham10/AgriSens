from django.shortcuts import render

def smart_farming_guide(request):
    return render(request, 'guide/index.html')

def index(request):
    return render(request, "index.html")  # Ensure "index.html" exists

# ✅ Add this function if "recommend" is needed
def recommend(request):
    return render(request, "guide/crop_recommendation.html")  # Ensure "recommend.html" exists in templates
