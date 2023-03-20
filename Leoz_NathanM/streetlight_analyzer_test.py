import streetlight_analyzer as sa
import arcpy
import sys

ws = r'..\..\..\..\data\Ottawa'
arcpy.env.workspace = ws
streetlight_fc= 'Street_Lights\Street_Lights.shp'
roads_cl_fc='Road_Centrelines\Road_Centrelines.shp'
road_name_field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME')
def test_get_streetlight_count():
    expect=19
    act=sa.get_streetlight_count('BRADLEY',0.0002 )
    assert expect == act

test_get_streetlight_count()

