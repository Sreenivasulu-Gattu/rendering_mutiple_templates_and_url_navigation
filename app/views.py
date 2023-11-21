from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')
def amazon(request):
    return render(request,'amazon.html')
def flipcart(request):
    return render(request,'flipcart.html')
