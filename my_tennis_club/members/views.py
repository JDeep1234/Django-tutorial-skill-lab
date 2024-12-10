#from django.http import HttpResponse
#from django.template import loader

#def members(request):
#  template = loader.get_template("C:\\Users\\jnyanadeep\\myworld\\my_tennis_club\\members\\templates\\firest.html")
#  return HttpResponse(template.render())


#from django.http import HttpResponse
#from django.template import loader
#from .models import Member

#def members(request):
 # mymembers = Member.objects.all().values()
 # template = loader.get_template('members.html')
  #context = {
   # 'mymembers': mymembers,
  #}
  #return HttpResponse(template.render(context, request))
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all()  # Fetch all members
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)  # Fetch member by ID
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

  