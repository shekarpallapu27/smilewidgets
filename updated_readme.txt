#install the following required modules

pip install django==1.11.17
pip install djangorestframework


# black friday product prices
http://127.0.0.1:8005/api/get-price/?product_code=big_widget&date=25-11-2019(DD-MM-YYYY)

#change the date according to the requirement it will give you different price

http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=25-11-2019      (DD-MM-YYYY)
http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=29-11-2019      (DD-MM-YYYY)
http://127.0.0.1:8000/api/get-price/?product_code=big_widget&date=25-11-2018      (DD-MM-YYYY)