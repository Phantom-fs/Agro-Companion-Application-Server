# Agro-Companion-Application-Server

This repository contains the server code for the Agro Companion application, which is designed to assist in soil classification and crop recommendation using advanced machine learning techniques and fuzzy logic. The application leverages ensembled Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) for precise soil classification and provides adaptive crop recommendations based on various environmental and soil parameters.

## Overview

Agro Companion is designed to assist farmers and agricultural enthusiasts by classifying different types of soil and providing advanced crop recommendations based on various factors. Users can easily classify different types of soil such as alluvial soil, black soil, red soil, yellow soil, laterite soil, arid soil, and mountain soil. The platform also offers crop recommendations considering factors like soil type, season, rainfall, temperature, humidity, nitrogen, phosphorus, potassium, and specific regional data, and it also provides a tool to access these information for specific crops. If climate data is not available for crop recommendation, the platform fetches the necessary information using a weather API.

<blockquote>
This application was developed as part of the research paper titled "<em>An advanced artificial intelligence framework integrating ensembled convolutional neural networks and Vision Transformers for precise soil classification with adaptive fuzzy logic-based crop recommendations</em>" by Farhan Sheth, Priya Mathur, Amit Kumar Gupta, and Sandeep Chaurasia, published in <b>Engineering Applications of Artificial Intelligence</b>.
</blockquote>

### Links
- **Paper**: [An advanced artificial intelligence framework integrating ensembled convolutional neural networks and Vision Transformers for precise soil classification with adaptive fuzzy logic-based crop recommendations](https://doi.org/10.1016/j.engappai.2025.111425)
- **Agro Companion Application**: [Agro Companion](https://github.com/Phantom-fs/Agro-Companion)
- **Dataset**: [Soil Classification Dataset](https://github.com/Phantom-fs/Soil-Classification-Dataset)
- **Code**: [Development Code (model and recommendation system)](https://github.com/Phantom-fs/Agro-Companion-Modules)

## Features

- **Soil Classification**: Identify and learn about different types of soil including alluvial, black, red, yellow, arid, and mountain soils.
- **Advanced Crop Recommendation**: Receive crop recommendations based on multiple factors such as soil type, season, climate conditions, and soil nutrients.
- **Climate Data Integration**: Fetches real-time weather data using a weather API when local climate data is unavailable.
- **Crop Information**: Detailed information on the requirements for growing specific crops, including ideal soils, season, rainfall, temperature, humidity, nitrogen, phosphorus, and potassium levels.
- **User-Friendly Interface**: Intuitive and easy-to-navigate interface for seamless user experience.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python-based server
- **Machine Learning**: Classification and fuzzy-logic based recommendation models
- **API Integration**: Weather API for real-time climate data
- **Application Server**: Deployed on a cloud platform Heroku

## How It Works

1. **Soil Classification**: Users can input soil data or upload an image to identify the soil type. The system processes the data/image and classifies the soil. The system uses ensembled CNN and ViT model for classification.
2. **Crop Recommendation**: Users can input various parameters such as soil type, season, and nutrient levels. The system provides crop recommendations based on these inputs. The system using fuzzy inference system for recommendation
3. **Climate Data Fetching**: If local climate data is not provided, the system uses a weather API to fetch real-time climate data relevant to the user's location.
4. **Detailed Crop Information**: Users can browse through a database of crops to view detailed growing requirements, including ideal soil type, climate conditions, and nutrient levels.

## Citation
Please cite the following paper if you use this application in your research or projects:

```bibtex
@article{SHETH2025111425,
    title = {An advanced artificial intelligence framework integrating ensembled convolutional neural networks and Vision Transformers for precise soil classification with adaptive fuzzy logic-based crop recommendations},
    journal = {Engineering Applications of Artificial Intelligence},
    volume = {158},
    pages = {111425},
    year = {2025},
    issn = {0952-1976},
    doi = {https://doi.org/10.1016/j.engappai.2025.111425},
    url = {https://www.sciencedirect.com/science/article/pii/S0952197625014277},
    author = {Farhan Sheth and Priya Mathur and Amit Kumar Gupta and Sandeep Chaurasia},
    keywords = {Soil classification, Crop recommendation, Vision transformers, Convolutional neural network, Transfer learning, Fuzzy logic}
}
```

## Developer
- ***[Farhan Sheth](https://www.linkedin.com/in/farhan-sheth/)***

----

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is a research prototype and is not intended for production use. It is provided "as is" without any warranties or guarantees. Use at your own risk.