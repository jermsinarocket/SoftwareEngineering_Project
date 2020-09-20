import googlemaps

def getDistance(origin,destination):
    gmaps = googlemaps.Client(key="AIzaSyCKYnwgeoP-2ovBzcN8veUZzDN6SrYv1t0")
    return gmaps.distance_matrix(origin,destination)
