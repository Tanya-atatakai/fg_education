from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin

from .models import Tag, BlogPost

blogpost_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
blogpost_fieldsets[0][1]["fields"].extend(["content", "tag", "user"])
blogpost_fieldsets = list(blogpost_fieldsets)
blogpost_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("tag",)


class BlogPostAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = blogpost_fieldsets
    list_filter = blogpost_list_filter
    filter_horizontal = ("tag", )

    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        OwnableAdmin.save_form(self, request, form, change)
        return DisplayableAdmin.save_form(self, request, form, change)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
