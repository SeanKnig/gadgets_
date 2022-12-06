async def is_in_polygon(polygon_coordinates_json, polygon_check):
        poly_file = open(polygon_coordinates_json).read()
        nd_polygon = json.loads(poly_file)

        nd_polygon_df = geopandas.GeoDataFrame.from_features(nd_polygon['features'])
        poly = nd_polygon_df['geometry'][0]
        p1 = Point(polygon_check.lon, polygon_check.lat)
        #print(poly.area)
        #print(poly.contains(p1))
        return poly.contains(p1)
