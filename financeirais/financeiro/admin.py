from django.contrib import admin

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


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('tipo', 'data_hora', 'descricao', 'valor', 'anexo')
    list_filter = ('tipo', 'data_hora')
    actions = ['export_as_csv']