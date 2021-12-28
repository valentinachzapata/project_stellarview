from django.contrib import admin
from stellarapp import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author') #nos permite editar el display de admin
    prepopulated_fields = { 'slug' : ('title',), } #

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'published', 'status')
    list_filter = ('status', 'published')
    search_fields = ('name', 'email', 'content')

admin.site.register(models.Category)