from flask import Flask, render_template, request
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html')
    
    



    
   
    
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator   
from keras.models import load_model
new_model = load_model('cnn_model.h5') 


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True)
training_set = train_datagen.flow_from_directory(
        'flowers/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')
        
        
        
test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
        'flowers/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')
        


    
    

        
        
from keras.preprocessing import image
from keras.models import load_model

def predict_image(img_path):
    test_image = image.load_img(img_path, target_size=(64,64) )
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image,axis=0)
    result = new_model.predict(test_image)
    training_set.class_indices
    if result[0][0]==1:
      output = 'Daisy'
      scname = 'Bellis perennis'
    elif result[0][1]==1:
      output = 'Dandelion'
      scname = 'Taraxacum'
    elif result[0][2]==1:
       output = 'Rose'
       scname = 'Rosa'
    elif result[0][3]==1:
       output = 'Sunflower'
       scname = 'Helianthus'
    elif result[0][4]==1:
       output = 'tulip'
       scname = 'Tulipa'
    return output, scname
    



   
 
   
@app.route('/', methods=['GET', 'POST'])
def getvalue():
    if request.method == 'POST':
       img = request.files['imgfile']
       img_path = "static/images/" + img.filename
       img.save(img_path)
       output, scname = predict_image(img_path)
    return render_template('result.html', o=output, scname=scname, fimage=img.filename)  
    
    
    
    
        
        
       

     

        


  








  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
    
    
 
    
    
    
    
    
    
    
    
    
	
	
	
	


