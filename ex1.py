from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

API_KEY = "YOUR_API_KEY"
URL = "YOUR_SERVICE_URL"

authenticator = IAMAuthenticator(API_KEY)
nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)
nlu.set_service_url(URL)

def detect_emotion(text):
    try:
        response = nlu.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        return response['emotion']['document']['emotion']
    except Exception as e:
        return {"error": str(e)}
