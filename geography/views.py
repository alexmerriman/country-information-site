from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Area, Attraction


COUNTRY_NAME = "North Korea (Democratic People's Republic of Korea)"


def geography_page_meta():
    return {
        "title": "Geography",
        "last_updated": None,
    }


def areas_page_meta():
    return {
        "title": "Areas",
        "last_updated": None,
    }


def attractions_page_meta():
    return {
        "title": "Attractions",
        "last_updated": None,
    }


def index(request):
    areas = Area.objects.prefetch_related('attraction_set').all()
    return render(request, 'geography/index.html', {
        'areas': areas,
        'country': COUNTRY_NAME,
        'page_title': 'Geography',
        'page_meta': geography_page_meta(),
    })


class AreaList(ListView):
    model = Area
    template_name = 'geography/area_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Areas'
        context['page_meta'] = areas_page_meta()
        return context


class AttractionList(ListView):
    model = Attraction
    template_name = 'geography/attraction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Attractions'
        context['page_meta'] = attractions_page_meta()
        return context


class AreaDetail(DetailView):
    model = Area
    template_name = 'geography/area_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = self.object.area_name
        context['page_meta'] = {
            "title": self.object.area_name,
            "last_updated": None,
        }
        return context


class AttractionDetail(DetailView):
    model = Attraction
    template_name = 'geography/attraction_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = self.object.attraction_name
        context['page_meta'] = {
            "title": self.object.attraction_name,
            "last_updated": None,
        }
        return context


class AreaCreate(CreateView):
    model = Area
    template_name = 'geography/area_form.html'
    fields = ['area_name', 'area_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Create Area'
        context['page_meta'] = {
            "title": "Create Area",
            "last_updated": None,
        }
        return context


class AreaUpdate(UpdateView):
    model = Area
    template_name = 'geography/area_form.html'
    fields = ['area_name', 'area_type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Update Area'
        context['page_meta'] = {
            "title": "Update Area",
            "last_updated": None,
        }
        return context


class AreaDelete(DeleteView):
    model = Area
    template_name = 'geography/area_confirm_delete.html'
    success_url = reverse_lazy('arealist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Delete Area'
        context['page_meta'] = {
            "title": "Delete Area",
            "last_updated": None,
        }
        return context


class AttractionCreate(CreateView):
    model = Attraction
    template_name = 'geography/attraction_form.html'
    fields = ['area', 'attraction_name', 'description', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Create Attraction'
        context['page_meta'] = {
            "title": "Create Attraction",
            "last_updated": None,
        }
        return context


class AttractionUpdate(UpdateView):
    model = Attraction
    template_name = 'geography/attraction_form.html'
    fields = ['area', 'attraction_name', 'description', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Update Attraction'
        context['page_meta'] = {
            "title": "Update Attraction",
            "last_updated": None,
        }
        return context


class AttractionDelete(DeleteView):
    model = Attraction
    template_name = 'geography/attraction_confirm_delete.html'
    success_url = reverse_lazy('attractionlist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = COUNTRY_NAME
        context['page_title'] = 'Delete Attraction'
        context['page_meta'] = {
            "title": "Delete Attraction",
            "last_updated": None,
        }
        return context
