# image-to-ascii
convert image file to 2 dotted ascii art
image-to-ascii
画像ファイルをテキストアートに変換します

テキストアートとは、端末の1キャラクタの縦横の比率が1:2なので、1キャラクタを横に半分に割って、1:1にし、上、下にドットがある場合は':'、上にのみドットがある場合は'\''、下にのみドットがある場合は'.'、両方にドットがない場合は' 'で表したアスキーアートのことです。

python3 main.py picturefile [ shrinkscale [ threshold ]]として使います。

普通、shrinkscaleは5、thresholdは0.6位です。きれいな画像が出てこなければ、調整してください。

ソースは、高橋美瑠さんのソースを改変したものです。私は著作権を放棄しますので、ライセンスは、美瑠ちゃんのライセンス条項に従います。
