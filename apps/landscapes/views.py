from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print ("Hello Wooooorld!")
    return render(request, 'landscapes/index.html')

def show(request, id):
    id=int(id)
    print type(id)
    image_path = "landscapes/img/"
    if id in range(1,11):
        image_path+='snow'
    elif id in range (11,21):
        image_path+='desert'
    elif id in range (21,31):
        image_path+='forest'
    elif id in range (31,41):
        image_path+='vineyard'
    elif id in range (41,51):
        image_path+='tropical'
    else:
        return redirect('/')
    context = {'img' : image_path +'.jpg'}
    print image_path
    return render(request, 'landscapes/show.html', context)
