from django.shortcuts import render, HttpResponse, redirect
from . forms import CvForm, ContactForm, ProjectForm, CategoryForm
from . models import Cv, Project, Category, ContactMessage
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

def index(request):
    cv_list = Cv.objects.get(id=2)
    cv = cv_list.pdf.url
    categories = Category.objects.all()
    projects = Project.objects.all()
    context = {'cv':cv, 'categories':categories, 'projects':projects,}
    return render(request, 'portfolio/index.html', context)

def about(request):
    cv_list = Cv.objects.get(id=2)
    cv = cv_list.pdf.url
    context = {'cv':cv}
    return render(request, 'portfolio/about.html', context)

def projects(request):
    category = request.GET.get('category')
    if category == None:
        all_projects = Project.objects.all()
    else:
        all_projects = Project.objects.filter(category__name=category)
    categories = Category.objects.all()

    context = {'categories':categories, 'all_projects':all_projects}
    return render(request, 'portfolio/projects.html', context)

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Category added!')
            return redirect('add-category')
    else:
        form = CategoryForm()

    context = {'form':form}
    return render(request, 'portfolio/add-category.html', context)

@login_required(login_url='login')
def add_projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new Project has been added to your Portfolio.')
            return redirect('add-projects')
    else:
        form = ProjectForm()

    context = {'form':form}
    return render(request, 'portfolio/add-project.html', context)

@login_required(login_url='login')
def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your new Project has been added to your Portfolio.')
            return redirect('projects')
        
    context = {'form':form}
    return render(request, 'portfolio/edit-project.html', context)

@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project': project}
    return render(request, 'portfolio/delete.html', context)

def project_details(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request, 'portfolio/project-detail.html', context)

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            full_name = contact_form.cleaned_data.get('full_name')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')

            html = render_to_string('portfolio/contactform.html', {
                'full_name':full_name,
                'email':email,
                'subject': subject,
                'message': message
            })

            try:
                send_mail(
                subject,
                message,
                email,
                ['anixar4architecture@gmail.com',],
                fail_silently=False,
                html_message=html
            )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, f'Dear {full_name}, Your email has been received.\nI will respond shortly. Thank You!')
            return redirect('contact')
        messages.error(request, "Error! Message not sent.")
    else:
        contact_form = ContactForm()
    context = {'contact_form':contact_form}
    return render(request, 'portfolio/contact.html', context )

@login_required(login_url='login')
def upload_cv(request):
    if request.method == 'POST':
        cv_form = CvForm(request.POST, request.FILES)
        if cv_form.is_valid():
            cv_form.save()
            messages.success(request, 'Upload Successful!')
            return redirect('upload')
    else:
        cv_form = CvForm()
    context = {'cv_form':cv_form}
    return render(request, 'portfolio/upload-cv.html', context)