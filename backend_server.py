from flask import Flask, request, send_file
from remove_bg import remove_background # Import your background removal function

app = Flask(__name__)

# Define the endpoint for background removal
@app.route('/remove-background', methods=['POST'])
def remove_bg_endpoint():
    image_data = request.files['image']
    processed_image = remove_background(image_data)
    return send_file(processed_image, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True) # You can change debug to False in production
