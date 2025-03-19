from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book
from .forms import BookForm


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BorrowedBook

from .models import Review
from .forms import ReviewForm


# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'library/login.html', {'error': 'Invalid username or password'})
    return render(request, 'library/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')


##########################

# Helper function to check if user is admin/superadmin
def is_admin(user):
    return user.role in ['admin', 'superadmin']

# View all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# Add a new book (only admins)
@login_required
@user_passes_test(is_admin)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Add'})

# Edit a book (only admins)
@login_required
@user_passes_test(is_admin)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'action': 'Edit'})

# Delete a book (only admins)
@login_required
@user_passes_test(is_admin)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})



###################


# Borrow a book (students can borrow up to 3 books)
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowed_count = BorrowedBook.objects.filter(user=request.user, returned=False).count()

    if borrowed_count >= 3:
        return HttpResponseForbidden("You can only borrow up to 3 books at a time.")
    
    BorrowedBook.objects.create(user=request.user, book=book)
    book.available_copies -= 1
    book.save()
    
    return redirect('book_list')

# Return a book
@login_required
def return_book(request, borrow_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrow_id, user=request.user)
    borrowed_book.returned = True
    borrowed_book.save()
    
    borrowed_book.book.available_copies += 1
    borrowed_book.book.save()
    
    return redirect('book_list')



#######################################


# Submit a Review
@login_required
def submit_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_list')
    else:
        form = ReviewForm()
    
    return render(request, 'library/review_form.html', {'form': form, 'book': book})
