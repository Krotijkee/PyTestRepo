from django.shortcuts import render

def index(request):
   return render (request, 'testApp/homePage.html')

def contact(request):
   return render(request, 'testApp/basic.html',{'values':['если у вас остались вопросы','943-343-24-33']})