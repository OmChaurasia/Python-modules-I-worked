## Steps I covered 
- Install django `pip install django`
- Create django app in a folder `django-admin startproject mysite`
- Open your project folder that is created 
- To run the project `python manage.py runserver`
- To Create a app in project `python manage.py startapp home`
- Create urls.py file in apps folder
- In app/urls.py copy all the code as in project/urls.py
- import 'include' from django.urls
- The requests first go to project/urls.py
- if requests blank we redirect it to app/urls.py
`
path('', include('home.urls'))
`
- import views in app/urls.py `from home import views`
- Redirect to a function name index in views.py `path("",views.index, name='home')`
- def index function in views.py and import httpresponse from django.shortcuts 
- the index function Should return Httpresponse

```
def index(request):
    return HttpResponse("this is home page")
```
### Create more end points
- In app/urls.py add more path as you want and also corresponding function you want to run on the path form views.py
```
path("",views.index, name='home'),
path("about",views.about, name='about'),
path("contact",views.contact, name='contact')
```
- Define the function in views.py that what you want to return
```
def index(request):
    return HttpResponse("this is home page")
def about(request):
    return HttpResponse("this is about page")
def contact(request):
    return HttpResponse("this is contact page")
```

- This process is also called url dispaching
## Create static and templates files at the top of the folder
- Adding static files manually
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR / "static")
]
```
- Create a file in static folder this folder is public
- check it is showing in the browser or not
`http://127.0.0.1:8000/static/text.txt`
- Add template file in settings.py 
`os.path.join(BASE_DIR / "static")` DIR templates
- Create index.html and more files in templates folder
- Now render the file in views.py `return render(request,"index.html")`

Passing variable to templates
- Add `{{variable}}` in index.html file
- Add the variable in index function
```
context = {
        "variable":"This is sent"
    }
    return render(request,"index.html", context)
```

## Admin panel setting
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- Creatd admin username and admin password for now
- Login admin setting changes: added this in urls.py of project
```
admin.site.site_header = "Om Chaurasia Admin"
admin.site.site_title = "Om Chaurasia  Admin Portal"
admin.site.index_title = "Welcome to Om Chaurasia backend"
```
## Adding blocks of templates such as header, footer (template inheritance)

- install django extention for suggestion
- Creating block in bash.html which is common in all
```
{% block title %}{% endblock title %}
{% block body %}{% endblock body %}
```
- Extends this in index.html at the top
```
{% extends 'bash.html' %}
```
- Add body in index.html
```
{% block body %}
this is my body
{% endblock body %}
```
- Add block title in index.html
```
{% block title %}
Home
{% endblock title %}
```

## Submitting form in databases
- add csrf token in form 
`{% csrf_token %}` to prove that website is your
- Logic for post request will be in views.py in the function your want to post
- Creating tables in database known as model in models.py
```
class Contact(models.Model):
    name=models.CharField(max_length=122)
    message=models.CharField(max_length=122)
```
- import it in admin.py `from home.models import Contact`
- register the model in admin.py `admin.site.register(Contact)`
- copy the name from apps.py and paste it in setttings.py installed apps `'home.apps.HomeConfig',`
- `python manage.py makemigrations`
- `python manage.py migrate` to generate table
- `from home.models import Contact
` in views.py
- goto views.py in the handling function
- handle the post request and save in database
```
if request.method=="POST":
    name = request.POST.get('name')
    message = request.POST.get('message')
    contact = Contact(name=name , message=message)
    contact.save()
```
- change the record name as name
```
def __str__(self):
    return self.name
```

- alert to submited form import this in settings and views
`from django.contrib.messages import constants as messages`
- added this code in bash to show the success message
```
{% if messages %}
      {% for message in messages %}
      <div class="alert alert-{{message.tags}}   alert-dismissible fade show" role="alert">
          {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endfor %}
      {% endif %}
```
- pass the message variable in views.py after save the model
`messages.success(request,  'Your form has been submitted!')`

## (CURD) data from terminal
- `python manage.py shell`
- import models(table) `from home.models import Contact`
- To print all objects name in data `Contact.objects.all()`
- To print specific objects name in data `Contact.objects.all()[0]`
- To access a attribute of of a objects `Contact.objects.all()[0].name`
- To search in models `Contact.objects.filter(name="Om Chaurasia")` you can also pass two attribute for searching
- to filter first and last object in models
```
Contact.objects.filter().first()
Contact.objects.filter().last()
Contact.objects.all().first()
Contact.objects.all().last()
```
- To update a value in database
```
take=Contact.objects.all()[0]
take.name="hello"
take.save()
```

- go to documentation of django for more search and other queries