from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json

# Create your views here.
def mensagem(nome,email,mensagem):
    msg = "\n\nNome: {}\nMensagem: {}\nEmail: {}\n".format(nome,mensagem,email)
    return msg

def index(nome, email, mensagem):
    subject = "FoodCare: {}".format(nome)
    message = mensagem(nome, email, mensagem)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER,]
    send_mail( subject, message, email_from, recipient_list )


@csrf_exempt
def email(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        resposta = json.loads(body_unicode)
        print(resposta)
        index(resposta["nome"],resposta["email"],resposta["msg"])
        return HttpResponse(status=204)
    
    
