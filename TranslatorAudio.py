from speakerpy import lib_sl_text
from speakerpy import lib_speak
from googletrans import Translator
import whisper
import os

global dir # директория проекта

# Функция преобразования текста в речь
def text_to_sp(text):
   text_t = lib_sl_text.SeleroText(text, to_language="ru")
   speaker = lib_speak.Speaker(model_id="ru_v3", language="ru", speaker="aidar", device="cpu")
   speaker.to_mp3(text=text, name_text="Текст", sample_rate=48000,
                  audio_dir=str(dir), speed=1.0)

# Функция перевода текста
def eng_to_rus(text):
  translator = Translator()
  text_Rus = translator.translate(text, src='en', dest='russian')
  return text_Rus.text


dir = os.path.dirname(os.path.abspath(__file__))
# Модель для извлечения текста из исходного аудио
model = whisper.load_model("base")
# Исходное аудио на английском
audio = rf"{dir}\audio_test.mp3"
# Извлечение текста из исходного аудио на английском
transcribe = model.transcribe(audio, fp16=False)
# Перевод извлечённого текста на русский язык
string = eng_to_rus(transcribe['text'])
# Конвертация русского текста в речь
text_to_sp(text=string)