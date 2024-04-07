from django.contrib import admin

from Market.models import Books


# Register your models here.
# admin.site.register(Books)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'category', 'author_name', 'image']
    search_fields = ['name', 'author_name']
