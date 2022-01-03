from django.contrib import admin
from home.models import Category, Product, Images, Brand, Size,Color
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import admin_thumbnails


class NewsAdminForm(forms.ModelForm):
    detail = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'



@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']


class ProductAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['title','category']
    list_filter = ['category']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)