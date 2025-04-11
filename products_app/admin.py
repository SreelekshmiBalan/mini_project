from django.contrib import admin
from .models import Category,Product,ProductImage

# Register your models here.
admin.site.site_header='The Golden Hanger Admin'
admin.site.site_title='The Golden Hanger Dashboard'
admin.site.index_title='Welcome to your Shop Admin'
admin.site.register(Category)
admin.site.register(ProductImage)

class ProductImageAdmin(admin.TabularInline):
    model=ProductImage
    extra=1

class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Product_Code','Material','Type','Price','Availability','Stock','Best_Seller','New_Launch')
    list_filter=('Availability','category','Material','Type','New_Launch','Best_Seller')
    search_fields=('Name','Product_Code','Colour')
    fieldsets = (
        ('Basic Info',{
            'fields':('Name','Product_Code','category','Colour','Material','Type','Wash_Care','Price','Best_Seller','New_Launch')
        }),
        ('Stock and Availability',{
            'fields':('Availability','Stock')
        }),
    )
    inlines=[ProductImageAdmin]

admin.site.register(Product, ProductAdmin)


