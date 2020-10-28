import googlemaps

def getDistance(origin,destination):
    gmaps = googlemaps.Client(key="AIzaSyDDCVt_rTIk3xHjMY5OTtKb7TvEzPqOD4U")
    return gmaps.distance_matrix(origin,destination)
