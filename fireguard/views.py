from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ultralytics import YOLO
import os
from django.conf import settings

# Load your trained YOLO model once
model = YOLO("best.pt")

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # save the uploaded file
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        full_path = fs.path(file_path)

        # run detection
        results = model(full_path)

        # save annotated image
        save_path = os.path.join(settings.MEDIA_ROOT, "results", uploaded_file.name)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        results[0].plot(save=True, filename=save_path)

        return render(request, "fireguard/result.html", {
            "uploaded_file_url": fs.url(file_path),
            "result_file_url": settings.MEDIA_URL + "results/" + uploaded_file.name
        })

    return render(request, "fireguard/upload.html")
