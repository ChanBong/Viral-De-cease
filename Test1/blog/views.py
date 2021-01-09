from django.shortcuts import render
from django.http import HttpResponse
import sys
from subprocess import run, PIPE


def home(request):
    return render(request, 'blog/home.html')


def chatbot(request):
    return render(request, 'blog/chatbot.html')


def external(request):
    inp = request.POST.get('param')

    import datetime
#import speech_recoginition as sr
    import pyttsx3
    import random
    from . import Viral_diseases
    import webbrowser
    #import User

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[2].id)

    def speak(audio):  # here audio is var which contain text
        engine.say(audio)
        engine.runAndWait()

    def response(y):
        return print(y), speak(y)

        # Lists Used
    bye_list = ["exit", "goodbye", "good night", "bbye",
                "bye", "tata", "good bye", "see you", "see ya", "gn"]
    positive_user_response = [
        "fine", "cool", "i'm good", "happy", "elated"]
    yes_list = ["yes", "ya", "yup", "sure", "yupz", "why not"]
    no_list = ["nah", "no", "that's enough", "nope", "exit"]
    praise = ["very good", "amazing", "so cute", "so kind", "efficient",
              "helpful", "wonderful", "brilliant", "intelligent", "awesome"]
    thanks_list = ["thanks", "thank you", "tysm"]
    sds_support = ["team you", "best team",
                   "favorite team", "your favorite team"]
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
        elif 16 <= datetime.datetime.now().hour < 20:
            x = "Good Evening!"
        else:
            x = "It's bed time, but I'll still help you!"
        return response(x)

    def About_Jane(str):
        if "name" in str:
            return response("My name is " + Jane.name)
        if "gender" in str:
            return print(Jane.gender + "\U0001F643"), speak(Jane.gender)
        if "hobbies" in str:
            return response("I like " + random.choice(Jane.hobbies))
        if 'what do you do' in str:
            return response(Jane.function)
        if "creat" in str:
            return response(Jane.creator)
        if "favorite song" in str:
            response(Jane.fav_song), response("Would you like to hear it?")
            song = input().lower()
            for bc in yes_list:
                if bc in song:
                    print("Enjoy!\U0001F607"), speak("Enjoy!")
                    return webbrowser.open_new("https://www.youtube.com/watch?v=vVqGNfAZb2w")
            for bc in no_list:
                if bc in song:
                    return print("Ok, no problem!\U0001F615"), speak("Ok, no problem!")

    def j_praise(str):
        for x in praise:
            if x in str:
                return print("Awww, that's so sweet of you!\U0001F60A"), speak("Awww, that's so sweet of you!")
        for lala in thanks_list:
            if lala in str:
                return print("\U0001F60A"), response("Happy to help!")

    def Conversation(str):
        if "i love" in str:
            return print(j_emotion.love + "\U0001F92D"), speak(j_emotion.love)
        if "i like" in str:
            return print(j_emotion.like + "\U0001F603"), speak(j_emotion.like)
        if "you single" in str:
            return print(j_emotion.single + "\U0001F606"), speak(j_emotion.single)
        if "how are you" in str:
            return response(random.choice(j_emotion.halchal) + "\U0001F643")
        for x in j_emotion.other_ai:
            if "about " + x in str:
                return print("We are partners in crime! \U0001F606"), speak("We are partners in crime!")
            if "are you " + x in str:
                return print("No! She's my sister.\U0001F605"), speak("No! She's my sister.")
        if "friend" in str:
            return print(j_emotion.friends + "\U0001F601"), speak(j_emotion.friends)
        for x in sds_support:
            if x in str:
                return response("Team Algo Nukes anytime, they're literally on \U0001F525!")

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
                print(str(alpha) + ". " +
                      buffer_diagnose[alpha]), speak(buffer_diagnose[alpha])
                alpha += 1
            response(
                "If you want to know more about the diagnosed disease type its number else type 0!")
            lol = int(input())
            if lol != 0:
                webbrowser.open_new(buffer_diagnose[lol].get_website())
            else:
                response("Let's continue the convo than!")
        return()

    def about_disease(str):
        temp_y = [Viral_diseases.Aids, Viral_diseases.Rabies, Viral_diseases.Influenza, Viral_diseases.Corona,
                  Viral_diseases.CommonCold, Viral_diseases.H1N1_SwineFlu, Viral_diseases.Measles, Viral_diseases.Chicken_Pox, Viral_diseases.Hepatitis_A, Viral_diseases.Hepatitis_B]
        for y in temp_y:
            name = "about " + y.get_name()
            if name in str:
                response(y.get_about())
                response("Would you like to know more?")
                c = input().lower()
                for l in yes_list:
                    if l in c:
                        response("Here you go!")
                        # open site of that disease
                        return webbrowser.open_new(y.get_site())
                for m in no_list:
                    if m in c:
                        response("As you wish!")

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

    Greeting()

    response("How are you?")

    flag = 1

    while (flag == 1):
        a = input().lower()
        About_Jane(a)
        j_praise(a)
        Conversation(a)
        count = 0
        for z in positive_user_response:
            if z in a:
                print("That's good to know! How may I help you then? \U0001F60A"), speak(
                    "That's good to know! How may I help you then?")

        about_disease(a)
        Diagnoser(a)
        '''Appointment_booker(a)'''

        for l in bye_list:
            if l in a:
                while count < 1:
                    print("See ya soon! \U0001F64B"), speak("See ya soon!")
                    count += 1
                flag = 0

    out = run(["pyhton3", "C:\\Users\\hk\\Desktop\\testscript.py",
               inp], shell=False, stdout=PIPE)
    return render(request, 'chatbot.html')
