import pyocr
from PIL import Image, ImageEnhance
import os

TESSERACT_PATH = 'C:\\Program Files\\Tesseract-OCR'
TESSDATA_PATH = TESSERACT_PATH + '\\tessdata'

os.environ["PATH"] += os.pathsep + TESSERACT_PATH
os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

def relativePath(path):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return str(cwd + "/" + path)

#OCRエンジン取得
tools = pyocr.get_available_tools()
tool = tools[0]

#OCRの設定 ※tesseract_layout=6が精度には重要。デフォルトは3
builder = pyocr.builders.TextBuilder(tesseract_layout=6)

#解析画像読み込み(雨ニモマケズ)
img = Image.open(relativePath('test.jpg')) #他の拡張子でもOK

#適当に画像処理(何もしないと結構制度悪いです・・)
img_g = img.convert('L') #Gray変換
enhancer= ImageEnhance.Contrast(img_g) #コントラストを上げる
img_con = enhancer.enhance(2.0) #コントラストを上げる

#画像からOCRで日本語を読んで、文字列として取り出す
txt_pyocr = tool.image_to_string(img_con , lang='jpn', builder=builder)

#半角スペースを消す ※読みやすくするため
txt_pyocr = txt_pyocr.replace(' ', '')

print(txt_pyocr)