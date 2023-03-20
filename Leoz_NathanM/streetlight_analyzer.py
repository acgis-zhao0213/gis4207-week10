import arcpy
import sys

# def main():
ws = r'..\..\..\..\data\Ottawa'
arcpy.env.workspace = ws
streetlight_fc= 'Street_Lights\Street_Lights.shp'
roads_cl_fc='Road_Centrelines\Road_Centrelines.shp'
road_name_field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME')

def _get_unique_values(fc, field_name):
      unique_values = set()
      with arcpy.da.SearchCursor(fc,[field_name]) as cursor:
        for row in cursor: 
           unique_values.add(row[0])
        return unique_values 

def get_streetlight_count(road_name, distance):
    
    streetlight = "Street_Lights"

    unique_roads = _get_unique_values("Road_Centrelines", "ROAD_NAME")

    if road_name in unique_roads: 
        arcpy.management.SelectLayerByLocation("Road_Centrelines", "NEW_SELECTION", "ROADNAME = '{}'".format(road_name), None) 
        arcpy.management.SaveToLayerFile('Road_Centrelines', road_name) 


        Selection_Layer = arcpy.management.SelectLayerByLocation(streetlight, 'WITHIN_A_DISTANCE', road_name + '.lryx', distance, "NEW_SELECTION", "NOT_INVERT")
        return arcpy.management.GetCount(Selection_Layer)[0]
    else: 
        print('Road Invalid')
        print (unique_roads)
        pass 

Road = "CRAMER" 
road_distance = "0.002 DecimalDegrees"

get_streetlight_count(Road, road_distance)




def save_streetlights(road_name, distance, out_fc):
    road_segments = arcpy.management.SelectLayerByAttribute(roads_cl_fc, "NEW_SELECTION", f"{road_name_field} = '{road_name}'")
  
    near_streetlights,in_lyr,count = arcpy.management.SelectLayerByLocation(streetlight_fc, "WITHIN_A_DISTANCE", road_segments, distance)
   
    arcpy.management.CopyFeatures(near_streetlights, out_fc)

def show_road_names(pattern=None):
    if pattern:
        pattern_upper = pattern.upper()
        query = f"{road_name_field} LIKE '%{pattern_upper}%'"
        road_names = _get_unique_values(roads_cl_fc, road_name_field)
        road_names = [road_name for road_name in road_names if road_name.upper().find(pattern_upper) >= 0]
    else:
        query = None
        road_names = _get_unique_values(roads_cl_fc, road_name_field)
    print("\n".join(sorted(road_names)))

# if __name__ == "__main__":
#     main()
