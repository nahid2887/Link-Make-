from django.shortcuts import render,get_object_or_404
from .models import Link, Profile
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class LinkListView(ListView):
    model = Link
      # Specify your template here
    context_object_name = 'links'  # Name to use in the template for the list of objects
class LinkCreateView(CreateView):
    model=Link
    fields='__all__'
    success_url = reverse_lazy('LinkListView')

class LinkUbdate(UpdateView):
    model = Link  # Model name should be capitalized
    fields = ['text','url']  # Use '__all__' to include all fields from the model
    success_url = reverse_lazy('LinkListView')

class Linkdelet (DeleteView):
    model=Link
    success_url = reverse_lazy('LinkListView')

def profile_view(request, profile_slug):
    # Fetch the Profile object based on the slug
    profile = get_object_or_404(Profile, slug=profile_slug)
    
    # Assuming Profile has a 'link' related field (many-to-many or foreign key)
    link = profile.Link.all()
    
    # Prepare the context to pass to the template
    context = {
        'profile': profile,
        'link': link,
    }
    
    # Render the template with the context
    return render(request, 'myapp/profile.html', context)