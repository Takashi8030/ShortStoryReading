import os
import requests
from bs4 import BeautifulSoup
import re

# フォルダの作成（存在しない場合）
if not os.path.exists('texts'):
    os.makedirs('texts')

# URLの設定
base_url = 'https://bungo-search.com'
authors_url = f'{base_url}/authors/all/categories/flash/books'

# requestsを使って、ウェブページの内容を取得
response = requests.get(authors_url)

# BeautifulSoupオブジェクトの作成
soup = BeautifulSoup(response.text, 'html.parser')

# 特定の形式のリンクを取得し、重複を排除しつつ順序を保持
pattern = re.compile(r'/authors/\d+/categories/flash/books/\d+')
links = []
for a in soup.find_all('a', href=True):
    if pattern.match(a['href']) and a['href'] not in links:
        if "この作品は著作権が存続しています" in requests.get(base_url+a['href']).text:
            print(f"著作権が存続しているため、{a['href']}の処理をスキップします。")
            continue
        links.append(a['href'])

# 取得したリンクにアクセスし、特定の形式のリンクを取得
aozora_link_pattern = re.compile(r'https://www.aozora.gr.jp/cards/\d+/files/\d+_\d+.html')
i = 0
for link in links:
    i += 1
    full_link = base_url + link
    response = requests.get(full_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    aozora_links = [a['href'] for a in soup.find_all('a', href=True) if aozora_link_pattern.match(a['href'])]
    
    # 青空文庫のリンクから本文を取得し、ルビを削除して保存
    for aozora_link in aozora_links:
        response = requests.get(aozora_link)
        # 適切なエンコーディングを設定
        content = response.content.decode('Shift_JIS', errors='replace')
        
        # ルビタグとその前後の改行を削除
        content = re.sub(r'\n*\s*<ruby>.*?<rt>(.*?)</rt>.*?</ruby>\s*\n*', r'\1', content, flags=re.DOTALL)
        # 「底本:」以降を削除
        content = re.sub(r'底本：.*', '', content, flags=re.DOTALL)
        # 改行の直前に句点がない場合は句点を追加
        content = re.sub(r'(?<!。)\n', '。\n', content)

        soup = BeautifulSoup(content, 'html.parser')
        
        # 本文の取得（例として<body>タグ内のテキストを取得）
        text = soup.body.get_text(separator='\n', strip=True)
        
        # ファイル名の生成（URLの最後の部分を使用）
        filename = str(i)+'.txt'
        filepath = os.path.join('texts', filename)
        
        # テキストファイルとして保存
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
        
        print(f'ファイル"{filename}"を保存しました。')