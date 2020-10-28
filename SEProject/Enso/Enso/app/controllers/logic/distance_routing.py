import bisect
import googlemaps
from django.forms.models import model_to_dict
from Enso.app.controllers.logic.geocoder import getDistance
from django.db.models.query_utils import Q
from Enso.app.controllers.logic.store_management import averageRatingCalculator

def route(stores_qdict,user_latitude,user_longitude):
    origin = [{"lat": user_latitude, "lng": user_longitude}]

    distance_list = []
    store_list = []
    count = 0
    for store in stores_qdict:
        store_lat = store.hawker_centre.zip_code.latitude
        store_long = store.hawker_centre.zip_code.longitude

        destination = [{"lat": store_lat, "lng": store_long}]
        distance_matrix =  getDistance(origin,destination)
        dist_dura = distance_matrix['rows'][0]['elements'][0]
        distance_text = dist_dura['distance']['text']
        distance_value = dist_dura['distance']['value']
        duration_text = dist_dura['duration']['text']

        store_dict = model_to_dict(store)
        store_dict['distance'] = distance_text
        store_dict['duration'] = duration_text
        store_dict['hawker_centre'] = store.hawker_centre.centre_name
        store_dict['address'] = store.hawker_centre.zip_code.getFormattedAddress()
        store_dict['zipcode'] = store.hawker_centre.zip_code.zipcode
        store_dict['store_image'] = store.get_storepic_url()
        store_dict['cuisine_type'] = store.cuisine_type.category_name
        store_dict['num_reviews'],store_dict['store_rating'] =  averageRatingCalculator(store.id)


        index_inserted = bisect.bisect(distance_list, distance_value)
        bisect.insort(distance_list,distance_value)

        store_list.insert(index_inserted,store_dict)

        count+=1
        if count==5:
            break

    return store_list
