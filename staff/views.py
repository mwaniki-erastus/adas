from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Staff,Privilege


class StaffProfile(DetailView):
    model = Staff
    template_name = "staff_profile.html"

    def get_context_data(self, **kwargs):
        context = super(StaffProfile, self).get_context_data(**kwargs)
        context['privileges'] = Privilege.objects.filter(staff=self.object)
        # context['flags'] = self.read_audit()

        return context
    


class AddStaff(CreateView):
    model = Staff
    fields = ['first_name','last_name','id_number','email','phone_number','employee_id','role']
    template_name = "add_staff.html"
    success_url = "/dashboard"

class UpdateStaff(UpdateView):
    model = Staff
    fields = ['first_name', 'last_name', 'description']
    template_name = "assets/update_asse.html"

class DeleteStaff(DeleteView):
    model = Staff
    template_name = "assets/delete_asset.html"
    success_url = reverse_lazy('asset-list')





























