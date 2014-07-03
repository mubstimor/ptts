from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tracker.forms import ContactForm, QuickContactForm
from tracker.models import *
from tracker.serializers import *
from rest_framework.decorators import api_view
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login
from django import template

register = template.Library()

# Applications' views here.
def home(request):
    return  render_to_response("index.html")

def about(request):
    return render_to_response("about.html")

def time(request):
    return render_to_response("poptime.html")

def contact(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
                subject = form.cleaned_data['subject']
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']
                recipients = ['info@example.com']

                if cc_myself:
                    recipients.append(sender)

                    from django.core.mail import send_mail
                    send_mail(subject, message, sender, recipients)
                    #return render_to_response("contact.html")
                    return HttpResponseRedirect('/thankyou/') # Redirect after POST
                else:
                    return HttpResponse('Make sure all fields are entered and valid.')

    else:
        form = ContactForm() # An unbound form
        return render_to_response('contact.html', {'form': form, }, context)

def quickContact(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = QuickContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
                subject = form.cleaned_data['subject']
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']
                recipients = ['info@example.com']

                if cc_myself:
                    recipients.append(sender)

                    from django.core.mail import send_mail
                    send_mail(subject, message, sender, recipients)
                    #return render_to_response("contact.html")
                    return HttpResponseRedirect('/thankyou/') # Redirect after POST
                else:
                    return HttpResponse('Make sure all fields are entered and valid.')

    else:
        form = QuickContactForm() # An unbound form
        return render_to_response('footer.html', {'form': form, }, context)

def thankyou(request):
    return render_to_response('thankyou.html')

#def contact(request):
#    return render_to_response("contact.html")

def demo(request):
    return render_to_response("demo.html")

def benefits(request):
    return render_to_response("benefits.html")

def gps(request):
    return render_to_response("gps.html")

def routes(request):
    return render_to_response("routes.html", {'routes': Route.objects.all()} )

def route_stops(request, route_id = 1):
	return render_to_response('route_stops.html', {'route_stops': Stop.objects.filter(id = route_id) })

def find_bus(request):
    route = Route.objects.all()
    variables = RequestContext(request,{"routes":route})
    return render_to_response("find_bus.html", variables)

def find_bus_location(request):
    location = coordinate.objects.all()
    locationdata = RequestContext(request,{"locationdata":location})
    return render_to_response("find_bus.html", locationdata)

def bus_route_details(request):
    details = Buse.objects.filter(id=1, imei="0.332335").select_related()
    bus_loc_details = RequestContext(request,{"buslocdetails":details})
    return render_to_response("find_bus.html", bus_loc_details)

def current_bus_location(request):
    location = coordinate.objects.select_related()
    buslocations = RequestContext(request,{"buslocations":location})
    return render_to_response("find_bus.html", buslocations)


@register.inclusion_tag('find_bus.html')
def show_results(request):
    locations = coordinate.objects.all()
    return {'locations': locations}

def rstops(request, route_id=1):
    return ('find_bus.html', {'route_stops': Stop.objects.filter(id = route_id) })

def get_started(request):
    return render_to_response("get_started.html")

class UserViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows users to be viewed or edited.
     """
     queryset = User.objects.all()
     serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows groups to be viewed or edited.
     """
     queryset = Group.objects.all()
     serializer_class = GroupSerializer

class RouteViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows routes to be viewed or edited.
     """
     queryset = Route.objects.all()
     serializer_class = RouteSerializer

class BusViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows routes to be viewed or edited.
     """
     queryset = Buse.objects.all()
     serializer_class = BusSerializer

class StopsViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allows stops to be viewed or edited.
     """
     queryset = Route.objects.all()
     serializer_class = StopSerializer

@api_view(['GET', 'POST'])
def cordinate_list(request):
    """
    List all cordinates, or create a new one.
    """
    if request.method == 'GET':
        snippets = coordinate.objects.all()
        serializer = CordinateSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CordinateSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bus_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Buse.objects.get(pk=pk)
    except Buse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BusSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def search_bus(request, license):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Buse.objects.filter(license_number= license)
    except Buse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BusSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_currentBusLocations(request, route):
    """
    Retrieve a snippet instance.
    """
    try:
        snippet = coordinate.objects.filter(route_id= route)
    except coordinate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(snippet, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_stopsOnRoute(request, route):
    """
    Retrieve a snippet instance.
    """
    try:
        snippet = Stop.objects.filter(route= route)
    except Stop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RouteStopSerializer(snippet, many=True)
        return Response(serializer.data)