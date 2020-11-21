from django.shortcuts import render,redirect
from .models import customers,transactionhistory
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request,'banksys/home.html')

def customer_view(request):
    cust=customers.objects.all()
    return render(request,'banksys/customer_view.html',{'cust':cust})

def profile(request, id):
    customer=customers.objects.get(id=id)
    return render(request,'banksys/profile.html',{'customer':customer})

def transaction(request, pk):
    sndr=customers.objects.get(id=pk)
    return render(request,'banksys/transaction.html',{'sndr':sndr})

def transfer(request, pk):
    sndr=customers.objects.get(id=pk)
    if request.method=='POST':
        recvr=customers.objects.get(account_number=request.POST['Reciver account name'])
        if float(request.POST['amount'])>sndr.bal:
            messages.error(request,'Insufficient Balance')
            #transactionhistory.objects.create(sender=sndr,receiver=recvr,amount=int(request.POST['amount']),result='Failed')
            # obj1.save()
            try:
                transactionhistory.objects.create(sender=sndr, receiver=recvr, amount=float(request.POST['amount']),
                                                  result='Failed')
            except Exception as e:
                print(e)
            return redirect('transaction', pk)
        else:
            recvr.bal=recvr.bal+float(request.POST['amount'])
            recvr.save()
            sndr.bal=sndr.bal-float(request.POST['amount'])
            sndr.save()
            #transactionhistory.objects.create(sender=sndr, receiver=recvr, amount=int(request.POST['amount']),
             #                                 result='Successful')
            messages.success(request, 'Transferred Succesfully')
            try:
                transactionhistory.objects.create(sender=sndr, receiver=recvr, amount=float(request.POST['amount']),
                                                  result='Successful')
            except Exception as e:
                print(e)
            # new.save()
            return redirect('cust-view')
    return render(request,'banksys/transaction.html',{'sndr':sndr})

def Transactionhistory(request):
    obj=transactionhistory.objects.all()
    return render(request,'banksys/transactionhistory.html',{'obj':obj})

class customer_view(ListView):
    model = customers
    template_name = 'banksys/customer_view.html'
    context_object_name = 'customer_viw'
    ordering = ['account_number']
    paginate_by = 4

