import streetlight_analyzer as sa
import arcpy
import sys,os

ws = r'..\..\..\..\data\Ottawa'
arcpy.env.workspace = ws
streetlight_fc= 'Street_Lights\Street_Lights.shp'
roads_cl_fc='Road_Centrelines\Road_Centrelines.shp'
road_name_field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME_')
def test_get_unique_values():
    test_name = 'BRADLEY'
    uniques = sa._get_unique_values(roads_cl_fc, "ROAD_NAME")
    assert test_name in uniques

def test_get_streetlight_count():
    expect=19
    act=int(sa.get_streetlight_count('BRADLEY',0.0002 ))
    assert expect == act

def test_save_streetlights():
    test_output = 'test.shp'
    sa.save_streetlights('BRADLEY',0.0002, 'test')
    filelist = []
    for root,dirs,files in os.walk(ws):
        for f in files:
            if f.find('.shp')>=0:
                filelist.append(f)
    assert test_output in filelist

def test_show_road_names():
    names = sa.show_road_names(pattern=None)
    test_output = 'ZOKOL'
    print('names type',type(names))
    assert test_output in names
