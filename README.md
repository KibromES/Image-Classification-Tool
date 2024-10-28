# Image-Classification-Tool

#Overview

This project is an image classification tool built with Python, using the Hugging Face transformers library. It employs a pre-trained model to classify images, supporting both URLs and local image files. The tool can process multiple images at once.

#Tool Features

    Batch Image Classification: Classify multiple images from URLs or file paths.
    Confidence-Based Filtering: Customize the minimum confidence score for displaying classification results.
    Error Handling: Automatically handles inaccessible URLs, providing detailed error messages for easy debugging.
    Resizing for Model Compatibility: Images are resized to the required 384x384 pixels to match the model's input specifications.

#Installation

To use this tool, you need Python and several Python libraries. Follow these steps to set up:

    Install Python:
    Ensure Python is installed on your system. Download it from python.org.

    Install Required Libraries:
    The transformers, Pillow, and requests libraries are needed. Install them via pip:

    bash

    pip install transformers pillow requests

#How to Use
Running the Script

    Clone this repository or copy the code into a Python file.
    Modify the image_urls list in the __main__ section to include the URLs or file paths of images you want to classify.
    Run the script from your terminal:

    bash

    python /path/to/your/script.py which is 
    python /home/kibrom/python/image.py


Code Configuration:

    Image URLs or Paths:
    Update the image_urls list in the __main__ block to specify the images you want to classify:

    python

    image_urls = [
        "https://example.com/image1.jpg",
        "/path/to/local/image2.jpg"
    ]

    Confidence Threshold:
    Adjust the confidence_threshold parameter in the function call to control the minimum confidence score required for displaying a result. The default threshold is set to 0.1.

#Output

The following is a sample output when running the script with two example image URLs:

plaintext

(image_classification_env_3.12) ➜  ~ python /home/kibrom/python/image.py

Results for https://images.unsplash.com/photo-1606112219348-204d7d8b94ee:

Results for https://images.unsplash.com/photo-1593642532973-d31b6557fa68:
Label: notebook, notebook computer, Score: 0.8998

In this example, the tool classified the second image with high confidence as a "notebook" or "notebook computer," while the first image did not return any results above the confidence threshold.
Objective

This tool is designed to make image classification quick and accessible, with flexibility for different image sources (URLs or local files) and adjustable confidence thresholds. It’s ideal for rapid image categorization and exploring pre-trained model capabilities.


