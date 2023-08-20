from django.shortcuts import render


from . import forms, models



def BookCreateView(request):
    model = models.Book
    form = forms.BookForm()
    context = {
        'form':form
    }
    
    return render(request, 'appformselect2/book_form.html', context=context)
