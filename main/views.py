from django.shortcuts import render,redirect
from .models import Settings
from blog.models import Post
from about.models import About, Our_Services, Img_services
from .forms import MessageForm
from django.contrib import messages




# Home Templates
def main(request):
    about = About.objects.last()
    services = Our_Services.objects.all()
    img_services = Img_services.objects.all()
    post = Post.objects.all()
    return render(request, 'index.html', 
        {
            'about': about,
            'services': services,
            'img_services': img_services,
            'post': post,
            })



# Contact Templates
def contact(request):
    settings = Settings.objects.last()
    if request.method == 'POST':
        form = MessageForm(request.POST or None)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
        return redirect('/contact/')
    else:
        form = MessageForm(request.POST or None)


    return render(request, 'contact.html', 
            {
            'settings': settings,
            'form': form
            })
    