from django.contrib import admin
from .models import Category, City, Ad, Conversation, Message


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_at', 'updated_at')
    search_fields = ('title',)


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('sender', 'text', 'created_at', 'updated_at', 'is_read')
    can_delete = False

class ConversationInline(admin.TabularInline):
    model = Conversation
    extra = 0
    readonly_fields = ('id', 'buyer', 'seller', 'created_at', 'updated_at')
    can_delete = False
    show_change_link = True


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'city', 'slug', 'user', 'category', 'price', 'active', 'created_at', 'updated_at')
    search_fields = ('title',)
    inlines = [ConversationInline]


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad', 'buyer', 'seller', 'created_at', 'updated_at')
    search_fields = ('buyer__phone_number', 'seller__phone_number', 'ad__title')
    list_filter = ('created_at',)
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'text', 'created_at', 'updated_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('text', 'sender__phone_number')
    ordering = ('-created_at',)