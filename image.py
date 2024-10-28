from transformers import pipeline # Importing the pipeline function from Hugging Face's transformers library
from PIL import Image # Importing the Image class from the Pillow library for image handling
import requests # Importing requests library to handle HTTP requests for images
import os # Importing os for file handling, if needed

# Load a larger, more accurate image classification model from huggingface
classifier = pipeline("image-classification", model="google/vit-large-patch32-384")

def classify_images(image_paths, confidence_threshold=0.1):
    """
    Classify multiple images using a pre-trained image classification model with improved accuracy and filtering.

    Parameters:
        image_paths (list): List of paths or URLs of the images to classify.
        confidence_threshold (float): Minimum score to display classification results.

    Returns:
        dict: A dictionary with image paths as keys and classification labels with scores above the confidence threshold as values.
    """
    results = {}

# Loop through each image path (either a URL or a local file path)
    for image_path in image_paths:
        try:
            # check if the image path is from URL or file
            if image_path.startswith("http"):
                # Send a GET request to download the image
                response = requests.get(image_path, stream=True)
                
                # verify if the request was successful
                if response.status_code == 200:
                    # Open the image directly from the response stream
                    image = Image.open(response.raw)
                else:
                    #If unsuccessful, log an error and move to the next image
                    print(f"Failed to retrieve image from {image_path}, status code: {response.status_code}")
                    results[image_path] = None
                    continue
            else:
                image = Image.open(image_path) # If the path is a local file, open it directly

            # Resize image to match model's expected input size (384x384 for vit-large-patch32-384)
            image = image.resize((384, 384))

            # Use the classifier to predict the label
            result = classifier(image)

            # Filter results based on confidence threshold
            filtered_result = [label for label in result if label['score'] >= confidence_threshold]
            results[image_path] = filtered_result

             # Print the classification results for each image that meets the confidence threshold
            print(f"\nResults for {image_path}:")
            for label in filtered_result:
                print(f"Label: {label['label']}, Score: {label['score']:.4f}")

        except Exception as e:
         # Handle errors, such as file not found or image decoding issues
            print(f"Error loading or classifying image {image_path}: {e}")
            results[image_path] = None

    return results # Return the dictionary containing classification results for all images

# Test the function with a list of images (URLs or local paths)
if __name__ == "__main__":
    # URLs
    image_urls = [
    "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee",
    "https://images.unsplash.com/photo-1593642532973-d31b6557fa68"
]
 # Call the classify_images function with the list of URLs
    classify_images(image_urls)


