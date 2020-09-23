from django.contrib import admin
from django.utils.html import format_html

from .models import Movimentacao


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Exportar CSV'



class MovimentacaoAdmin(admin.ModelAdmin, ExportCsvMixin):

    def img_tag(self, obj):
        return format_html('<img src="{}" >'.format(obj.url))
    img_tag.short_description = 'Imagem Comprovante'
    list_display = ['tipo', 'data_hora', 'descricao', 'valor', 'img_tag', 'anexo']
    list_filter = ['tipo', 'data_hora']
    actions = ['export_as_csv']
admin.site.register(Movimentacao, MovimentacaoAdmin)