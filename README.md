# dmarctest.py
Tiny phython script to test DMARC.

##  Description
DMARC認証のテスト用スクリプトです。
意図的に認証を失敗させて、DMARCレポートを取得する等の目的で使用します。

## 必須条件
1. LinuxまたはWSL
2. Python3
3. ローカルSMTPサーバー


##  使い方
SSHターミナルコンソールから下記のようにスクリプトを実行。

python3 ./dmarctest.py --to 宛先メールアドレス --hf ヘッダーFrom --ef エンベロープFrom



