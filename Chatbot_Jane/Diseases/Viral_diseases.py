class Viral_disease:
    def __init__(self,symptoms,about,site):
        self.name=str(self).lower()
        self.about=str(about)
        self.symptoms=symptoms
        self.site=site
    def get_name(self):
        return self.name
    def get_symptoms(self):
        return self.symptoms
    def get_about(self):
        return self.about
    def get_site(self):
        return self.site

#h1n1 swineflu, measles, aids , chicken pox, rabies, influenza, hepatitis a, hepatitis b, common cold(viral), corona
Aids=Viral_disease(["immunodeficiency","fever","chills","rashes","night sweats","muscle ache","sore throat","fatigued","swollen lymph nodes",
"mouth ulcers"],"HIV stands for human immunodeficiency virus. It weakens a person’s immune system by destroying important cells that fight disease and infection. There is currently no effective cure for HIV.",
'https://www.cdc.gov/hiv/default.html')
Aids.name="aids"


Measles=Viral_disease(["rashes","high fever","cough","runny nose","red eyes", "watery eyes"],"Measles is a highly contagious virus that can lead to complications.",
"https://www.cdc.gov/measles/index.html")
Measles.name="measles"


Chicken_Pox=Viral_disease(['fever','feeling tired','loss of appetite','headache','rashes','fatigued'],
"Chickenpox is a highly contagious disease caused by the varicella-zoster virus. It can cause an itchy, blister-like rash. The rash appears first on the chest, back, and face, and then spreads over the entire body.",
"https://www.cdc.gov/chickenpox/index.html")
Chicken_Pox.name="chicken pox"


Hepatitis_A=Viral_disease(['yellow skin', 'yellow eyes','loss of appetite','upset stomach','vomiting'
,'stomach pain','fever','dark urine','light colored stools','diarrhea','joint pain','feeling tired','fatigued'],"Hepatitis A is a highly contagious, short-term liver infection caused by the Hepatitis A virus."
,"https://www.cdc.gov/hepatitis/hav/index.htm")
Hepatitis_A.name="hepatitis a"


Hepatitis_B=Viral_disease(["fever","fatigued","feeling tired","loss of appetite","nausea","vomiting","stomach pain"
,"dark urine","clay colored bowel movements","joint pain","yellow eyes", "yellow skin"],
"Hepatitis B is a vaccine-preventable liver infection caused by the Hepatitis B virus.",
"https://www.cdc.gov/hepatitis/hbv/index.htm")
Hepatitis_B.name="hepatitis b"


CommonCold=Viral_disease(['sore throat','runny nose','coughing','sneezing','headache','body ache'] ,"Common cold can be caused by many different types of viruses. The condition is generally harmless and symptoms usually resolve within two weeks.",
 'https://www.cdc.gov/features/rhinoviruses/index.html')
CommonCold.name="common cold"

Corona=Viral_disease(['fever', 'chills','cough','shortness of breath', 'difficulty in breathing','fatigued','feeling tired'
,'muscle ache', 'body ache','headache','loss of taste','loss of smell','Sore throat','Congestion','runny nose','Nausea','vomiting','Diarrhea'],
"Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.",
"https://www.cdc.gov/coronavirus/2019-nCoV/index.html")
Corona.name="corona"

Rabies=Viral_disease(["weakness","discomfort","fever","headache","cerebral dysfunction", "anxiety",
 "confusion","agitation","delirium","abnormal behavior","hallucinations","hydrophobia","insomnia"],
"Rabies is a preventable viral disease most often transmitted through the bite of a rabid animal. The rabies virus infects the central nervous system of mammals, ultimately causing disease in the brain and death.",
"https://www.cdc.gov/rabies/index.html")
Rabies.name="rabies"

Influenza=Viral_disease(["fever","feeling feverish","chills","cough","sore throat","runny nose","muscle ache","body aches","headaches",
"fatigued","vomiting","diarrhea"],"Influenza is a contagious respiratory illness caused by influenza viruses. It can cause mild to severe illness, and at times can lead to death."
,"https://www.cdc.gov/flu/symptoms/index.html")
Influenza.name="influenza"

H1N1_SwineFlu=Viral_disease(['fever', 'feeling feverish', 'chills','Cough','Sore throat','Runny nose',
'muscle ache', 'body ache','headache','fatigued'],"Swine flu, also known as the H1N1 virus, is a relatively new strain of an influenza virus that causes symptoms similar to the regular flu.",
"https://www.cdc.gov/h1n1flu/general_info.htm")
H1N1_SwineFlu.name="swine flu"

