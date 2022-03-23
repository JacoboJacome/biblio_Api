from datetime import datetime

from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.empty_value_display = "No valor"

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = "Unknow"
    fieldsets = [
        (None, {'fields': ['name','last_name','description']})
    ]

    list_display = ('name', 'last_name','description')
    search_fields = ('name','last_name',)

class BookItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Books Information", {
            'fields': ('title','added', 'subject')
        }),('The author', {
            'fields': ('ref_author',),
        })

    ]

    list_display = ('added','book')
    list_display_links = ('book',)
    # list_editable = ('question_text',)
    # date_hierarchy = 'pub_date'
    save_on_top = True
    # list_filter = ('title',)
    # autocomplete_fields = ['ref_author']


    # def has_been_published(self, obj):
    #     present =  datetime.now()
    #     return obj.pub_date.date() < present.date()

    # has_been_published.boolean = True

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    list_filter = ('title',)
    search_fields = ('title',)
    # list_display_links = ('author',)


admin.site.register(Author,AuthorAdmin)
admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Book)
