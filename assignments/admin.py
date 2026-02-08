from django.contrib import admin
from .models import AboutUs, SocialLink
# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    list_display=('name','description')

    def has_add_permission(self, request):
        count = AboutUs.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(SocialLink)