### PlantDoc

Deployed [here](https://plant-doc-plantcv.herokuapp.com/) on Heroku

Endpoints:

* Analyze (GET):
    * Path Args: url (required - URL of the image to be analyzed)

-----------------------------------------------------------------------

#### Steps to run locally:
* Clone repository
```bash
git clone https://github.com/gary1998/plant_doc.git plant_doc_plantcv
```

* Move to directory
```bash
cd plant_doc_plantcv
```

* Install all dependencies
```bash
pip install .
```

* Run Flask Server
```bash
python plant_doc/server.py
```