from flask import Flask, render_template, request
import numpy as np
from templates.train_a import *

app = Flask(__name__)

# localhost:5000/ -> home page
@app.route('/')
def home():
    return render_template('index.html')

# i have a model.pkl file that contains the model and the predict function and it returns the prediction

@app.route('/predict', methods=['POST'])
def predict():
    device_name= request.form['device_name']
    network=request.form['network']
    device_brands=['Acer', 'Alcatel', 'Apple', 'Asus', 'BlackBerry', 'Celkon', 'Coolpad', 'Gionee', 'Google', 'HTC', 'Honor', 'Huawei', 'Karbonn', 'LG', 'Lava', 'Lenovo', 'Meizu', 'Micromax', 'Microsoft', 'Motorola', 'Nokia', 'OnePlus', 'Oppo', 'Others', 'Panasonic', 'Realme', 'Samsung', 'Sony', 'Spice', 'Vivo', 'XOLO', 'Xiaomi', 'ZTE']
    dic={'screen_size': 0,'rear_camera_mp': 0,'front_camera_mp': 0,'internal_memory': 0,'ram': 0,'battery': 0,'days_used': 0,'normalized_new_price': 0,'device_brand_Acer': 0,'device_brand_Alcatel': 0,'device_brand_Apple': 0,'device_brand_Asus': 0,'device_brand_BlackBerry': 0,'device_brand_Celkon': 0,'device_brand_Coolpad': 0,'device_brand_Gionee': 0,'device_brand_Google': 0,
 'device_brand_HTC': 0,
 'device_brand_Honor': 0,
 'device_brand_Huawei': 0,
 'device_brand_Karbonn': 0,
 'device_brand_LG': 0,
 'device_brand_Lava': 0,
 'device_brand_Lenovo': 0,
 'device_brand_Meizu': 0,
 'device_brand_Micromax': 0,
 'device_brand_Microsoft': 0,
 'device_brand_Motorola': 0,
 'device_brand_Nokia': 0,
 'device_brand_OnePlus': 0,
 'device_brand_Oppo': 0,
 'device_brand_Others': 0,
 'device_brand_Panasonic': 0,
 'device_brand_Realme': 0,
 'device_brand_Samsung': 0,
 'device_brand_Sony': 0,
 'device_brand_Spice': 0,
 'device_brand_Vivo': 0,
 'device_brand_XOLO': 0,
 'device_brand_Xiaomi': 0,
 'device_brand_ZTE': 0,
 '4g_no': 0,
 '4g_yes': 0,
 '5g_no': 0,
 '5g_yes': 0}
    dic['screen_size']=float(request.form['screen_size'])
    dic['rear_camera_mp']=float(request.form['rcm'])
    dic['front_camera_mp']=float(request.form['fcm'])
    dic['internal_memory']=int(request.form['storage'])
    dic['ram']=int(request.form['ram'])
    dic['battery']=int(request.form['battery'])
    dic['days_used'] =int(request.form['days_used'])
    dic['normalized_new_price']=float(request.form['new_price'])
    newprice = dic['normalized_new_price']
    for i in device_brands:
        if i==device_name:
            index = device_brands.index(device_name)
            dict_index=index+8
    keys_list = list(dic.keys())
    dic[keys_list[dict_index]]=1
    if network=='4g':
        dic['4g_yes']=1
        dic['5g_yes']=0
    elif network=='3g':
        dic['4g_yes']=0
        dic['5g_yes']=0
    else:
        dic['5g_yes']=1
        dic['4g_yes']=1
    values_list = list(dic.values())
    print(values_list)
    arr=[]
    pred = used_price_prediction(values_list)
    usedprice = pred[0]
    usedprice -= 0.12*newprice
    usedprice = round(usedprice, 2)
    arr.append(usedprice)
    days = dic['days_used']
    value2=success_rate(days,usedprice,newprice)
    arr.append(value2)
    return render_template('index.html',value=arr)
if __name__ == "__main__":
    app.run(debug=True)