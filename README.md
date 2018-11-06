# postcode-to-point

This repository contains a demo notebook and files that can be used to create a network graph and find postcodes that are within x meteres from the target point. 

You will need the following Python libraries installed, plus their dependencies:

```
geopandas=0.3.0+
shapely=1.6.4+
networkx=2.2+
folium=0.6.0+
matplotlib=3.0.0+
```

Some of these, like Folium and Networkx can be installed using `pip`, while others might be easier to install using `conda`. GeoPandas in particular can be tricky especially if you're mixing channels (conda-forge and conda).

The notebook has a script called `get_data.py` that will download all the data you need: the road network from Open Street Map and the postcode boundaries shapefile from the National Records of Scotland. 

If  you prefer to download them yourself, here are the links: [OSM](https://download.geofabrik.de/europe/great-britain/scotland.html) and [Postcodes](https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products/scottish-postcode-directory/2018-2). 

#### An example of a shortest path visualised on a Folium map:

![Example 1](Shortest%20Path%20Visualised%20on%20Map.png)
