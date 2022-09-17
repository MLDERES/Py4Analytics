NOW=$(date +"%c")
sed -i "s/Update:.*$/Update: $NOW/" _config.yml