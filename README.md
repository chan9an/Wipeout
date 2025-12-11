# Wipeout – Image Background Remover Plugin for Dify

**Author:** chan9an  
**Version:** 0.0.1  
**Type:** tool  

## Description
Wipeout is a simple and efficient background-removal plugin for Dify.  
It allows users to upload an image and automatically removes the background, returning a transparent PNG.

The plugin internally uses **rembg** (U2-Net / ONNX runtime) for fast background extraction.

---

## Features
- Removes image backgrounds automatically  
- Returns transparent PNG output  
- Works with most common image formats  
- Lightweight and easy to integrate into Dify workflows  

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/chan9an/Wipeout
cd Wipeout
