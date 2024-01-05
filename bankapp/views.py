from django.shortcuts import render,redirect
from . forms import PersonCreationForm
from . models import District,Branch
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def create_person(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Application Accepted')
            return redirect('bank:home')
    return render(request,'details.html',{'form':form})

def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown.html', {'branches': branches})

def connect(request):
    return render(request,'connector.html')

def success(request):
    return render(request,'success.html')