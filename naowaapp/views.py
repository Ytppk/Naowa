from django.shortcuts import render,Http404, HttpResponseRedirect, get_object_or_404
from .models import Members
from django.db.models import Q
import random
from .forms import MemReg

# Create your views here.

def search(request):
    try:
        query = request.GET.get('query')
    except:
        query = None
    if query:
            members = Members.objects.filter(Q(name__icontains=query) | Q(rank__icontains=query) | Q(appointment__icontains=query))
            context = {'query': query, 'members': members}
            template = 'search.html'
    else:
        template = 'search.html'
        context = {}
    return render(request, template, context)

def homepage(request):
    members = Members.objects.all()
    template = 'index.html'
    context = {'members': members}
    return render(request, template, context)

def result(request, slug):
    # member = (Members, slug)
    # similar_rank = list(memberss.exclude(id=member.id))
    # if len(similar_rank) >= 4:
    #     similar_rank = random.sample(similar_rank, 4)

    members = Members.objects.get(slug=slug)
    context = {'members': members}
    template = 'result.html'
    return render(request, template, context)

def adddata(request):
    if request.method == 'POST':
        fm = MemReg(request.POST, files=request.FILES)
        if fm.is_valid():
            ct = fm.cleaned_data['category']
            nm = fm.cleaned_data['name']
            sl = fm.cleaned_data['slug']
            hn = fm.cleaned_data['husbandname']
            rk = fm.cleaned_data['rank']
            ap = fm.cleaned_data['appointment']
            ph = fm.cleaned_data['phone']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            db = fm.cleaned_data['dob']
            im = fm.cleaned_data['image']
            reg = Members(category=ct, name=nm, slug=sl, husbandname=hn, rank=rk, appointment=ap, phone=ph, email=em, address=ad, dob=db, image=im)
            reg.save()
    else:
        fm = MemReg()
    memb = Members.objects.all()
    return render(request, 'addmember.html', {'form':fm, 'mem':memb,})

            




    
    
