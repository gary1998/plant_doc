### PlantDoc

Deployed [here](https://plant-doc-plantcv.herokuapp.com/) on Heroku

Endpoints:

* [/analyze](https://plant-doc-plantcv.herokuapp.com/analyze) (GET):
    * Path Arguments:
        * url - required - URL of the image to be analyzed
        * size - optional - Size, image to be resized in (default = 240)
        * mask_gray_low - optional - Lowest gray value to be allowed in mask (default = 95)
        * mask_gray_high - optional - Highest gray value to be allowed in mask (default = 255)
        * health_point - optional - Hue value (0 - 360), to be used as healthy point (default = 120)
        * spot_area - optional - Area of the spot (in pixels, according to size of image) to be counted (default = 50)
        * spot_count - optional - Count of spots to estimate leaf as diseased (default = 100)
        * raw - optional - Whether raw report needs to be attached in response or not (default = False)

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