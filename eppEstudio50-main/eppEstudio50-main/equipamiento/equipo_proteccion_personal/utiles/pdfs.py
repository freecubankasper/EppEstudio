import base64
# import pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template


def export_pdf_from_html(request, name, html, options, data, filepath=None):
    html_template = get_template(html)
    rendered_html = html_template.render(data, request)
    if filepath is not None:
        full_path = filepath + '/' + name + '.pdf'
        # pdfkit.from_string(rendered_html, output_path=full_path, configuration=settings.PDF_CONFIG, options=options)
        return
    # else:
    #     # pdf_file = pdfkit.from_string(rendered_html, False, configuration=settings.PDF_CONFIG, options=options)
    #     # http_response = HttpResponse(pdf_file, content_type='application/pdf')
    #     http_response['Content-Disposition'] = 'attachment;filename="%s.pdf"' % name
    #     return http_response


def to_base64(path):
    with open(path, 'rb') as image:
        return base64.b64encode(image.read()).decode('utf-8')