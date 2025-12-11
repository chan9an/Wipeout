## Privacy Policy 
Wipeout is a background-removal plugin designed for Dify. This privacy policy explains what data is processed, how it is handled, and the measures taken to protect user information.

### 1. Data Collection
Wipeout processes only the data required to remove the background from images:

- **User-uploaded image files**  
  These images are sent to the background-removal engine (rembg / ONNX model) for processing.
- **No personal information** such as names, emails, or identifiers is collected.

### 2. How the Data Is Used
- The plugin uses the provided image **solely for background removal**.
- The processed image is returned to the user.  
- No images or metadata are stored permanently.

### 3. External API or Service Usage
Depending on configuration:

- Wipeout may use **local rembg inference** (default), OR  
- It may call **an external remote background-removal API** *only if the user configures one*.

If an external endpoint is used, images are transmitted to that server for processing.

### 4. Data Retention
- Wipeout does **not store or retain** uploaded images.  
- All images exist **only in memory** for the duration of processing and are discarded immediately.

### 5. Security Measures
- Images are transmitted only through Dify’s internal plugin interface.
- No logs of image content are stored.
- The plugin performs no analytics, tracking, or telemetry.

### 6. User Rights
Users may:
- Remove their data by simply deleting the image or closing the session  
- Configure alternative processing endpoints  
- Review and modify plugin settings at any time  

### 7. Contact
For questions or issues, please open an issue on the repository:  
**https://github.com/chan9an/Wipeout**

