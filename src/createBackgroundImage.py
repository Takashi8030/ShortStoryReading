from PIL import Image, ImageDraw, ImageFont
import os

# 画像の基本設定
width, height = 1920, 1080
background_color = (220, 220, 220)  # 明度が高く彩度が低い色

# 新しい画像を作成
image = Image.new("RGB", (width, height), color=background_color)
draw = ImageDraw.Draw(image)

# 明朝体のフォントを設定（フォントのパスは環境によって異なる場合があります）
font_path = "~/Library/Fonts/NotoSerifJP-Bold.otf"  # 明朝体のフォントパスを適宜変更してください
font_size = 200
font = ImageFont.truetype(font_path, font_size)

# textsフォルダからtxtファイルを読み込む
texts_dir = "../texts"
for filename in os.listdir(texts_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(texts_dir, filename), "r", encoding="utf-8") as file:
            lines = file.readlines()
            title, author = "", ""
            for line in lines:
                if "。" not in line:
                    if not title:
                        title = line.strip()
                    elif not author:
                        author = line.strip()
                        break

            # タイトルと作者を画像に描画
            text = f"{title}\n{author}"
            text_box = draw.textbbox((0, 0), text, font=font)
            text_width = text_box[2] - text_box[0]
            text_height = text_box[3] - text_box[1]

            while text_width > width-200:
                font_size -= 1
                font = ImageFont.truetype(font_path, font_size)
                text_box = draw.textbbox((0, 0), text, font=font)
                text_width = text_box[2] - text_box[0]
                text_height = text_box[3] - text_box[1]

            text_x = (width - text_width) / 2
            text_y = (height - text_height) / 2
            draw.text((text_x, text_y), text, fill="black", font=font, align="center")

            # 画像を保存
            image.save(f"../backgroundImages/{filename[:-4]}.png")
            # 画像を初期化（まっさらに戻す）
            draw.rectangle((0, 0, width, height), fill=background_color)
            font_size = 200
            font = ImageFont.truetype(font_path, font_size)