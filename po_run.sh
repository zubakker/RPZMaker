python lang_c.py # заменяем русские буквы на спец символы в файле констант (включая экранирование точек)
python lang_f.py # заменяем русские буквы на спец символы в файле формул (включая экранирование точек)
python main.py
python lang.py # заменяем спец символы обратно на русские буквы в итоговом файле
echo '%s/\\\././g | w' | vim -e rr_kp.md # убираем экранирование точек ('\.' -> '.')
pandoc -s --katex -t html5 -o rr_kp.html rr_kp.md # рендерим html из md файла результата
