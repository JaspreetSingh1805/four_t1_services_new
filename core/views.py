from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'


class ServicesView(TemplateView):
    template_name = 'core/services.html'


class CalloutMaintenanceView(TemplateView):
    template_name = 'core/callout_maintenance.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            # Form submission processing (e.g., store in database or send email)
            messages.success(
                request,
                f"Thanks {name}, we'll be in touch shortly! Our team has received your enquiry."
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                "There was an issue submitting your request. Please check the fields below and try again."
            )
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
