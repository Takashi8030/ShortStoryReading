# ShortStoryReading
## 概要
  青空文庫の著作権切れの小説をWebスクレイピングし、合成音声化しYoutubeにアップできるスクリプト

## フォルダ・ファイル説明
  backgroundImages : 動画の背景の保存場所
  readingVoices :    合成音声データの保存場所
  src : ソースコードの保存場所
    convertTextToReading.py : textsに保存された文章を合成音声に変換するプログラム
    createBackgroundImage.py : textsからタイトルと著者を抽出し、動画の背景画像を生成するプログラム
    getTextForSSR.py : 青空文庫から著作権の小説のタイトル、著者、本文を抽出するプログラム

## 注意事項・備忘録
  1. convertTextToReading.py
     1. 実行するときはVOICEBOXのソフトウェアを立ち上げること
     1. VOICEBOX側の合成音声に変換する処理がかなり重い
  1. createBackgroundImage.py
     1. タイトルの大きさなどは要調整
  1. getTextForSSR.py
     1. テキスト整形は改善の余地あり(2024/06/30)
