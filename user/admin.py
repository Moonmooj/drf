from django.contrib import admin
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

# 사용 방법은 TabulaInline과 StackedInline 모두 동일
# 둘 다 사용해보고 뭐가 좋은지 비교해보기
# class UserProfileInline(admin.TabularInline):
class UserProfileInline(admin.StackedInline):  # 유저가 유저프로필을 역참조하고 있기떄문에 유저어드민에서 인라인 가능 (역참조일때만가능)
    model = UserProfileModel
    filter_horizontal = ['hobby']

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

    inlines = (
            UserProfileInline,
        )


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
