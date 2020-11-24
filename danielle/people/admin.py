from django.contrib import admin
from people.models import Person

admin.site.site_header = "Gestão de pessoas"
admin.site.site_title = "Gestão fácil!"
admin.site.index_title = "Bem vindo! "


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_date')
    list_filter = ['gender', 'state']
    search_fields = ['name']
    fieldsets = [('Identificação', {
        'fields': [
            'name', 'mother_name', 'born_date', 'cpf', ('rg', 'rg_ssp'),
            'gender'
        ]
    }),
                 ('Endereço', {
                     'fields': [
                         'address_line_1', 'address_line_2', 'neighbourhood',
                         'state', 'city', 'postal_code', 'residence_type'
                     ]
                 }),
                 ('Contato', {
                     'fields': ['email', 'private_phone', 'message_phone']
                 }),
                 ('Outras informações', {
                     'fields': ['observation', 'death_date'],
                     'classes': ('collapse', ),
                 })]


admin.site.register(Person, PersonAdmin)
