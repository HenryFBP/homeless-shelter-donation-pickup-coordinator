
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Other pages](#other-pages)
- [For those who dislike reading or have little time](#for-those-who-dislike-reading-or-have-little-time)
- [For donaters](#for-donaters)
- [For shelters](#for-shelters)
- [For developers](#for-developers)

<!-- /TOC -->

App built from `release` branch is available here:
https://shelter-pickup-coordinator.herokuapp.com/

This application will (once developed) help to coordinate picking up
to-be-donated goods from people who wish to donate them.

It will achieve this by letting donaters and shelters essentially cooperate with
each other over this platform.

# Other pages
- [Sketches](_sketches)
- [Reflection about this app](_notes/reflection.md)
- [Notes on shelters](_notes)

# For those who dislike reading or have little time
- Working on an application for a comms course at IIT
- Will coordinate picking up donated goods from civilians:
  - Lets donaters publish their location and what they will donate publicly to various organizations
  - When pickup vehicle is collecting, their route (can be) visible to those who want to donate
  - Lets orgs plan routes based off of available donations
  - Donaters can see what organizations need which items

# For donaters
- List what items they wish to donate
- Publish their location to homeless shelters as to optimize the collection
  routes of pickup vehicles
- See **which shelters**; **where**; need **what** items 
- Get notified of pickup routes
  - If a route does not intersect with you, is there another dropoff point
  nearby?
  
# For shelters
- Publicly display needed items
- See all people who have things to donate
- Plan routes based off of customizable criteria:
  - Distance
  - Needed items
  - Statistics! (possibly)
    - Best geo-locations for most items?
      - Of a specfic class?
    - See item-yield of routes as statistics
    - Heatmap of item density?
  - By item group
    - Clothing
      - Winter clothes
      - Summer clothes
    - Food
      - Canned food
      - Produce

# For developers
To develop or contribute for this project, you will need the following:
- Python >= 3.6
  - See `requirements.txt` for details
  - `pip install -r requirements.txt`
- PostGreSQL
- [Geospatial libraries](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/geolibs/)
  - PostGIS
  - GEOS
  - GDAL
  - PROJ.4

Because of the way Django handles database ORM, you will need to run these commands to migrate the objects into SQL schemas:
- `py manage.py makemigrations`
- `py manage.py migrate`

To run, simply type `py manage.py runserver`
