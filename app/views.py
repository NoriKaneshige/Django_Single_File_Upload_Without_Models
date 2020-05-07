from django.views import generic
from .forms import SingleUploadForm


class SingleUploadView(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)

# form.save() gives file's URL path, ant put it into context