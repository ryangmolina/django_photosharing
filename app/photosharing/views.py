from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from .forms import PhotoUploadForm
from .models import Photo, Team


class PhotoListView(generic.ListView):
    model = Photo
    template_name = 'photosharing/pages/home.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.filter(public=True)


class TeamPhotoListView(generic.ListView):
    model = Photo
    template_name = 'photosharing/pages/photo_list.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.filter(
            uploaded_to=self.kwargs.get('pk')
        )


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    template_name = 'photosharing/pages/team.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.filter(
            Q(members__in=[self.request.user]) |
            Q(owner=self.request.user)
        )


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = ['name', 'description', 'logo']
    template_name = 'photosharing/pages/create_team.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = 'photosharing/pages/team_details.html'
    context_object_name = 'team'


class PhotoUploadView(LoginRequiredMixin, generic.FormView):
    form_class = PhotoUploadForm
    template_name = 'photosharing/pages/photo_upload_form.html'

    def form_valid(self, form):
        form.instance.uploaded_to = Team.objects.get(pk=self.kwargs.get('pk'))
        form.instance.uploader = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('photosharing:photo_details',
                            kwargs={'pk': self.object.pk})


class PhotoDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Photo
    template_name = 'photosharing/pages/photo_details.html'
    context_object_name = 'photo'
