echo "まずtweetをスクレイピングします。処理にしばらく時間がかかります。"
twint -u $1 -o all-tweet.csv --csv
twint -u $1 -o tweet-image-only.csv --csv --images


echo "pythonでcsvを処理して画像つきのものを除外します。"
python3 remove-tweets-with-image.py
