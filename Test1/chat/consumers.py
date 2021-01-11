# chat/consumers.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
        if data == "GO":
            commit.append("\n")
            return commit
        else:
            commit.append(data)
    ##############

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
                    buffer_diagnose.append(x.get_name() + "\n")
        wait_for_response = buffer_diagnose
        if len(wait_for_response) >= 2:
            response("You may have: ")
            alpha = 1
            while alpha < len(wait_for_response):
                response_commit(str(alpha) + ". " + wait_for_response[alpha])
                alpha += 1
            response_commit(
                "If you want to know more about the diagnosed disease type its number else type 0 !")
            wait = 10
            return response_commit("GO")
        else:
            return response("I have no disease in my database that matches this symptom")

    def binary_response2(number):
        webbrowser.open_new(wait_for_response[number].get_website())

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

    def binary_response1(str):
        if "yes" in str:
            return ("redirect")
        if "no" in str:
            return response("As you wish!")

    def Convo(str):
        if "i love" in str:
            return response(j_emotion.love + "\U0001F92D")
        if "i like" in str:
            return response(j_emotion.like + "\U0001F603")
        if "you single" in str:
            return response(j_emotion.single + "\U0001F606")
        if "how are you" in str:
            return response(random.choice(j_emotion.halchal) + "\U0001F643")
        if "friend" in str:
            return response(j_emotion.friends + "\U0001F601")

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
    Convo(UserInput)

    if "yes" in UserInput or "no" in UserInput:
        return binary_response1(UserInput)
    Number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if UserInput in Number_list:
        converted = int(UserInput)
        return binary_response2(converted)

    if UserInput in bye_list:
        return response("See ya soon! \U0001F64B")

    if "i have" in UserInput:
        symptoms = UserInput.split()
        return Diagnoser(symptoms[2])

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
