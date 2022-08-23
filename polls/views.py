
from multiprocessing import context
from rest_framework.response import Response
from polls.models import *
from rest_framework.views import *
from rest_framework.decorators import *
from rest_framework.response import *
from datetime import datetime
from polls.serializers import  *
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        
        serializer = UserSerializerWithToken(self.user).data
        print(serializer)
        for k, v in serializer.items():
            data[k] = v
        data["detail"]="ok"
        print(data)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer     




@api_view(['POST'])
def make_invite(request):
    print(request.data)
    serializer=inviteMarried_requestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response ({"success":"True"})
    else:
          return Response(   { "success":"fail", "error":serializer.errors } )
    # invite_id = request.data['invite_id']
    # invite_image = inviteMarried_request.objects.get(id=invite_id)
    # invite_image.image =request.FILES.get('image')
    # invite_image.save()
    # return Response('Image was uploaded')

# @api_view(['POST'])
# def invite_request(request): 
#     data=request.data
#     maleName=data["maleName"]
#     femaleName=data["femaleName"]
#     location=data["location"]
#     clock= data["clock"]
#     date=data["date"]

#     requests=inviteMarried_request.objects.filter(maleName=maleName,femaleName=femaleName)
#     if requests.exists():
#         return Response({'result':'تم انشاء الدعوة مسبقا '})
#     else:
#         p=inviteMarried_request(maleName=maleName,femaleName=femaleName,location=location,clock=clock,date=date)
#         p.save()
#         return Response({'result':'تم انشاء الدعوة بنجاح'})
@api_view(['POST'])
def details(request): 
    data=request.data
    iid=data["iid"]
    p=inviteMarried_request.objects.get(id=iid)
    serializer=inviteMarried_requestSerializer(p)
    return Response(serializer.data)
@api_view(['GET'])
def my_invites(request):  
    try:
        invites=inviteMarried_request.objects.filter(date__gte=datetime.today()).order_by('-date')
        serializer = inviteMarried_requestSerializer(invites, many=True)
        a=[]
        for i in range(len(invites)):
            a.append({"result":serializer.data[i]})
        return JsonResponse(a,safe=False)    
    except:
        return Response({'result':'ليس هناك اي دعوات'})


        