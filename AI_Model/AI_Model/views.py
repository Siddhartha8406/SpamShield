from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.models import load_model # type: ignore
import tensorflow_hub as hub

model = load_model('/Users/siddharthareddy/FinalYearProject/SpamSheild/new-trained-model.h5', custom_objects={'KerasLayer':hub.KerasLayer})

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            print("[Server]: POST Request")
            print(request.POST)
            text = request.POST['email']
            text = str(text)
            print("\n [Server Log]:"+text+"\n")

            def spam_ham(text):
                a = model.predict(text)
                a = a[0][0]
                a = a*100

                if a >= 0.5:
                    return JsonResponse({'predictions': 'spam', 'confidence': a})
                elif a < 0.5:
                    return JsonResponse({'predictions': 'not spam', 'confidence': a})
                else:
                    return JsonResponse({'error': 'Invalid input'})

            spam_ham(text)
            return JsonResponse({'predictions': 'spam', 'confidence': 0.9999})
        except Exception as e:
            print("Error: ", e)
            return JsonResponse({'error': 'Invalid input'})

    else:
        print("[Server]: GET Request")
        return JsonResponse({'error': 'Invalid request method'})