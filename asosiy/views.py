from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.views import View

# from django.contrib.auth.models import User

from .forms import *  # djangodagi Forma uchun

def salomlash(request):
    return HttpResponse('salom,dunyo')

def salom_ber(request):
    data = {'ism': 'Islom', 'ismlar':['Ali', 'Vali', "G'ani"]}
    return render(request,'salom.html',data)

def bosh_sahifa(request):
   return render(request,'bosh_sahifa.html')

# Bazaga ma'lumot qo'shish uchun

# djangoda FORMA uchun -->

class TalabalarView(View):
    def post(self,request):
        forma=TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism=forma.cleaned_data.get('name'),
                kurs=forma.cleaned_data.get('course'),
                bitiruvchi=forma.cleaned_data.get('graduate'),
                kitoblar_soni=forma.cleaned_data.get('books')
            )
        return redirect('/talabalar')
    def get(self,request):
        if request.user.is_authenticated:
            data={'talabalar':Talaba.objects.all(),
                  'forma':TalabaForm}
            return render(request,'talabalar.html',data)
        return redirect('/')

# def hamma_talabalar(request):
#     if request.method=='POST':
#         forma=TalabaForm(request.POST)
#         if forma.is_valid():
#             Talaba.objects.create(
#                 ism=forma.cleaned_data.get('name'),
#                 kurs=forma.cleaned_data.get('course'),
#                 bitiruvchi=forma.cleaned_data.get('graduate'),
#                 kitoblar_soni=forma.cleaned_data.get('books')
#             )
#         return redirect('/talabalar')
#
#
#     data={'talabalar':Talaba.objects.all(),
#           'forma':TalabaForm}
#     return render(request,'talabalar.html',data)


# Update uchun
def bitta_talaba(request,son):
    if request.method=='POST':
        if request.POST.get('b')=='on':
            bitiruvchi_qiy=True
        else:
            bitiruvchi_qiy=False
        Talaba.objects.filter(id=son).update(
            ism=request.POST.get('ism'),
            bitiruvchi=bitiruvchi_qiy,
            kurs=request.POST.get('kurs'),
            kitoblar_soni=request.POST.get('kitoblar_soni')
        )
        return redirect('/talabalar')
    data={'talaba':Talaba.objects.get(id=son)}
    return render(request,'talaba.html',data)


# Qidirish uchun funksiyalar--------------------------------------

def all_muallif(request):
    if request.method=='POST':
        forma=MuallifForm(request.POST)
        if forma.is_valid():
            Muallif.objects.create(
            ism=forma.cleaned_data.get('ism'),
            tirik=forma.cleaned_data.get('tirik'),
            kitoblar_soni = forma.cleaned_data.get('kitoblar_soni'),
            jinsi = forma.cleaned_data.get('jinsi'),
            yosh=forma.cleaned_data.get('yosh')
            )
        return redirect('/all_mualliflar')

    qidirish=request.GET.get('qidirish')
    if qidirish is None or qidirish=='':
        all_muallif = Muallif.objects.all()
    else:
        all_muallif=Muallif.objects.filter(ism__contains=qidirish)
    data={'muallif':all_muallif,
          'forma':MuallifForm}
    return render(request,'all_muallif.html',data)



