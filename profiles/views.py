# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from datetime import datetime
from .models import IdCard

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.lib.units import mm


#from topics.models import Topic, ActivityRoom#, RoomTopic
#from rooms.models import Room
from activities.models import Activities,signUpActivities
#from agenda.models import TopicAgenda, SignUpSchedule

from reportlab.lib.utils import ImageReader

class DownloadIdCardPdfView(TemplateView):

    template_name = 'home/index.html'
    form_class = ""

    def get(self, request, *args, **kwargs):

        user = request.user

        id_card_code = request.GET['id_card_code']

        obj_id_card = IdCard.objects.filter(id_card_code = id_card_code,active = True)[0]
        sign_up_activity_code = obj_id_card.fk_sign_activity_code

        obj_id_card.is_downloaded = True
        obj_id_card.modified_at = datetime.today()
        obj_id_card.fk_user_modified = user
        obj_id_card.save(update_fields = ['is_downloaded','modified_at','fk_user_modified'])

        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="id_card.pdf"'

        # Create the PDF object, using the response object as its "file."
        canvas = Canvas(response)
        canvas.setPageSize((300, 450))

        image = ImageReader('https://fbcdn-photos-d-a.akamaihd.net/hphotos-ak-xpa1/v/t1.0-0/p206x206/13419028_989746344471689_3801540286586582921_n.jpg?oh=6cda5970c618fea4bf5d8c3beaf512eb&oe=581D6111&__gda__=1479503095_802d073eeb57c1edb6125384a435df97')
        canvas.drawImage(image,0,0,300,450)

        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleH = styles['Heading1']

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.

        canvas.setFont('Helvetica', 12)

        #p = Paragraph("II congreso internacional de la red de ongs asoprovida,cambio climatico,soberania y educacion", style=styleH)
        #p.wrapOn(canvas, 280, 150)
        #p.drawOn(canvas, 10,380)
        #canvas.drawCentredString(10,400,'')

        canvas.drawString(10,300,'NOMBRES:')
        canvas.drawString(80,300,user.get_full_name())


        barcode=code128.Code128("c891ea68-17c5-42d3-a238-815a1aefd701",barWidth=0.2*mm,barHeight=15*mm,humanReadable = False)
        barcode.drawOn(canvas,10,200)

        canvas.setLineWidth(30)
        canvas.setStrokeColor(colors.green)
        canvas.line(0,10,400,10)

        # Close the PDF object cleanly, and we're done.
        canvas.showPage()
        canvas.save()
        return response

class SearchIdCardPdfView(TemplateView):

    template_name = "home/index.html"
    form_class = ""

    def get(self, request, *args, **kwargs):

        try:

            response_data = {}
            message = ""
            is_error = False
            is_downloaded = False
            id_card_code = ""
            is_authenticated = False
            is_sign_up = False

            user = request.user

            if user.is_authenticated():

                is_authenticated = True
                obj_sign_up_activity = signUpActivities.objects.filter(fk_user = user, active = True)
                if obj_sign_up_activity:
                    is_sign_up = True
                    sign_up_activity_code = obj_sign_up_activity[0].sign_up_code

                    obj_id_card = IdCard.objects.filter(active = True,fk_sign_activity_code =sign_up_activity_code)
                    id_card_code = obj_id_card[0].id_card_code
                    is_downloaded = obj_id_card[0].is_downloaded

                    if(is_downloaded):

                        message = "usted ya descargo la tarjeta de identificacion para esta actividad"

                    else:

                        message = "puede descargar la escarapela"
                else:

                    message = "inscribase en la base de datos del congreso para generar una escarapela"
            else:
                message = "por favor inicie sesion para imprimir la escarapela"

        except Exception as e:

            is_error = True
            message = "error en el sistema por favor comuniquese con soporte"
            response_data['type_error'] = type(e).__name__

        response_data['message'] = message
        response_data['is_error'] = is_error
        response_data['is_downloaded'] = is_downloaded
        response_data['id_card_code'] = id_card_code
        response_data['is_authenticated'] = is_authenticated
        response_data['is_sign_up'] = is_sign_up

        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)
