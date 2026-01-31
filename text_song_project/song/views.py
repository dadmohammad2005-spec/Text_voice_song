# from django.shortcuts import render
# from django.conf import settings
# from gtts import gTTS
# import os

# def home(request):
#     audio_file = None

#     if request.method == "POST":
#         text = request.POST.get("text")
#         media_path = os.path.join(settings.MEDIA_ROOT, "output.mp3")
#         tts = gTTS(text=text, lang='ur')
#         tts.save(media_path)
#         audio_file = "output.mp3"

#     return render(request, "home.html", {"audio": audio_file})


# from django.http import JsonResponse
# from gtts import gTTS
# import os
# from django.conf import settings

# def generate_audio(request):
#     text = request.GET.get('text', '')
#     if text:
#         # Audio generate karna
#         tts = gTTS(text=text, lang='en')
        
#         # File ka naam aur path set karna
#         filename = "generated_audio.mp3"
#         file_path = os.path.join(settings.MEDIA_ROOT, filename)
        
#         # Save karna
#         tts.save(file_path)
        
#         # Audio ka URL wapis bhejna
#         audio_url = settings.MEDIA_URL + filename
#         return JsonResponse({'status': 'success', 'audio_url': audio_url})
    
#     return JsonResponse({'status': 'error', 'message': 'No text provided'})














# from django.shortcuts import render
# from django.http import JsonResponse
# from gtts import gTTS
# import os
# from django.conf import settings

# # Aapka purana home view
# def home(request):
#     return render(request, 'home.html')

# # Naya function jo aapne urls.py mein likha hai
# def generate_audio(request):
#     text = request.GET.get('text', '')
#     if text:
#         try:
#             tts = gTTS(text=text, lang='en')
#             filename = "generated_audio.mp3"
            
#             # Media folder check karna
#             if not os.path.exists(settings.MEDIA_ROOT):
#                 os.makedirs(settings.MEDIA_ROOT)
                
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
#             tts.save(file_path)
            
#             audio_url = settings.MEDIA_URL + filename
#             return JsonResponse({'status': 'success', 'audio_url': audio_url})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})
    
#     return JsonResponse({'status': 'error', 'message': 'No text provided'})

# from django.shortcuts import render
# from django.http import JsonResponse

# from gtts import gTTS
# import os
# from django.conf import settings

# def home(request):
#     if request.method == "POST":
#         text = request.POST.get("text")  # text from form
#         # Convert to audio
#         folder = "audio_files"
#         if not os.path.exists(folder):
#             os.makedirs(folder)
#         file_path = os.path.join(folder, "output.mp3")
#         tts = gTTS(text=text, lang='en')
#         tts.save(file_path)
#         return render(request, "home.html", {"audio_file": file_path})
#     return render(request, "home.html")
















from django.shortcuts import render
from django.http import JsonResponse
from gtts import gTTS
import os
from django.conf import settings





def home(request):
    return render(request, 'home.html')

def generate_audio(request):
    text = request.GET.get('text', '')
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            
            # Folder ensure karna
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            
            filename = "output.mp3"
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            # os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            # Purani file delete karna taake error na aaye
            if os.path.exists(file_path):
                os.remove(file_path)
                
            tts.save(file_path)
            
            audio_url = settings.MEDIA_URL + filename
            return JsonResponse({'status': 'success', 'audio_url': audio_url})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'No text found'})