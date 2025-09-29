from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ultralytics import YOLO
import os
from django.conf import settings

#load trained YOLO model
model = YOLO("best.pt")

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]
        
        #save the uploaded file
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        full_path = fs.path(file_path)
        
        #Run detection
        results = model(full_path)
        
        #Check if fire was detected
        fire_detected = False
        if len(results[0].boxes) > 0:
            #If there are any detections = fire was detected
            fire_detected = True
        
        #save annotated image
        save_path = os.path.join(settings.MEDIA_ROOT, "results", uploaded_file.name)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        results[0].plot(save=True, filename=save_path)
        
        return render(request, "fireguard/result.html", {
            "uploaded_file_url": fs.url(file_path),
            "result_file_url": settings.MEDIA_URL + "results/" + uploaded_file.name,
            "fire_detected": fire_detected  #Pass the detection status
        })
    
    return render(request, "fireguard/upload.html")