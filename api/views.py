from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import User , ActivityPeriod

DATE_FORMAT = '%b %d %Y %I:%M%p'

def GetJson(request):
    response_dict=dict()
    Members = User.objects.all()

    if(Members):
        response_dict['ok']='true'

        for user in Members:
            if('members' not in response_dict):
                response_dict['members']=list()

            response_dict['members'].append({
            	'id':user.user_id ,
                'real_name':user.real_name ,
                'tz':str(user.tz),
                'activity_periods':[
                    { 
                    'start_time': datetime.strftime(period.start_time ,DATE_FORMAT),
                    'end_time' : datetime.strftime(period.end_time,DATE_FORMAT) 
                    } for period in ActivityPeriod.objects.filter(User=user) ]
                    })

    else:
        response_dict['ok']='false'

    return JsonResponse(response_dict,json_dumps_params={'indent': 4},safe=False)