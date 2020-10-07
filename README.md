# Zscaler
## ZscalerのAPIを利用したスクリプト
Zscalerヘルプページに記載のAPI Referenceよりスクリプトを作成しています。
https://help.zscaler.com/zia/api

## 各種説明
+ `.env-sample` : Zscaler API利用にあたって必要な管理者アカウント情報やAPIトークンを格納
+ `settings.py` : .envからアカウント情報を取得するための関数を定義
+ `getApiSession.py` :  APIトークンは利用にあたって、現在時刻情報から難読化処理が必要ではり、本ファイルで関数を定義