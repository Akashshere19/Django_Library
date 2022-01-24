from django.shortcuts import render,redirect
from .models import BookRecord
from .forms import BookRegistration
from django.contrib import messages

# Create your views here.
def add_book(request):
    if request.method=='POST':
        bn=BookRegistration(request.POST)
        if bn.is_valid():
            nb=bn.cleaned_data['BookName']
            od=bn.cleaned_data['OutDate']
            id=bn.cleaned_data['InDate']
            un=bn.cleaned_data['UserName']
            mb=bn.cleaned_data['MobNo']
            reg=BookRecord(BookName=nb,OutDate=od,InDate=id,UserName=un,MobNo=mb)
            reg.save()
            messages.success(request,"your details has been submitted.!")
            bn=BookRegistration()
    else:
        bn=BookRegistration()
    show=BookRecord.objects.all()
    return render(request,'update.html',{'form':bn,'show':show})

def delete_data(request,id):
    if request.method == 'POST':
        delete = BookRecord.objects.get(pk=id)
        delete.delete()
        messages.info(request,"Delete Successfully.")
        return redirect('/')
def update_data(request,id):
    if request.method =='POST':
        edit =BookRecord.objects.get(pk=id)
        bn = BookRegistration(request.POST,instance=edit)
        if bn.is_valid():
            bn.save()
        messages.info(request, "Update Successfully.")
    else:
        edit = BookRecord.objects.get(pk=id)
        bn = BookRegistration(instance=edit)
    return render(request, 'update.html', {'form':bn})
    return redirect('/')
