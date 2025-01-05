# LDR to HDR conversion.

<div>
  <img src="https://i.imgur.com/F8xGFhW_d.webp?maxwidth=760&fidelity=grand" alt="LDR-to-HDR" style="height:500px;width:500px;">
</div>

  
## Abstract
<p align="center">High dynamic range (HDR) imaging provides the capability of handling real world lighting as opposed to the low dynamic range (LDR) which struggles to accurately represent images with higher dynamic range. However, most imaging content is still available only in LDR. This implementation presents a method for generating HDR images from LDR images based on Convolutional Neural Networks . The model attempts to reconstruct missing information that was lost from the original image . The image is reconstructed from learned features .The model is trained in a supervised method using a dataset of HDR images.</p>


## Table of Contents
- [Introduction](#introduction) <br>
- [Requirements](#requirements) <br>
- [How to use](#installation-and-usage) <br>
- [Preview](#previews)
- [Contribution](#contribution)

## Introduction
This project is a simple implementation of a LDR to HDR conversion using Convolutional Neural Networks.The model is trained on a dataset of HDR images and is able to reconstruct missing information that was lost from the original image. The image is reconstructed from learned features.The model is trained in a supervised method using a dataset of HDR images.
The model is able to handle real world lighting and is able to accurately represent images with higher dynamic range than LDR images.

## Requirements
- Python 3.8
- numpy 1.26.8
- PyTorch 1.9.0
- imageio 2.36.0
- streamlit 1.40.1
- scikit-image 0.24.0
- opencv python headless 4.10.0.84



## Installation and usage
Step by step process of cloning the project, installments needed and how to use it

- Clone the repository
- Run `pip install -r requirements.txt` to download all necessary dependencies
- Run `streamlit run app.py` to run the conversion algorithm, and upload the picture to the website opened.


## Preview
Screenshots of the project
<img src="https://i.imgur.com/pdu1ccZ.jpeg">

## Contribution 
**This section provides instructions and details on how to submit a contribution via a pull request. It is important to follow these guidelines to make sure your pull request is accepted.**
1. Before choosing to propose changes to this project, it is advisable to go through the readme.md file of the project to get the philosophy and the motive that went behind this project. The pull request should align with the philosophy and the motive of the original poster of this project.
2. To add your changes, make sure that the programming language in which you are proposing the changes should be the same as the programming language that has been used in the project. The versions of the programming language and the libraries(if any) used should also match with the original code.
3. Write a documentation on the changes that you are proposing. The documentation should include the problems you have noticed in the code(if any), the changes you would like to propose, the reason for these changes, and sample test cases. Remember that the topics in the documentation are strictly not limited to the topics aforementioned, but are just an inclusion.
4. Submit a pull request via [Git etiquettes](https://gist.github.com/mikepea/863f63d6e37281e329f8) 

