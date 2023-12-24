# BigData
Skripta se kuca na https://query.wikidata.org/ , sacuvan kao SestrinskiGradovi.csv
```
SELECT ?city ?cityLabel ?city_population ?city_country ?city_countryLabel ?sister ?sisterLabel ?sister_population ?sister_country ?sister_countryLabel WHERE {
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    ?city wdt:P31 wd:Q515.
    ?city wdt:P17 ?city_country.
    ?city wdt:P1082 ?city_population.
    ?city wdt:P190 ?sister.
    ?sister wdt:P1082 ?sister_population.
    ?sister wdt:P17 ?sister_country.
}
```

### Hadoop komande: 
hadoop version </br>
start-all.sh </br>
hdfs namenode -format </br>
.. / cd hadoop / cd sbin </br>
start-dfs.cmd ( http://localhost:9870 ) </br>
jps </br>
start-yarn.cmd ( http://localhost:8088/cluster ) </br>

Importovanje SestrinskiGradovi.csv u hadoop 
```
hdfs dfs -put SestrinskiGradovi.csv /user/branislav.brnjos
```

CMD komande za pokretanje map reduce algoritama:
```
chmod +x /Users/branislavbrnjos/Desktop/BigData/mapper.py
chmode +x /Users/branislavbrnjos/Desktop.BigData/reducer/py
```
```
hadoop jar /Users/branislavbrnjos/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \                              
-file /Users/branislavbrnjos/Desktop/BigData/mapper.py -mapper /Users/branislavbrnjos/Desktop/BigData/mapper.py \
-file /Users/branislavbrnjos/Desktop/BigData/reducer.py -reducer /Users/branislavbrnjos/Desktop/BigData/reducer.py \
-input hdfs:///user/branislav.brnjos/SestrinskiGradovi.csv \
-output hdfs:///user/branislav.brnjos/grana.csv
```


![Screenshot_3](https://github.com/Jxis/BigData/assets/24139683/f4abddad-ffd8-4349-a781-9747a9b20b17)

![Screenshot_4](https://github.com/Jxis/BigData/assets/24139683/74e90e7c-6607-4189-b77f-47d33e127a87)

![Screenshot_5](https://github.com/Jxis/BigData/assets/24139683/1fa36627-62e9-405e-8d3f-7c8f473e28c3)

![Screenshot_6](https://github.com/Jxis/BigData/assets/24139683/dcadfa61-674e-4c56-bea2-bc6253c8ba98)

![Screenshot_1](https://github.com/Jxis/BigData/assets/24139683/c7655b8c-cc1b-4066-a578-9476cc3676e1)

![Screenshot_2](https://github.com/Jxis/BigData/assets/24139683/bcbd3a03-1230-4ea1-993d-0e68d5649ee0)
