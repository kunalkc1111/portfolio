from django.shortcuts import render, HttpResponseRedirect, redirect
from resume.forms import ContactMeForm
from django.contrib import messages
import re
from resume.serializer import ContactSerializer
from resume.models import ContactModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class contactview(APIView):
    def get(self,r):
        contact = ContactModel.objects.all()
        ser = ContactSerializer(contact,many=True)
        return Response(ser.data)

class contactpost(APIView):
    def post(self,r):
        serobj = ContactSerializer(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data)

class contactput(APIView):
    def put(self,r,pk):
        contact = ContactModel.objects.get(pk=pk)
        serobj = ContactSerializer(contact,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data)
        return Response(serobj.errors)
    
class contactpatch(APIView):
    def patch(self,r,pk):
        contact = ContactModel.objects.get(pk=pk)
        serobj = ContactSerializer(contact,data=r.data,partial=True)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data)
        return Response(serobj.errors)
    
class contactdelete(APIView):
    def delete(self,r,pk):
        contact = ContactModel.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_410_GONE)


def contactMe(r):
    # messages.error(r, 'Welcome to ContactME')
    form = ContactMeForm()
    if r.method == 'POST':
        form = ContactMeForm(r.POST)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = r.POST['email']
        number = r.POST['phone']
        if form.is_valid():
            print('form = ',form)
            #check for email
            # if not(re.fullmatch(regex, email)):
            #     print("InValid Email")
            #     messages.error(r,"InValid Email")
            #     return redirect('/portfolio/resume/')

            #check for number
            if not(re.fullmatch(regex, email)) or len(number) > 10 or len(number) < 10:
                messages.error(r,"InValid Number")
                return redirect('/portfolio/resume/')
            
            if not number.isdigit():
                messages.error(r,"InValid Number")
                return redirect('/portfolio/resume/')
            # form_dict= {'form':form}
            else:
                form.save()
                messages.success(r, 'Your Message has been sent successfully!')
                return HttpResponseRedirect('/')
    return render(r,'resume/resume.html',{'form':form})