
echo "$(date +%Y-%m-%d\ %H:%M:%S), $(curl -s 'https://coinmarketcap.com/fr/currencies/xrp/' | grep -oP '(?<=priceValue ).*(?=</div>)' | grep -Po '\d+\.\d+'| head -1 | cut -d ">" -f 2)" >> prices.csv
