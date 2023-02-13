from django.contrib import admin
from .models import *
@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display=('id','ism','kitoblar_soni','bitiruvchi','kurs') # hamma ma'lumot ko'rinish uchun
    list_display_links=('id',)   # biror bir ustunni linkka aylantirish uchun
    list_editable=('kurs','kitoblar_soni','bitiruvchi') # edit boladigan ustunlar Eslatma: link uchun berilgan ustunni edit uchun berib bolmaydi
    list_filter=('bitiruvchi',) # filterlash uchun
    list_per_page=8 # Maluotlarni 8 tadan bolib beradi har bir page ga
    search_fields=('id','ism') # qidirish uchun id va ism uchun

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display=('id','ism','tirik','kitoblar_soni','jinsi','yosh')
    list_display_links=('id','ism')
    list_editable=('kitoblar_soni','tirik')
    search_fields=('ism',)
    list_filter=('tirik',)

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    autocomplete_fields=('mualif_fk',)
    search_fields=('nom',)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display=('ism','ish_vaqti')
    list_filter=('ish_vaqti',)
    search_fields=('ism',)

# admin.site.register(Admin)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Talaba)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    autocomplete_fields=('talaba_fk','kitob_fk','admin_fk')

    list_display=('talaba_fk','kitob_fk','admin_fk','olingan_sana','qaytarish_sana','qaytarildi')
    search_fields=('talaba_fk',)


# admin.site.register(Record)



