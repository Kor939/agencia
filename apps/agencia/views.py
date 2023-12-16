import os
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Auto, Modelo, Marca, MarcaModelo

class ModeloListView(ListView):
    model = Modelo
    template_name = "agencia/modelos/modelo_list.html"
    context_object_name = "modelos"

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = "agencia/autos/auto_confirm_delete.html"
    context_object_name = "auto"
    success_url = reverse_lazy("auto_list")

    def form_valid(self, form):

        auto = self.get_object()


        if auto.imagen:

            image_path = auto.imagen.path


            if os.path.exists(image_path):
                os.remove(image_path)

        return super().form_valid(form) 