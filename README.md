# dmarctest.py

## 説明
DMARC認証のテスト用スクリプトです。
意図的に認証を失敗させて、DMARCレポートを取得する等の目的で使用します。

## 必須条件
1. LinuxまたはWSL
2. Python3
3. ローカルSMTPサーバー

## 使い方
SSHターミナルコンソールから下記のようにスクリプトを実行。

```
python3 ./dmarctest.py --to 宛先メールアドレス --hf ヘッダーFrom --ef エンベロープFrom
```

###  DMARC認証失敗レポートを発生させるには
--hfと--efにて異なるメールアドレスを記述します。例えば、下記のようにすればSPFアラインメントのDMARC認証エラーとなります。
ヘッダーFromが@rms.ne.jp、エンベロープFromが@brandkeeper.jpとなりドメインが異なるので、アラインメントエラーとなります。

アラインメントエラーの場合
```
python3 ./dmarctest.py --to brandkeeper.jp@gmail.com --hf info@rms.ne.jp --ef fake@brandkeeper.jp
```

DMARC認証成功の場合
```
python3 ./dmarctest.py --to brandkeeper.jp@gmail.com --hf info@rms.ne.jp --ef fake@brandkeeper.jp
```


### DMARCレポートの動き
次に、DMARCレポートの動きを見ます。
上記の例の場合は、DMARCレポートはヘッダーFromのドメイン宛てにDMARC認証エラーのレポートが送信されます。




