from django.shortcuts import render, redirect
from django.views import View
from .langchain import recipe_generator

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'myapp/home.html')
    
    def post(self, request):
        data = request.POST.get('recipe')
        if not data == '':
            recipe_result = recipe_generator(recipe=data)
            print(recipe_result)
            return render(request, 'myapp/home.html', {'recipe_result': recipe_result})
        
        return redirect('/')