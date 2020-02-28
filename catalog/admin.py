from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status', 'due_back')
    


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')



# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Book)
admin.site.register(Genre)