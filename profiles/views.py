from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/profile_list.html'
    paginate_by = 6
    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    
    def get_object(self):
        return get_object_or_404(Profile, user__name=self.kwargs['username'])
