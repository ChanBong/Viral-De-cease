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

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):  # here audio is var which contain text
        engine.say(audio)
        engine.runAndWait()

    def response(y):
        return print(y), speak(y)

    class Jane:
        name = "Jane"
        function = "Think me as your guide @ this website!"
        gender = "Hey! Does that matters?"
        hobbies = ["helping people", "thinking about space",
                   "doing critical analysis", "doing calculations", "irony, top notch!"]

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

    # response(Viral_diseases.AIDS.name)
    bye_list = ["exit", "goodbye", "good night", "bbye",
                "bye", "tata", "good bye", "see you", "see ya", "gn"]

    def About_Jane(str):
        if "your name" or "name" in str:
            return response("My name is " + Jane.name)
        if "gender" in str:
            return response(Jane.gender)
        if "hobbies" in str:
            return response("I like " + random.choice(Jane.hobbies))
        if 'what do you do' in str:
            return response(Jane.function)

    response(Viral_diseases.AIDS.name)

    def Diagnoser(str):
        temp_x = [Viral_diseases.AIDS, Viral_diseases.Rabies, Viral_diseases.Influenza, Viral_diseases.Corona,
                  Viral_diseases.CommonCold, Viral_diseases.H1N1_SwineFlu, Viral_diseases.Measles, Viral_diseases.Chicken_Pox, Viral_diseases.Hepatitis_A, Viral_diseases.Hepatitis_B]
        for x in temp_x:
            if x.symptoms in str:
                buffer_diagnose = []
                buffer_diagnose.append(x.name)

            return response("You may have " + buffer_diagnose)

    def about_disease(str):
        temp_y = [Viral_diseases.AIDS]
        for y in temp_y:
            if ("about" + y.name.string()) in str:
                response(y.about)
                response("Would you like to know more?")
                yes_list = ["yes", "ya", "yup", "sure", "yupz", "why not"]
                no_list = ["nah", "no", "that's enough", ]
                c = input()
                for l in yes_list:
                    if l in c:
                        # open site of that disease
                        c = webbrowser.open(y.site)
                for m in no_list:
                    if m in c:
                        response("As you wish!")

    Greeting()

    response("How are you?")

    flag = 1

    while (flag == 1):
        About_Jane(inp)
        about_disease(inp)
        for l in bye_list:
            if l in a:
                response("See ya soon!")
                flag = 0

    # out = run(["pyhton3", "C:\\Users\\hk\\Desktop\\testscript.py",
    #          inp], shell=False, stdout=PIPE)
    print(out)
    return render(request, 'chatbot.html', {'data1': out.stdout})
