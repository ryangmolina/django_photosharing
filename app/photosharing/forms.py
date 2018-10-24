from django.forms import ModelForm

from .models import Photo, Team

# Forms can be created like this, then pass it as a form_class for FormView
# But, it's better to use CreateView when dealing with creation of objects.
# FormView with form_class must only be used on forms like Contact-Us
class PhotoUploadForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'public', )


class TeamCreateForm(ModelForm):
    class Meta:
        model = Team
        fields = ('logo', 'name', 'description')