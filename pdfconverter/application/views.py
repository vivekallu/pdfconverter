from django.shortcuts import render
from django.http import HttpResponse
import pdfkit
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from form import UploadFileForm
import pdfcrowd

#import os,sys
#sys.path.append(os.path.abspath('..'))
import app_config 

# Create your views here.
def pdf_converter(request):
    ''' This view generates pdf from the uploaded html file or the url entered and returns the pdf as HttpResponse''' 
    if request.method == 'POST':
        filename = ''
        pdf_file_location = app_config.pdf_file_location
        html_file_location = app_config.html_file_location
        if request.FILES:
            print request.FILES
            data = request.FILES['html_file']
            print data.name
            html_file_location = app_config.html_file_location
            pdf_file_location = app_config.pdf_file_location
            if default_storage.exists(html_file_location+str(data.name)):
                default_storage.delete(html_file_location+str(data.name))
            default_storage.save(html_file_location+str(data.name), ContentFile(data.read()))
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            filename = pdf_file_location+str(data.name).replace("html","pdf")
            pdfkit.from_file(html_file_location+str(data.name), filename)
        else:
            urlname = request.POST.get('url')
            post_data = UploadFileForm(request.POST)
            valid = post_data.is_valid()
            if not valid:
                err = post_data.errors
                return render(request,'upload_file.html')
           
            config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
            filename = pdf_file_location+'url.pdf'
            try:
                pdfkit.from_url(str(urlname),filename)
            except:
                return render(request,'upload_file.html',{'error':1})
        
        fsock = open(filename, 'r')
        response = HttpResponse(fsock, content_type='application/pdf')

        return response

    return render(request,'upload_file.html')





