from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from ..photosharing.models import Team
from .models import Invite


class InviteListView(LoginRequiredMixin, generic.ListView):
    model = Invite
    template_name = 'photosharing/pages/invite.html'
    context_object_name = 'invites'

    def get_queryset(self):
        return Invite.objects.filter(invited=self.request.user)


class InviteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Invite
    fields = ['invited']
    template_name = 'photosharing/pages/create_invite.html'

    def form_valid(self, form):
        form.instance.inviter = Team.objects.get(pk=self.kwargs.get('pk'))
        self.object = form.save()
        return super().form_valid(form)


class InviteDetailsView(LoginRequiredMixin, generic.DetailView):
    model = Invite
    template_name = 'photosharing/pages/invite_details.html'
    context_object_name = 'invite'


class InviteRejectView(LoginRequiredMixin, generic.DeleteView):
    model = Invite

    def get(self, *args, **kwargs):
        # bypass the display of confirm delete template
        return self.post(*args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Invite, pk=pk)

    def get_success_url(self):
        return reverse('photosharing:invite_list',
                       kwargs={'pk': self.request.user.id})


class InviteAcceptView(LoginRequiredMixin, generic.RedirectView):

    def get(self, request, *args, **kwargs):
        invite = Invite.objects.get(pk=self.kwargs.get('pk'))
        inviter = invite.inviter
        invited = invite.invited
        inviter.members.add(invited)
        inviter.save()

        invite.delete()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('invites:invite_list')