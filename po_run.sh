python lang_c.py # заменяем русские буквы на спец символы в файле констант (включая экранирование точек)
python lang_f.py # заменяем русские буквы на спец символы в файле формул (включая экранирование точек)
python main.py
python lang.py # заменяем спец символы обратно на русские буквы в итоговом файле
echo '%s/\\\././g | w' | vim -e out_calculated.md # убираем экранирование точек ('\.' -> '.')
echo '%s/\\overla/\\overleftarrow/g | w' | vim -e out_calculated.md # убираем экранирование точек ('\.' -> '.')
echo $'%s/_{Omicron}/\\\'/g | w' | vim -e out_calculated.md
echo $'%s/_{\\\\Omicron}/\\\'/g | w' | vim -e out_calculated.md
echo $'%s/_{\\\\Omicron\\\'/\\\'\\\'_{/g | w' | vim -e out_calculated.md
echo $'%s/_{Omicron/\\\'_{/g | w' | vim -e out_calculated.md
echo $'%s/_{\\\\Omicron/\\\'_{/g | w' | vim -e out_calculated.md
pandoc -s --katex -t html5 -o out.html out_calculated.md # рендерим html из md файла результата