def kitoblar(request):

    if request.method=='POST':
        forma=KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Kitob.objects.create(
        #     nom=request.POST.get('nom'),
        #     sahifa=request.POST.get('sahifa'),
        #     mualif_fk=Muallif.objects.get(id=request.POST.get('muallif')),
        #     janr=request.POST.get('janr')
        # )
        return redirect('/kitoblar/')

    nom=request.GET.get('nom')
    if nom is None or nom=='':
        data1=Kitob.objects.all()
    else:
        data1=Kitob.objects.filter(nom__contains=nom)
    data={'kitoblar':data1,
          'muallif':Muallif.objects.all(),
          'forma':KitobForm()
          }
    return render(request,'kitoblar.html',data)

def one_kitob(request):
    data={'kitob':Kitob.objects.all()}
    return render(request,'one_kitob.html',data)


class Record_view(View):
    def post(self,request):
        if request.user.is_authenticated:
            Record.objects.create(
                talaba_fk=Talaba.objects.get(id=request.POST.get('rec_talaba')),
                kitob_fk=Kitob.objects.get(id=request.POST.get('rec_kitob')),
                admin_fk=Admin.objects.get(id=request.POST.get('rec_admin')),
                olingan_sana=request.POST.get('olingan_sana'),
                qaytarish_sana=request.POST.get('qaytarilgan_sana'),
                qaytarildi=True
            )
            return redirect('/record')
        return redirect('/')
    def get(self,request):
        if request.user.is_authenticated:
            ism=request.GET.get('record')
            if ism is None or ism=='':
                 rec=Record.objects.all()
            else:
                rec=Record.objects.filter(talaba_fk__ism__contains=ism)
            mal={'record':rec,
                 'data_talaba':Talaba.objects.all(),
                 'data_kitob':Kitob.objects.all(),
                 'data_admin':Admin.objects.all(),
                 'forma':RecordForm}
            return render(request,'record.html',mal)
        return redirect('/')

# def record(request):
#     if request.user.is_authenticated:
#         if request.method=='POST':
#             forma=RecordForm(request.POST)
#             if forma.is_valid():
#                 forma.save()
#             data={
#                 'data':Record.objects.filter(foydalanuvchi=request.user)
#             }
#             return render(request,'record.html',data)
#
#
#         ism=request.GET.get('record')
#         if ism is None or ism=='':
#              rec=Record.objects.all()
#         else:
#             rec=Record.objects.filter(talaba_fk__ism__contains=ism)
#         mal={'record':rec,
#              'data_talaba':Talaba.objects.all(),
#              'data_kitob':Kitob.objects.all(),
#              'data_admin':Admin.objects.all(),
#              'forma':RecordForm}
#         return render(request,'record.html',mal)
#     return redirect('record/')
def admin_pannel(request):
    if request.method=='POST':
        forma=AdminForm(request.POST)
        if forma.is_valid():
            Admin.objects.create(
                ism=forma.cleaned_data.get('ism'),
                ish_vaqti=forma.cleaned_data.get('ish_vaqti')
            )
        # Admin.objects.create(
        #     ism=request.POST.get('ism'),
        #     ish_vaqti=request.POST.get('ish_vaqti')
        # )
        return redirect('/admin_p')
    data={"admin":Admin.objects.all(),
          'time':Admin.objects.all(),
          'admin_forma':AdminForm}
    return render(request,'admin.html',data)



def muallif(request,num):
    data={'muallif':Muallif.objects.get(id=num)}
    return render(request,'muallif.html',data)

def mashq(request,son):
    data={'mashq':Kitob.objects.get(id=son)}
    return render(request,'mashq.html',data)
def idd(request):
    data={'idd':Kitob.objects.all()}
    return render(request,'tanlangan_kitob.html',data)

def tirik_mualliflar(request):
    f1={'tirik':Muallif.objects.all()}
    return render(request,'tirik_mualliflar.html',f1)

def badiy(request):
    return HttpResponse(Kitob.objects.filter(janr='badiy'))

def yosh(request):
    d={'yosh':Muallif.objects.order_by('-yosh')[:3]}
    return render(request,'muallif_yosh.html',d)

def kitob_soni(request):
    iy={'soni':Kitob.objects.filter(mualif_fk__kitoblar_soni__lt=10)}
    return render(request,'kitob_soni.html',iy)

def more_record(request,son):
    k={'n':Record.objects.get(id=son)}
    return render(request,'more_record.html',k)
def one_record(request):
    l={'rec':Record.objects.all()}
    return render(request,'one_record.html',l)

# O'chirish uchun funksiyalar-----------------------------

def bit_talaba(request):
    f={'ff':Talaba.objects.filter(bitiruvchi=True)}
    return render(request,'bit_talaba.html',f)

def talaba_uchir(request,son):
    Talaba.objects.get(id=son).delete()
    return redirect('/talabalar')

def muallif_uchir(request,num):
    Muallif.objects.get(id=num).delete()
    return  redirect('/all_mualliflar')
def record_delete(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/one_record')

def record_del(request,son):
    # Record.objects.get(id=son).delete()
    if request.user.is_authenticated :
        Record.objects.get(id=son).delete()
        return redirect('/record')
    return redirect('/')
def admin_del(request,son):
    Admin.objects.get(id=son).delete()
    return redirect('/admin_p')



# tahrirash uchun funksiya
def admin_edit(request,son):
    if request.method=='POST':
        Admin.objects.filter(id=son).update(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('vaqt')
        )
        return redirect('/admin_p')
    data={'admin':Admin.objects.get(id=son)}
    return render(request,'admin_edit.html',data)

def muallif_edit(request,son):
    if request.method=='POST':
        if request.POST.get('tirik')=='on':
            tirik=True
        else:
            tirik=False
        Muallif.objects.filter(id=son).update(
            tirik=tirik,
            ism=request.POST.get('ism'),
            kitoblar_soni=request.POST.get('soni'),
            jinsi=request.POST.get('jinsi'),
            yosh=request.POST.get('yosh')
            )
        return redirect('/all_mualliflar')
    mal={'data':Muallif.objects.get(id=son)}
    return render(request,'muallif_edit.html',mal)


def record_edit(request,son):
    if request.method=='POST':
        if request.POST.get('ok')=='on':
            qay=True
        else:
            qay=False
        Record.objects.filter(id=son).update(
            qaytarish_sana=request.POST.get('sana')
        )
        return redirect('/record')
    data={'data':Record.objects.get(id=son)}
    return render(request,'rec_edit.html',data)


def user_login(request):
    usernam=request.POST.get('ll')
    passwor=request.POST.get('pp')
    user=authenticate(request,username=usernam,password=passwor)
    if user is not None:
        login(request,user)
        return redirect('bosh_sahifa/')

    return render(request,'login.html')

def logaut_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    username=request.POST.get('l')
    password=request.POST.get('p')
    passwordN=request.POST.get('cp')
    ism=request.POST.get('ism')
    vaqt=request.POST.get('vaqt')
    if request.method=='POST' and passwordN==password:
        User.objects.create_user(
            username=username,
            password=passwordN
        )
        Admin.objects.create(
            ism=ism,
            ish_vaqti=vaqt
        )
        return redirect('/')
    return render(request,'register.html')

