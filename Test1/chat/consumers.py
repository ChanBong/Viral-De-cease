# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


def call_chatbot(UserInput, iteration):
    UserInput = UserInput.lower()
    import datetime
    from . import Viral_diseases
    #import speech_recoginition as sr
    #import pyttsx3
    import random
    import webbrowser

    # Lists Used
    bye_list = ["exit", "goodbye", "good night", "bbye",
                "bye", "tata", "good bye", "see you", "see ya", "gn"]
    positive_user_response = ["fine", "cool", "i'm good", "happy", "elated"]
    yes_list = ["yes", "ya", "yup", "sure", "yupz", "why not"]
    no_list = ["nah", "no", "that's enough", "nope", "exit"]
    praise = ["very good", "amazing", "so cute", "so kind", "efficient",
              "helpful", "wonderful", "brilliant", "intelligent", "awesome"]
    thanks_list = ["thanks", "thank you", "tysm"]
    sds_support = ["team you", "best team",
                   "favorite team", "your favorite team"]
    commit = []
    wait_for_response = []
    dis_found = ""
    ###############
    wait = 0

    def response(y):
        wait = 0
        return (y + "\n")

    def response_commit(data):
        if data == "\n":
            commit.append(data)
            return commit
        else:
            commit.append(data)
    ##############

    class Viral_disease:
        def __init__(self, symptoms, about, site):
            self.name = str(self).lower()
            self.about = str(about)
            self.symptoms = symptoms
            self.site = site

        def get_name(self):
            return self.name

        def get_symptoms(self):
            return self.symptoms

        def get_about(self):
            return self.about

        def get_site(self):
            return self.site

    # h1n1 swineflu, measles, aids , chicken pox, rabies, influenza, hepatitis a, hepatitis b, common cold(viral), corona
    Aids = Viral_disease(["fever", "chills", "rashes", "night sweats", "muscle ache", "sore throat", "fatigued", "swollen lymph nodes",
                          "mouth ulcers"], "HIV stands for human immunodeficiency virus. It weakens a person’s immune system by destroying important cells that fight disease and infection. There is currently no effective cure for HIV.",
                         'https://www.cdc.gov/hiv/default.html')
    Aids.name = "aids"

    Measles = Viral_disease(["rashes", "high fever", "cough", "runny nose", "red eyes", "watery eyes"], "Measles is a highly contagious virus that can lead to complications.",
                            "https://www.cdc.gov/measles/index.html")
    Measles.name = "measles"

    Chicken_Pox = Viral_disease(['fever', 'feeling tired', 'loss of appetite', 'headache', 'rashes', 'fatigued'],
                                "Chickenpox is a highly contagious disease caused by the varicella-zoster virus. It can cause an itchy, blister-like rash. The rash appears first on the chest, back, and face, and then spreads over the entire body.",
                                "https://www.cdc.gov/chickenpox/index.html")
    Chicken_Pox.name = "chicken pox"

    Hepatitis_A = Viral_disease(['yellow skin', 'yellow eyes', 'loss of appetite', 'upset stomach', 'vomiting', 'stomach pain', 'fever', 'dark urine', 'light colored stools', 'diarrhea',
                                 'joint pain', 'feeling tired', 'fatigued'], "Hepatitis A is a highly contagious, short-term liver infection caused by the Hepatitis A virus.", "https://www.cdc.gov/hepatitis/hav/index.htm")
    Hepatitis_A.name = "hepatitis a"

    Hepatitis_B = Viral_disease(["fever", "fatigued", "feeling tired", "loss of appetite", "nausea", "vomiting", "stomach pain", "dark urine", "clay colored bowel movements", "joint pain", "yellow eyes", "yellow skin"],
                                "Hepatitis B is a vaccine-preventable liver infection caused by the Hepatitis B virus.",
                                "https://www.cdc.gov/hepatitis/hbv/index.htm")
    Hepatitis_B.name = "hepatitis b"

    CommonCold = Viral_disease(['sore throat', 'runny nose', 'coughing', 'sneezing', 'headache', 'body ache'], "Common cold can be caused by many different types of viruses. The condition is generally harmless and symptoms usually resolve within two weeks.",
                               'https://www.cdc.gov/features/rhinoviruses/index.html')
    CommonCold.name = "common cold"

    Corona = Viral_disease(['fever', 'chills', 'cough', 'shortness of breath', 'difficulty in breathing', 'fatigued', 'feeling tired', 'muscle ache', 'body ache', 'headache', 'loss of taste', 'loss of smell', 'Sore throat', 'Congestion', 'runny nose', 'Nausea', 'vomiting', 'Diarrhea'],
                           "Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.",
                           "https://www.cdc.gov/coronavirus/2019-nCoV/index.html")
    Corona.name = "corona"

    Rabies = Viral_disease(["weakness", "discomfort", "fever", "headache", "cerebral dysfunction", "anxiety",
                            "confusion", "agitation", "delirium", "abnormal behavior", "hallucinations", "hydrophobia", "insomnia"],
                           "Rabies is a preventable viral disease most often transmitted through the bite of a rabid animal. The rabies virus infects the central nervous system of mammals, ultimately causing disease in the brain and death.",
                           "https://www.cdc.gov/rabies/index.html")
    Rabies.name = "rabies"

    Influenza = Viral_disease(["fever", "feeling feverish", "chills", "cough", "sore throat", "runny nose", "muscle ache", "body aches", "headaches",
                               "fatigued", "vomiting", "diarrhea"], "Influenza is a contagious respiratory illness caused by influenza viruses. It can cause mild to severe illness, and at times can lead to death.", "https://www.cdc.gov/flu/symptoms/index.html")
    Influenza.name = "influenza"

    H1N1_SwineFlu = Viral_disease(['fever', 'feeling feverish', 'chills', 'Cough', 'Sore throat', 'Runny nose',
                                   'muscle ache', 'body ache', 'headache', 'fatigued'], "Swine flu, also known as the H1N1 virus, is a relatively new strain of an influenza virus that causes symptoms similar to the regular flu.",
                                  "https://www.cdc.gov/h1n1flu/general_info.htm")
    H1N1_SwineFlu.name = "swine flu"

    ###############

    class Jane:
        name = "Jane"
        function = "Think me as your guide @ this website!"
        gender = "Hey! Does that matters?"
        hobbies = ["helping people", "thinking about space",
                   "doing critical analysis", "doing calculations", "irony, top notch!"]
        fav_song = "Liar by Camila Cabello."
        creator = "Aryan Ranjan is my creator!"

    class j_emotion:
        love = "I love you too, but, as a friend!"
        like = "I like you too!"
        single = "I'm single, but I don't like to mingle."
        friends = "All people are my friends!"
        halchal = ["Always as fresh as the morning dew!",
                   "I'm good, thanks for asking!"]
        other_ai = ["siri", "google assistant", "alexa"]

    def Greeting():
        if 0 <= datetime.datetime.now().hour < 12:
            x = "Good Morning!"
        elif 12 <= datetime.datetime.now().hour < 16:
            x = "Good Afternoon!"
        elif 16 <= datetime.datetime.now().hour < 24:
            x = "Good Evening!"
        return response(x + "\nI am the beta version of Jane" + "\nHow are you ?")

    def Diagnoser(string):
        temp_x = [Viral_diseases.Aids, Viral_diseases.Rabies, Viral_diseases.Influenza, Viral_diseases.Corona,
                  Viral_diseases.CommonCold, Viral_diseases.H1N1_SwineFlu, Viral_diseases.Measles, Viral_diseases.Chicken_Pox, Viral_diseases.Hepatitis_A, Viral_diseases.Hepatitis_B]
        buffer_diagnose = [" "]
        for x in temp_x:
            z = x.get_symptoms()
            for y in z:
                if y in string:
                    buffer_diagnose.append(x.get_name())
        if len(buffer_diagnose) >= 2:
            response("You may have: ")
            alpha = 1
            while alpha < len(buffer_diagnose):
                response_commit(str(alpha) + ". " + buffer_diagnose[alpha])
                alpha += 1
            response_commit(
                "If you want to know more about the diagnosed disease type its number else type 0 !")
            wait = 10
            wait_for_response = buffer_diagnose
            return response_commit("GO")
        else:
            return response("I have no disease in my database that matches this symptom")

    def binary_response2(number):
        return webbrowser.open_new(wait_for_response[lol].get_website())

    def about_disease(str):
        temp_y = [Viral_diseases.Aids, Viral_diseases.Rabies, Viral_diseases.Influenza, Viral_diseases.Corona,
                  Viral_diseases.CommonCold, Viral_diseases.H1N1_SwineFlu, Viral_diseases.Measles, Viral_diseases.Chicken_Pox, Viral_diseases.Hepatitis_A, Viral_diseases.Hepatitis_B]
        for y in temp_y:
            name = y.get_name()
            if name in str:
                response_commit(y.get_about())
                response_commit("\n")
                response_commit("Would you like to know more?")
                wait = 11
                dis_found = name
                return response_commit("GO")
                c = input().lower()
                for l in yes_list:
                    if l in c:
                        response("Here you go!")
                        # open site of that disease
                        return webbrowser.open_new(y.get_site())
                for m in no_list:
                    if m in c:
                        response("As you wish!")

    def binary_response1(str):
        if "yes" in str:
            return webbrowser.open_new(y.get_site())
        if "no" in str:
            return response("As you wish!")

    def Convo(str):
        if "i love" in str:
            return response(j_emotion.love + "\U0001F92D"), speak(j_emotion.love)
        if "i like" in str:
            return response(j_emotion.like + "\U0001F603"), speak(j_emotion.like)
        if "you single" in str:
            return response(j_emotion.single + "\U0001F606"), speak(j_emotion.single)
        if "how are you" in str:
            return response(random.choice(j_emotion.halchal) + "\U0001F643")
        if "friend" in str:
            return response(j_emotion.friends + "\U0001F601"), speak(j_emotion.friends)

    '''def Appointment_booker(str):
        if "appointment" in str:
            response("Would you like to start the appointment booking procedure?")
            lala=input().lower
            for abc in yes_list:
                if abc in lala:
                    if "username != Guest_something":
                        response("Welcome to the booking procedure, "+User.Logged_user.get_name())
                        response("If at any time you wanna cancel the procedure type a disagreement.")
                        response("We allot appointments for timings between 2pm-6pm ")
                        response("At present the unbooked time slots are:")
                        ##for loop for going through list of free slots
                        response ("Which slot would you like to book?")
                        bala=int(input())
                        response("Would you like to book the appointment for timings?")'''
    if iteration == 1:
        return Greeting()

    if wait == 1:
        if "yes" in UserInput or "no" in UserInput:
            return binary_response1(UserInput)
        Number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if UserInput in Number_list:
            converted = int(UserInput)
            return binary_response2(converted)

    if UserInput in bye_list:
        return response("See ya soon! \U0001F64B")

    Convo(UserInput)

    if "i have" in UserInput:
        symptoms = UserInput.split()
        Diagnoser(symptoms[2])

    else:
        return about_disease(UserInput)


class ChatConsumer(AsyncWebsocketConsumer):
    bot_reply = "Invalid_Option"

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.iteration_no = 1
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        iteration_no = self.iteration_no
        bot_reply = call_chatbot(message, iteration_no)
        self.iteration_no += 1
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': bot_reply
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
