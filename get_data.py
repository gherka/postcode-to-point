import os
import urllib.request
import zipfile

here = os.path.dirname(__file__)

data_dir = os.path.abspath(os.path.join(here, 'data'))
if not os.path.exists(data_dir):
    raise OSError('data/ directory not found, aborting data preparation.')


def postcodes():
    pc_dir = os.path.join(data_dir, 'postcodes')
    pc_raw = os.path.join(data_dir, 'spd-unit-boundaries-cut-18-2.zip')

    if not os.path.exists(pc_raw):
        print("- Downloading Scottish Postcode Shapefiles... ", end='', flush=True)
        url = "https://www.nrscotland.gov.uk/files//geography/2018-2/spd-unit-boundaries-cut-18-2.zip"
        urllib.request.urlretrieve(url, pc_raw)
        print("done", flush=True)

    if not os.path.exists(pc_dir):
        print("- Extracting Postcode data... ", end='', flush=True)
        with zipfile.ZipFile(pc_raw, 'r') as pc:
            pc.extractall('data/postcodes/')
        print("done", flush=True)

    print("** Finished! **")
    
    
def roads_osm():
    roads_dir = os.path.join(data_dir, 'roads')
    roads_raw = os.path.join(data_dir, 'scotland-latest-free.shp.zip')

    if not os.path.exists(roads_raw):
        print("- Downloading OSM Road network Shapefiles... ", end='', flush=True)
        url = "https://download.geofabrik.de/europe/great-britain/scotland-latest-free.shp.zip"
        urllib.request.urlretrieve(url, roads_raw)
        print("done", flush=True)

    if not os.path.exists(roads_dir):
        
        sh = [
            'gis_osm_roads_free_1.cpg',
            'gis_osm_roads_free_1.dbf',
            'gis_osm_roads_free_1.prj',
            'gis_osm_roads_free_1.shp',
            'gis_osm_roads_free_1.shx']
        
        print("- Extracting Road network data... ", end='', flush=True)

        with zipfile.ZipFile(roads_raw, 'r') as rd:
            
            for file in sh:
                rd.extract(file, 'data/roads/')
        
        print("done", flush=True)

    print("** Finished! **")


if __name__ == '__main__':
    postcodes()
    roads_osm()
