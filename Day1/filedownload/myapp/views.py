from django.shortcuts import render
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.
class FileDownload(APIView):
    def get(self,request):
        # get file name from url
        filename = request.GET.get("filename",None)
        
        if filename:
            # get the file path
            filepath = default_storage.location + f"/media/files/{filename}"
            
            try:
                with open(filepath,"rb") as f:
                    # get the response
                    response = HttpResponse(f.read())
                    
                    # set the appropriate header
                    response["Content-Type"] = "application/octet-stream"
                    response["Content-Disposition"] = f"attachments; filename:{filename}"
                    return response
            except:
                return Response({"Error" : "File not found."}, status=400)
        else:
            return Response({"Error" : "File name not provided."}, status=400)