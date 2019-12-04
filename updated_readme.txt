#install the following required modules

pip install django==1.11.17
pip install djangorestframework


# black friday product prices
http://127.0.0.1:8005/api/get-price/?product_code=big_widget&date=25-11-2019(DD-MM-YYYY)

#change the date according to the requirement it will give you different price

http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=23-11-2019 to 25-11-2019  (DD-MM-YYYY)
http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=29-11-2019                (DD-MM-YYYY)
http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=25-11-2018                (DD-MM-YYYY)

### Technical Requirements
* We currently have to products with the following prices:
    * Big Widget - $1000
    * Small Widget - $99
* These products, along with existing gift cards are already setup in the database.  Study the existing models and initial data.
* Create a new ProductPrice model and setup the following price schedule:    
  * Black Friday Prices (November 23, 24, & 25)
    * Big Widget - $800
    * Small Widget - FREE!
  * 2019 Prices (starting January 1, 2019)
    * Big Widget - $1200
    * Small Widget - $125
* Build a JSON API endpoint that accepts a product code, date, and (optional) gift card and returns product price.
  * The endpoint should live at `api/get-price` and accept the following parameters:
    * `"productCode"`
    * `"date"`
    * `"giftCardCode"`
* Update this README file with instructions on how to run and access your price calculator.
* Create a pull request with your changes.

### Additional Information
* Please use Django Rest Framework or a Python web framework of your choice to create the endpoint.
* Just as a general guideline, we've designed this exercise to take less than 4 hours.
