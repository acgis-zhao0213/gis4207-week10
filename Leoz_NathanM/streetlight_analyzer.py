import arcpy
import sys

# def main():
ws = r'..\..\..\..\data\Ottawa'
arcpy.env.workspace = ws
streetlight_fc= 'Street_Lights\Street_Lights.shp'
roads_cl_fc='Road_Centrelines\Road_Centrelines.shp'
road_name_field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME')

def _get_unique_values(field_name):
      with arcpy.da.SearchCursor(streetlight_fc,'STREET_NAM') as cursor:
        field_list = []
        for row in cursor:
            field_list += row
        if field_name not in field_list:
            print('Road name is invalid')
            break
        else:
            print('Road name is valid')
            continue

def get_streetlight_count(road_name, distance):
	_get_unique_values(road_name)
    road_segments = arcpy.management.SelectLayerByAttribute(roads_cl_fc, "NEW_SELECTION", f"{road_name_field} = '{road_name}'")
  
    near_streetlights,in_lyr,count = arcpy.management.SelectLayerByLocation(streetlight_fc, "WITHIN_A_DISTANCE", road_segments, distance)

    return count


print(get_streetlight_count('BRADLEY',0.0002))
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