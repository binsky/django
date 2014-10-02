from django.contrib import admin

from books_app.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')
    list_filter = ('publication_date',)
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)
    # raw_id_fields = ('publisher',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')
    list_filter = ('country',)
    ordering = ('country',)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)