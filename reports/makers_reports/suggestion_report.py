import os
import io
from django.conf import settings

# reportlab PDF
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
cm = 2.54 


Title = "Pruebas diagnósticas oftalmológicas"
pageinfo = "Smart Data Visio 2022"
logo = "repository/staticfiles/Smart_Data_Visio.png"

def myFirstPage(canvas, doc):
 canvas.saveState()
 canvas.setLineWidth(.3)
 canvas.setTitle("Resultados pruebas visuales")
#  canvas.setFont('Helvetica-Oblique', 14)
#  canvas.drawCentredString(440, PAGE_HEIGHT-80, Title)
#  canvas.line(30,750,580,750)
#  logo = "repository/staticfiles/Smart_Data_Visio.png"
#  canvas.drawImage(os.path.join(settings.BASE_DIR, logo), 390,780, width=200, height=50)
 canvas.setFont('Times-Roman',9)
 canvas.drawString(inch, 0.75 * inch, "Pag: %d -  %s" % (doc.page, pageinfo))
 canvas.restoreState()

def myLaterPages(canvas, doc):
 canvas.saveState()
 canvas.setFont('Times-Roman',9)
 canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
 canvas.restoreState()
 
class SuggestionReportMaker():
    @staticmethod 
    def create():
        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()
        elements = []
        # Create the PDF object, using the buffer as its "file."
        pdf = SimpleDocTemplate(buffer, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
        
        im = Image(os.path.join(settings.BASE_DIR, logo), width=200 , height=50)
        elements.append(im)

        style = styles["Heading1"]
        titleReport = Paragraph(Title, style)
        elements.append(titleReport)

        style = styles["BodyText"]
        titleReport = Paragraph("<b>Informe de Resultados</b>", style)
        elements.append(titleReport)

        data=[(1,2),(3,4)]
        table = Table(data, colWidths=270, rowHeights=79)
        elements.append(table)

        # pdf.drawString(30,450,'OFFICIAL COMMUNIQUE')
        # pdf.drawString(30,435,'OF ACME INDUSTRIES')
        # pdf.drawString(500,450,"12/12/2010")
        # pdf.line(480,447,580,447)
        # pdf.drawString(275,425,'AMOUNT OWED:')
        # pdf.drawString(500,425,"$1,000.00")
        # pdf.line(378,423,580,423)
        # pdf.drawString(30,403,'RECEIVED BY:')
        # pdf.line(120,400,580,400)
        # pdf.drawString(120,403,"JOHN DOE")

        # Close the PDF object cleanly, and we're done.
        # pdf.showPage()
        # pdf.save()
        
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        pdf.build(elements, onFirstPage=myFirstPage, onLaterPages=myLaterPages  )
        buffer.seek(0)
        return buffer