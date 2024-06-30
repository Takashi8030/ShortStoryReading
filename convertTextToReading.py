import requests
import json
import os
import wave

def vvox_test(text, output_filename):
    host = "127.0.0.1"
    port = 50021
    
    params = (
        ('text', text),
        ('speaker', 37),
    )
    
    query = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )
    
    synthesis = requests.post(
        f'http://{host}:{port}/synthesis',
        headers = {"Content-Type": "application/json"},
        params = params,
        data = json.dumps(query.json())
    )
    
    voice = synthesis.content
    
    # readingVoicesフォルダが存在しない場合は作成
    if not os.path.exists('readingVoices'):
        os.makedirs('readingVoices')
    
    # 音声ファイルの保存パスを指定
    filename = os.path.join("readingVoices", output_filename + ".wav")
    
    # 音声ファイルを保存
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # モノラル
        wf.setsampwidth(2)  # サンプル幅を2bytesに設定
        wf.setframerate(24000)  # サンプリングレートを24000Hzに設定
        wf.writeframes(voice)

if __name__ == "__main__":
    # textsフォルダ内の全テキストファイルをリストアップ
    for text_file in os.listdir('texts'):
        if text_file.endswith('.txt'):
            # ファイルを読み込み
            with open(os.path.join('texts', text_file), 'r', encoding='utf-8') as file:
                text = file.read()
                # テキストファイル名（拡張子なし）を出力ファイル名として使用
                output_filename = os.path.splitext(text_file)[0]
                print(f"'{output_filename}'を生成中…")

                vvox_test(text, output_filename)