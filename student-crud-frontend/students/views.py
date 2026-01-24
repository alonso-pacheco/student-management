import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View

API_URL = settings.API_URL

# Create your views here.
class Index(View):

    template_name = 'students/index.html'

    def get(self, request):
        try:
            response = requests.get(API_URL)
            students = response.json()
        except Exception as e:
            students = []
            messages.error(request, "Error al obtener datos de los estudiantes")
        return render(request, self.template_name, {"students": students})


class Student(View):
    template_name = 'students/form.html'

    def get(self, request, id=None):
        action = "Agregar"
        student = {}
        if id:
            action = "Editar"
            try:
                student_url = f"{API_URL}/{id}"
                response = requests.get(student_url)
                student = response.json()
            except:
                messages.error(request, "Error al obtener datos del estudiante")
        
        return render(request, self.template_name,
                      {"is_edit": action == "Editar",
                       "action": action,
                       "student": student
                    })
    
    def post(sefl, request, id = None):
        data = {
            'name': request.POST.get('name'),
            'age': int(request.POST.get('age')),
            'email': request.POST.get('email')
        }
        try:
            if id:
                # Edit student
                student_url = f"{API_URL}/{id}"
                response = requests.put(student_url, json=data)
                if response.status_code == 200:
                    messages.success(request, "Estudiante actualizado correctamente")
                else:
                    messages.error(request, "Error al actualizar el estudiante")
            else:
                # Create student
                response = requests.post(API_URL, json=data)
                if response.status_code == 201:
                    messages.success(request, "Estudiante creado correctamente")
                else:
                    messages.error(request, "Error al crear estudiante")
        except:
            messages.error(request, "Error al conectar con la API")
        return redirect('students:index')
    

    def delete(self, request, id):
        student_url = f"{API_URL}/{id}"
        try:
            response = requests.delete(student_url)
            if response.status_code == 200:
                messages.success(request, "Estudiante eliminado correctamente")
            else:
                messages.error(request, "Error al eliminar estudiante")
        except:
            messages.error(request, "Error al conectar con la API")
        return redirect('students:index')
