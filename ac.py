from playsound import playsound
from gtts import gTTS
import pytesseract
import cv2

cuadro = 100
anchoC = 640
altoC = 480

cap = cv2.VideoCapture(0)
cap.set(3, anchoC)
cap.set(4, altoC)

def text(imagen):
  # archivo de texto, lenguaje, nombre con el que se va a guardar
  def voz(archi_text, lenguaje, nom_archi):
    with open(archi_text, "r") as lec:  # abrir archivo de texto
      lectura = lec.read()
    lect = gTTS(text=lectura, lang=lenguaje, slow=False)
    nombre = nom_archi
    lect.save(nombre)

  #pytesseract.pytesseract.tesseract_cmd = r'/tesseract.exe'
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
  texto = pytesseract.image_to_string(gris)
  print(texto)
  direc = open('Info.txt', "w")
  direc.write(texto)
  direc.close()
  voz("Info.txt", "es", "Voz.mp3")
  audio = "Voz.mp3"
  playsound(audio)


while True:
  ret, frame = cap.read()
  if ret == False:
    break
  cv2.putText(frame, 'Coloque aqui el texto a leer', (158, 80),
              cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0), 2)
  cv2.putText(frame, 'Coloque aqui el texto a leer', (158, 80),
              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
  cv2.rectangle(frame, (cuadro, cuadro), (anchoC -
                cuadro, altoC - cuadro), (0, 0, 0), 2)
  x1, y1 = cuadro, cuadro
  ancho, alto = (anchoC - cuadro) - x1, (altoC - cuadro) - y1
  x2, y2 = x1 + ancho, y1 + alto
  doc = frame[y1:y2, x1:x2]
  cv2.imwrite("Imatext.jpg", doc)

  cv2.imshow("Lector inteligente", frame)
  t = cv2.waitKey(1)
  if t == 27:
    break

text(doc)
cap.release()
cv2.destroyAllWindows()
