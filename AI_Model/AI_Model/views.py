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
            print("POST Request")
            text = request.POST.get('mail')
            text = str(text)
            print(text)
            tokenizer = Tokenizer()

            def spam_ham(text):
                sms_test = [text]
                sms_seq = tokenizer.texts_to_sequences(sms_test)
                sms_pad = pad_sequences(sms_seq, maxlen= 20, padding='post')
                tokenizer.index_word
                sms_pad
                a = model.predict(sms_pad)
                a = a[0][0]
                a = a*100

                if a >= 0.5:
                    return JsonResponse({'predictions': 'spam', 'confidence': a})
                elif a < 0.5:
                    return JsonResponse({'predictions': 'not spam', 'confidence': a})
                else:
                    return JsonResponse({'error': 'Invalid input'})

            spam_ham(text)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Invalid input'})

    else:
        print("GET Request")
        return JsonResponse({'error': 'Invalid request method'})