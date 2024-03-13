from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input 
from tensorflow.keras.preprocessing import image
import numpy as np  
# Load the VGG16 model (include_top=False to exclude the final classification layers)
model = VGG16(weights='imagenet', include_top=False)  
def extract_features(img_path):
   
    img = image.load_img(img_path, target_size=(224, 224))  # Standard input size for VGG
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    preprocessed_img = preprocess_input(img_array)       # Preprocess as expected by VGG

    features = model.predict(preprocessed_img)  # Extract features
    return features 


def generate_caption(image_feature):



    # Start with a beginning token
    input_text = 'startseq' 

    for i in range(max_caption_length):
        # Convert the current input text into a sequence
        sequence = [word_to_index[word] for word in input_text.split() if word in word_to_index]
        sequence = pad_sequences([sequence], maxlen=max_caption_length)  

        # Predict the next word
        prediction = decoder_model.predict([image_feature, sequence], verbose=0) 
        prediction = np.argmax(prediction) 
        
        # Map the predicted index back to a word
        word = index_to_word[prediction] 

        # Stop if we've predicted the end token
        if word == 'endseq':
            break

        # Append the word to our predicted caption 
        input_text += ' ' + word 

    return input_text



