import arcpy
import sys

ws = r'..\..\..\..\data\Ottawa'
arcpy.env.workspace = ws
streetlight_fc= 'Street_Lights\Street_Lights.shp'
roads_cl_fc='Road_Centrelines\Road_Centrelines.shp'
road_name_field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME')

def _get_unique_values(field_name):

# field=['STREET_NAM']       
    with arcpy.da.SearchCursor(streetlight_fc,'STREET_NAM') as cursor:
        field_list = []
        for row in cursor:
            field_list += row

        # return field_list
   
        if field_name not in field_list:
            return print('Road name is invalid')
        else:
            return print('Road name is valid')

# test=_get_unique_values('STRM')

def get_streetlight_count(road_name, distance):
    # dist = arcpy.AddFieldDelimiters(ws, 'ROAD_NAME')
    # wc = f"{dist}" 
    

    road_name_selection = arcpy.management.SelectLayerByAttribute(roads_cl_fc, "ROAD_NAME_ LIKE f'{road_name}'" )
    count = arcpy.management.SelectLayerByLocation(road_name_selection, "WITHIN_A_DISTANCE", roads_cl_fc, distance, "NEW_SELECTION", "NOT_INVERT")
    
    return count
dist= 0.0002
num= get_streetlight_count( 'CARLING AVE',dist)
