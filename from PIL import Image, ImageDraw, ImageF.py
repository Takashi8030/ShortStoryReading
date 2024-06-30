from PIL import Image, ImageDraw, ImageFont

# 画像とドローイングオブジェクトを作成
image = Image.new("RGB", (100, 100))
draw = ImageDraw.Draw(image)

# フォントを設定（フォントファイルのパスは環境に合わせて変更してください）
font = ImageFont.truetype("~/Library/Fonts/NotoSerifJP-Bold.otf", 15)

# テキストのサイズを取得
text = "Hello, world!"
text_width, text_height = draw.textsize(text, font=font)

print(text_width, text_height)