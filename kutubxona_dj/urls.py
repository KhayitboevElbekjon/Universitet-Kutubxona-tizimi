from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_login),
    path('logaut/',logaut_view),
    path('register/',register_view),
    path('salom/', salomlash),
    path('hello/', salom_ber),
    path('bosh_sahifa/', bosh_sahifa),
    path('talabalar/', TalabalarView.as_view()),
    path('talaba/<int:son>/',bitta_talaba),
    # path('idd/',studentlar)
    path('all_mualliflar/',all_muallif),
    path('muallif/<int:num>',muallif),
    path('mashq/<int:son>',mashq),
    path('tanlangan_kitob/',idd),

    path('record/',Record_view.as_view()),

    path('tirik_mualliflar/',tirik_mualliflar),
    path('sahifa/',badiy),
    path('yosh/',yosh),
    path('kitob_soni/',kitob_soni),
    path('admin_p/', admin_pannel),
    path('one_record/',one_record),
    path('more_record/<int:son>/',more_record),
    path('bit_talaba/',bit_talaba),
    path('talaba_uchir/<int:son>/',talaba_uchir),
    path('muallif_uchir/<int:num>/',muallif_uchir),
    path('kitoblar/',kitoblar),
    path('record_delete/<int:son>/',record_delete),
    path('record_del/<int:son>',record_del),
    path('admin_del/<int:son>',admin_del),
    path('admin_edit/<int:son>',admin_edit),
    path('muallif_edit/<int:son>',muallif_edit),
    path('rec_edit/<int:son>',record_edit),
    # path('one_kitob/<int:son>',one_kitob)


]
