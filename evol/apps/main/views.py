from django.shortcuts import render
from models import News

def home(request):
	latest_news = News.objects.all()
	context = {'latest_news': latest_news}
	return render(request, 'main/test.html', context)

