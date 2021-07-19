## Import pytesseract and PIL
```
import pytesseract as tess
from PIL import Image
```
## Set Tesserect Application Path
```
tess.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
## Opening image
```
img = Image.open("img.jpg")
```
## Extracting text
```
text= tess.image_to_string(img)
```

# How to get tesseract application
**Tesseract link :** [Download](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe) for window 64
