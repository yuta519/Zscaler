# zscaler-sdk

## 概要
[Zscaler API](https://help.zscaler.com/zia/api)を利用して、
ユーザから渡されたURLについて、Zscalerのカテゴライゼーション情報を表示します。

## 各種ファイルの説明
+ `.env-sample` : Zscaler API利用にあたって必要な管理者アカウント情報やAPIトークンを格納
+ `zia.py` :  Zscaler API利用での関数を定義
+ `main.py` :  Zscaler API利用にあたってのmain関数を定義

## pythonバージョン
+ python3.7+

## python外部ライブラリ
+ requests
```
pip install requests

```

## Zscaler必要情報
+ クラウドのドメイン
+ 管理者アカウント
+ 管理者アカウントのパスワード
+ APIキー

## 使用方法
+ URLルックアップ
> python main.py lookup -u *Target URL*

+ ZscalerのURLカテゴリー取得
> python main.py categories

## 注意事項
+ hoge

## ライセンス
+ [MIT license](https://en.wikipedia.org/wiki/MIT_License).
