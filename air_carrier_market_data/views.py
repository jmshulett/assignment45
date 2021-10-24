import pdb
from django.db.models.aggregates import Avg, Min
from django.views.generic import ListView
from django.db.models import Max, Sum

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

#freight queries
# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFrgByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="rankorder_list_freight_origin.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrgByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_freight=Sum('freight')) \
                                 .order_by('-total_freight')[0:5]
    template_name="rankorder_list_freight_destination.html"

#mail queries
# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_origin.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_destination.html"

#What are the top 5 airports in terms of:
#Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dis=Sum('distance')) \
                        .order_by('-total_dis')[0:5]
    template_name="rankorder_list_distance_origin.html"

#Total distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dis=Sum('distance')) \
                                 .order_by('-total_dis')[0:5]
    template_name="rankorder_list_distance_destination.html"

#Which airport reported the most passengers by month?
class TopPassByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pass_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_pass=Max('passengers')) \
                .order_by('-total_pass')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Max Which airline reported the most freight carried?
class MaxFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name','carrier_id') \
                                 .annotate(max_freight=Max('freight')) \
                                 .order_by('-max_freight')[0:1]
    template_name="maxfreight.html"

#Which airline reported the most passengers carried?
class MaxPass(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name','carrier_id') \
                                 .annotate(max_pass=Max('passengers')) \
                                 .order_by('-max_pass')[0:1]
    template_name="maxpass.html"

#Which airline reported the most mail carried?
class MaxMail(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name','carrier_id') \
                                 .annotate(max_mail=Max('mail')) \
                                 .order_by('-max_mail')[0:1]
    template_name="maxmail.html"

#Which airline reported the longest flight distance?
class MaxDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name','carrier_id') \
                                 .annotate(max_distance=Max('distance')) \
                                 .order_by('-max_distance')[0:1]
    template_name="maxdistance.html"

#Rank order passengers carried, by month, for these airlines:
#AA (American Airlines)
#AS (Alaska Airlines)
#DL (Delta Airlines)
#UA (United Airlines)
#WN (Southwest Airlines)

class PassbyCarrierbyMonthAA(ListView):
    context_object_name = "airport_list"
    template_name="PassCarrierMonthAA.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'carrier_id',
                        'passengers',
                        'month') \
                .filter(month__exact=month, carrier_id='AA') \
                .annotate(total_passaa=Max('passengers')) \
                .order_by('-total_passaa')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class PassbyCarrierbyMonthAS(ListView):
    context_object_name = "airport_list"
    template_name="PassCarrierMonthAS.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'carrier_id',
                        'passengers',
                        'month') \
                .filter(month__exact=month, carrier_id='AS') \
                .annotate(total_passas=Max('passengers')) \
                .order_by('-total_passas')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class PassbyCarrierbyMonthDL(ListView):
    context_object_name = "airport_list"
    template_name="PassCarrierMonthDL.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'carrier_id',
                        'passengers',
                        'month') \
                .filter(month__exact=month, carrier_id='DL') \
                .annotate(total_passdl=Max('passengers')) \
                .order_by('-total_passdl')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class PassbyCarrierbyMonthUA(ListView):
    context_object_name = "airport_list"
    template_name="PassCarrierMonthUA.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'carrier_id',
                        'passengers',
                        'month') \
                .filter(month__exact=month, carrier_id='UA') \
                .annotate(total_passua=Max('passengers')) \
                .order_by('-total_passua')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list                 

class PassbyCarrierbyMonthWN(ListView):
    context_object_name = "airport_list"
    template_name="PassCarrierMonthSA.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'carrier_id',
                        'passengers',
                        'month') \
                .filter(month__exact=month, carrier_id='WN') \
                .annotate(total_passsa=Max('passengers')) \
                .order_by('-total_passsa')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list  

class LAXFlightAvg(ListView):
    context_object_name = "airport_list"
    template_name="LAXFlightAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, dest_iata_code='LAX') \
                .annotate(avg_passla=Avg('passengers')) \
                .order_by('-avg_passla')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list  


class SFOFlightAvg(ListView):
    context_object_name = "airport_list"
    template_name="SFOFlightAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, dest_iata_code='SFO') \
                .annotate(avg_passsfo=Avg('passengers')) \
                .order_by('-avg_passsfo')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list  

class DFWFlightAvg(ListView):
    context_object_name = "airport_list"
    template_name="DFWFlightAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, dest_iata_code='DFW') \
                .annotate(avg_passdfw=Avg('passengers')) \
                .order_by('-avg_passdfw')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list  

class ATLFlightAvg(ListView):
    context_object_name = "airport_list"
    template_name="ATLFlightAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, dest_iata_code='ATL') \
                .annotate(avg_passatl=Avg('passengers')) \
                .order_by('-avg_passatl')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list  

class ORDFlightAvg(ListView):
    context_object_name = "airport_list"
    template_name="ORDFlightAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, dest_iata_code='ORD') \
                .annotate(avg_passord=Avg('passengers')) \
                .order_by('-avg_passord')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class MAIDepartAvg(ListView):
    context_object_name = "airport_list"
    template_name="MIADepartAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'passengers',
                        'month') \
                .filter(month__exact=month, orig_iata_code='MIA') \
                .annotate(aavg_frgdeptmia=Avg('passengers')) \
                .order_by('-aavg_frgdeptmia')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class MEMDepartAvg(ListView):
    context_object_name = "airport_list"
    template_name="MEMDepartAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'freight',
                        'month') \
                .filter(month__exact=month, orig_iata_code='MEM') \
                .annotate(avg_frgdeptmem=Avg('freight')) \
                .order_by('-avg_frgdeptmem')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class JFKDepartAvg(ListView):
    context_object_name = "airport_list"
    template_name="JFKDepartAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'freight',
                        'month') \
                .filter(month__exact=month, orig_iata_code='JFK') \
                .annotate(avg_frgdeptjfk=Avg('freight')) \
                .order_by('-avg_frgdeptjfk')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class ANCDepartAvg(ListView):
    context_object_name = "airport_list"
    template_name="ANCDepartAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'freight',
                        'month') \
                .filter(month__exact=month, orig_iata_code='ANC') \
                .annotate(avg_frgdeptanc=Avg('freight')) \
                .order_by('-avg_frgdeptanc')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class SDFDepartAvg(ListView):
    context_object_name = "airport_list"
    template_name="SDFDepartAvg.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'freight',
                        'month') \
                .filter(month__exact=month, orig_iata_code='SDF') \
                .annotate(avg_frgdeptsdf=Avg('freight')) \
                .order_by('-avg_frgdeptsdf')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

class FreightDistanceMax(ListView):
    context_object_name = "airport_list"
    template_name="FreightDistanceMax.html"
    queryset = MarketData.objects.values('orig_city_name', 'dest_city_name') \
                .annotate(max_freight=Max('freight'), max_distance=Max('distance')) \
                .order_by('-max_freight')[0:1]
            

class MailDistanceMin(ListView):
    context_object_name = "airport_list"
    template_name="MailDistanceMin.html"
    queryset = MarketData.objects.values('orig_city_name', 'dest_city_name') \
                .annotate(min_mail=Max('mail'), min_distance=Max('distance')) \
                .order_by('-min_mail')[0:1]

