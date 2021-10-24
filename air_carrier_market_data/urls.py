# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
                    Top5AirportsFrgByOrigin, \
                    Top5AirportsFrgByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistanceByOrigin, \
                    Top5AirportsDistanceByDestination, \
                    TopPassByMonth, \
                    MaxFreight, \
                    MaxPass, \
                    MaxMail, \
                    MaxDistance, \
                    PassbyCarrierbyMonthAA, \
                    PassbyCarrierbyMonthAS, \
                    PassbyCarrierbyMonthDL, \
                    PassbyCarrierbyMonthUA, \
                    PassbyCarrierbyMonthWN, \
                    LAXFlightAvg, \
                    SFOFlightAvg, \
                    DFWFlightAvg, \
                    ATLFlightAvg, \
                    ORDFlightAvg, \
                    MAIDepartAvg, \
                    MEMDepartAvg, \
                    JFKDepartAvg, \
                    ANCDepartAvg, \
                    SDFDepartAvg, \
                    FreightDistanceMax, \
                    MailDistanceMin
                         


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('top5frgorigin/', 
        Top5AirportsFrgByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ),
        name="top5frgorigin"),
    path('top5frgdestination/', 
        Top5AirportsFrgByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ),
        name="top5frgdestination"),
    path('top5mailorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailorigin"),
    path('top5maildestination/', 
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5maildestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5disorigin/', 
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distnace by Origin Airport"}
        ),
        name="top5disorigin"),
    path('top5pass/', 
        TopPassByMonth.as_view(
            extra_context={'title': "Most Passengers per Month"}
        ),
        name="top5pass"),
    path('top5disdestination/', 
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5disdestination"),
    path('MaxFreight/', 
        MaxFreight.as_view(
            extra_context={'title': "Carrier with the Max Freight"}
        ),
        name="MaxFreight"),
    path('MaxPass/', 
        MaxPass.as_view(
            extra_context={'title': "Carrier with the Max Passengers"}
        ),
        name="MaxPass"),
    path('MaxMail/', 
        MaxMail.as_view(
            extra_context={'title': "Carrier with the Max Mail"}
        ),
        name="MaxMail"),
    path('MaxDistance/', 
        MaxDistance.as_view(
            extra_context={'title': "Carrier with the Max Mail"}
        ),
        name="MaxDistance"),
    path('PassbyCarrierbyMonthAA/', 
        PassbyCarrierbyMonthAA.as_view(
            extra_context={'title': "Passengers Per Carrier By Month"}
        ),
        name="PassbyCarrierbyMonthAA"),
   path('PassbyCarrierbyMonthAS/', 
        PassbyCarrierbyMonthAS.as_view(
            extra_context={'title': "Passengers Per Carrier By Month"}
        ),
        name="PassbyCarrierbyMonthAS"),
   path('PassbyCarrierbyMonthDL/', 
        PassbyCarrierbyMonthDL.as_view(
            extra_context={'title': "Passengers Per Carrier By Month"}
        ),
        name="PassbyCarrierbyMonthDL"),
   path('PassbyCarrierbyMonthUA/', 
        PassbyCarrierbyMonthUA.as_view(
            extra_context={'title': "Passengers Per Carrier By Month"}
        ),
        name="PassbyCarrierbyMonthUA"),
   path('PassbyCarrierbyMonthWN/', 
        PassbyCarrierbyMonthWN.as_view(
            extra_context={'title': "Passengers Per Carrier By Month"}
        ),
        name="PassbyCarrierbyMonthWN"),
    path('LAXFlightAvg/', 
        LAXFlightAvg.as_view(
            extra_context={'title': "Average Passengers By Month"}
        ),
        name="LAXFlightAvg"),
    path('SFOFlightAvg/', 
        SFOFlightAvg.as_view(
            extra_context={'title': "Average Passengers By Month"}
        ),
        name="SFOFlightAvg"),
    path('DFWFlightAvg/', 
        DFWFlightAvg.as_view(
            extra_context={'title': "Average Passengers By Month"}
        ),
        name="DFWFlightAvg"),
    path('ATLFlightAvg/', 
        ATLFlightAvg.as_view(
            extra_context={'title': "Average Passengers By Month"}
        ),
        name="ATLFlightAvg"),
    path('ORDFlightAvg/', 
        ORDFlightAvg.as_view(
            extra_context={'title': "Average Passengers By Month"}
        ),
        name="ORDFlightAvg"),
    path('MAIDepartAvg/', 
        MAIDepartAvg.as_view(
            extra_context={'title': "Average Freight By Month"}
        ),
        name="MAIDepartAvg"),
    path('JFKDepartAvg/', 
        JFKDepartAvg.as_view(
            extra_context={'title': "Average Freight By Month"}
        ),
        name="JFKDepartAvg"),
    path('MEMDepartAvg/', 
        MEMDepartAvg.as_view(
            extra_context={'title': "Average Freight By Month"}
        ),
        name="MEMDepartAvg"), 
    path('ANCDepartAvg/', 
        ANCDepartAvg.as_view(
            extra_context={'title': "Average Freight By Month"}
        ),
        name="ANCDepartAvg"),
    path('SDFDepartAvg/', 
        SDFDepartAvg.as_view(
            extra_context={'title': "Average Freight By Month"}
        ),
        name="SDFDepartAvg"),
    path('FreightDisMax/', 
        FreightDistanceMax.as_view(
            extra_context={'title': "Paired Cities with Max Freight and Distnace"}
        ),
        name="FreightDisMax"),
    path('MailDisMin/', 
        MailDistanceMin.as_view(
            extra_context={'title': "Paired Cities with Max Freight and Distnace"}
        ),
        name="MailDisMin"),
]






