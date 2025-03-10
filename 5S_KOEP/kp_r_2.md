# Лапа КОЭП МДЗ-2

# ВВЕДЕНИЕ

Целью расчёта является назначение степени точности и вида сопряжения на все зубчатые колеса, такие, что бы обеспечить суммарную погрешность менее заданной.

Основные данные ЭМП приведены в таблице 1 и на рисунке 1.


| Наименование параметра    | Обозначение       | Значение |
| ---                       | ---               | --- |
| Момент нагрузки           | $M_н$             | {M_(н)} $Н \cdot М$ |
| Частота вращения 
выходного вала              | $n_н$             | {n_(н)} $об/мин$ | 
| Угловое ускорение 
вращения выходного вала     | $\varepsilon_н$   | {varepsilon_(н)} $рад/сек^2$ | 
| Момент инерции нагрузки   | $J_н$             | {J_(н)} $кг \cdot м^2$ |
| Температура эксплуатации  | $t_{{жар}}$.. $t_{{хол}}$     | +{t_(жар)}..{t_(хло)} $^\circ С$ |
| Рабочий угол поворота 
выходного вала              | $\alpha_{{вых вала}}$     | {alpha_(выхваал)} $град.$ |
| Точность отработки 
| Критерий расчета          | ---               | комплексный |
| Режим работы двигателя    | ---               | редкие пуски |
| Метод расчета, процент 
риска при расчете, точность | ---               | вероятностный, 1% |
не хуже                     | $\delta_{{\Sigma ТЗ}}$    | {delta_(SigmaЗТ)} $угл.мин.$ | 
| Срок службы не менее      | $L_h$             | {L_(h)} $час$ |

Таблица 1. Основные параметры ЭМП.


**TODO вставить картинку кинематической схемы**

Рисунок 1. Кинематическая схема ЭМП.

# 1. Расчёт вида сопряжения.

Выберем вид сопряжения из условия:
$$
$$

где $j_p$ — расчётное значение бокового зазора;

$j_{{n min}}$ — минимальное значение гарантированного бокового зазора для соответствующего вида сопряжения.

Расчётное значение бокового зазора определяется по формуле:
$$
$$

где $j_n^t$ — боковой зазор, компенсирующий изменение рабочей температуре;

$j_с$ — боковой зазор, необходимый для размещения слоя смазки.

Боковой зазор, компенсирующий изменение рабочей температуре, определяется по формуле:
$$
$$

где $a_\omega$ — межосевое расстояние;

$\alpha_{{зк}}$ и $\alpha_{{кор}}$ — коэффициенты линейного расширения материалов зубчатого колеса и корпуса ({alpha_(зк)} для зубчатого колеса и {alpha_(кор)} для корпуса);

$t_{{зк}}$ и $t_{{кор}}$ — температура нагрева зубчатого колеса и корпуса.

При температуре $+{t_(жар)}^\circ$ получим (приведены расчеты для всех передач):
$$
$$
$$
$$

(При температуре {t_(жар)} все значения бокового зазора $j_n^t < 0$, в этом случае температурные компенсации не нужны.)

При температуре ${t_(хло)} ^\circ$ получим (приведены расчеты для всех передач):
$$
$$
$$
$$

Значения зазора для компенсации температурного диапазона ${t_(хло)}..{t_(жар)}^\circ$:
$j_{{n12}}^t = {j_(nхол12)t} \ (мкм)$,

$j_{{n34}}^t = {j_(nхол34)t} \ (мкм)$.


Значение зазора, необходимого для размещения смазки, определяется по формуле:
$$
$$

где $m$ — модуль зацепления.

$$
$$
$$
$$

Расчётное значение бокового зазора для всех передач:
$$
$$
$$
$$

**Вывод: в соответствии с условием [1], назначаем из таблицы зазоров виды сопряжения:**

первая передача: **F**, степень точности **7**;

вторая передача: **F**, степень точности **7**;

третья передача: **F**, степень точности **7**;

четвёртая передача: **E**, степень точности **7**;

пятая передача: **E**, степень точности **7**.

# 2. Расчёт кинематической погрешности.

Исходя из рекомендаций [1], назначим степень точности TODO на все передачи.

В таблице 2 приведены значения параметров передач.

| № З.К. | $z$     | $d$, $мм$ | $F_r$, $мкм$ | $T_H$, $мкм$ | $F_p$, $мкм$ | $E_H$, $мкм$ |
| ---    | ---     | ---       | ---          | ---          | ---          | ---          |
| 1      | {z_(1)} | {d_(1)}   | {F_(rтабл1)} | {T_(H1)}     | {F_(p1)}     | {E_(HS1)}    |
| 2      | {z_(2)} | {d_(2)}   | {F_(rтабл2)} | {T_(H2)}     | {F_(p2)}     | {E_(HS2)}    |
| 3      | {z_(3)} | {d_(3)}   | {F_(rтабл3)} | {T_(H3)}     | {F_(p3)}     | {E_(HS3)}    |
| 4      | {z_(4)} | {d_(4)}   | {F_(rтабл4)} | {T_(H4)}     | {F_(p4)}     | {E_(HS4)}    |

| Пара З.К. | Вид сопряжения | $K_\phi$   | $K$      | $K_S$     | $f_a$, $мкм$ | $j_{{n \ min}}$, $мкм$ | $a_\omega$, $мм$ | $f_f$     |
| ---       | ---            | ---        | ---      | ---       | ---          | ---                    | ---              | ---       |
| 1-2       | TODO           | {K_(phi2)} | {K_(12)} | {K_(S12)} | {f_(a12)}    | {j_(nmin12)}           | {a_(omega12)}    | {f_(f12)} |
| 3-4       | TODO           | {K_(phi4)} | {K_(34)} | {K_(S34)} | {f_(a34)}    | {j_(nmin34)}           | {a_(omega34)}    | {f_(f34)} |

Таблица 2. Параметры передач. 

Минимальное значение кинематической погрешности для передачопределяется по формуле:
$$
$$

где $K_S$ — коэффициент фазовой компенсации;

$K_\phi$ — коэффициент, учитывающий угол поворота ведомого колеса;

$F_{{iш}}'$ и $F_{{iк}}'$ — допуски на кинематическую погрешность шестерни и колеса.

Допуски на кинематическую погрешность определяются по формуле:
$$
$$

где $F_p$ — допуск на накопленную погрешность шага зубчатого колеса;

$f_f$  — допуск на погрешность профиля зуба.

Произведем расчет для всех передач:
$$
$$
$$
$$
$$
$$
$$
$$

$$
$$
$$
$$

Погрешность монтажа определяется по формуле:
$$
$$

где $e_r$ — монтажное радиальное биение зубчатого колеса;

$e_a$ — монтажное осевое биение зубчатого колеса;

$\alpha = {alpha}\ (радиан)$ — угол исходного профиля колеса;

$\beta = {beta}\ (радиан)$ — делительный угол наклона линии зуба.

Монтажное радиальное и осевое биения зубчатого колеса определяются по формулам:
$$
$$
$$
$$

где $e_i$ и $e_j$ — допуски на погрешность, создающие первичные радиальные и осевые биения.

**Принимаем погрешности монтажа равными нулю, так как отсутствует техническая документация или чертеж со значениями вышеназванных допусков.**

Максимальное значение кинематической погрешности определяется по формулам:
$$
$$
$$
$$

где $K$ — коэффициент фазовой компенсации;

$F_{{iш}}'$ и $F_{{iк}}'$ — допуски на кинематическую погрешность шестерни и колеса;

$K_\phi$ — коэффициент учитывающий угол поворота ведомого колеса;

$E_{{\Sigma M ш}}$ и $E_{{\Sigma Mк}}$ — погрешности монтажа шестерни и колеса (принимаем равными нулю).

Тогда:
$$
$$
$$
$$

Угловая погрешность элементарной передачи определяется по формуле:
$$
$$

где $F_{{i0}}'$ — кинематическая погрешность;

$m$ — модуль зацепления;

$z$ — число зубьев ведомого звена.

Тогда:
$$
$$
$$
$$

$$
$$
$$
$$


Проверка: для всех передач максимальное значение кинематической погрешности больше минимального значения:
$$
$$
$$
$$

# 3. Расчёт погрешности мертвого хода.

Минимальное значение мёртвого хода определяется по формуле:
$$
$$

где $j_{{n  min}}$  — минимальное значение гарантированного бокового зазора соответствующей передачи;

$\alpha = 20^\circ$ — угол исходного профиля колеса;

$\beta = 0^\circ$— угол наклона боковой стороны профиля.

Расчет для всех передач:
$$
$$
$$
$$

Максимальное значение мёртвого хода определяется по формуле:
$$
$$

где $E_{{HS}}$ — наименьшее смещение исходного контура зубчатого колеса;

$T_H$ — допуск на смещение исходного контура зубчатого колеса;

$f_a$ — допуск на отклонение межосевого расстояния передачи;

$\Delta_p$ — радиальный зазор в опорах зубчатого колеса.

Тогда:
$$
$$
$$
$$

Мёртвый ход передачи в угловых минутах определяется по формуле:
$$
$$

где $j_t$ — значение мёртвого хода рассчитываемой передачи;

$d$ — диаметр ведомого ЗК.

$$
$$
$$
$$

$$
$$
$$
$$

Проверка: для всех передач максимальное значение погрешности мертвого хода больше минимального значения.
$$
$$
$$
$$

# 4. Погрешность упругого скручивания валов.

Погрешность мертвого хода передачи, обусловленная скручиванием валов, определяется по формуле:
$$
$$

где $M_{{кр}}$ — крутящий момент на валу;

$l$ — длина рабочего участка вала;

$G = {G} МПа$ — модуль упругости второго рода для стали;

$J_p$ — полярный момент инерции сечения.

Полярный момент инерции определяется по формуле:
$$
$$

где $d_в$  — диаметр вала;

Длина вала расчитывается по формуле:
$$
$$

где $b$ — расстояние от края ступицы З.К. до центра штифта.

Примем $b$ всех з.к. равным TODO, соответственно $l$ всех валов равными:

$l_{{I}} = {l_(I)}$

$l_{{II}} = {l_(II)}$

$l_{{III}} = {l_(III)}$


Произведем расчет для всех валов:
$$
\Delta \phi_I = 0
$$

$$
$$
$$
$$


Переведем значение погрешности из радиан в угловые минуты:
$$
$$

Получим:
$$
\Delta_{{\phi I мин}} = 0
$$

$$
$$
$$
$$


Передаточный коэффициент $j$-той элементарной передачи определяется по формуле:
$$
$$

где $i_{{j-в}}$ — передаточное отношение кинематической цепи между выходными валами j-той передачи и привода.
$$
$$

$$
$$
$$
$$



Суммарная погрешность от скручивания валов определяется выражением:
$$
$$

где $\xi_j$ — передаточный коэффициент j-той элементарной передачи;

$\Delta_{{\phi j мин}}$ — значение погрешности скручивания j-ого вала в угловых минутах.

Тогда:
$$
$$

# 5. Суммарная кинематическая погрешность по вероятностному методу.

Суммарная погрешность по вероятностному методу определяется выражением:
$$
$$

где $\xi_j$ — передаточный коэффициент j-той элементарной передачи;

$t_1$ — коэффициент, учитывающий процент брака;

($t_1 = {t_(1)}$ при $P=$ TODO%);

$$
$$

где $\delta \phi_{{jmax}}$ , $\delta \phi_{{jmin}}$ — максимальное и минимальное значение кинематической погрести для j-той элементарной передачи в угловых минутах;

$$
$$

Произведем расчет для всех передач:
$$
$$
$$
$$

$$
$$
$$
$$

$$
$$
$$
$$

$$
$$

$$
$$

# 6. Суммарная погрешность мертвого хода по вероятностному методу.

Суммарная погрешность по вероятностному методу определяется выражением:
$$
$$

где $\xi_j$ — передаточный коэффициент j-той элементарной передачи;

$t_2$ — коэффициент, учитывающий процент брака;

($t_2={t_(2)}$ при $P=$ TODO%)

$$
$$

где $j_{{\phi max j}}$, $j_{{\phi min j}}$ — максимальное и минимальное значение погрешности мертвого хода для j-той элементарной передачи в угловых минутах;

$$
$$

Произведем расчет для всех передач:
$$
$$
$$
$$


$$
$$
$$
$$

# 7. Общая погрешность. Анализ результатов.

Общая погрешность положения выходного вала ЭМП определенная по вероятностному методу задается выражением:
$$
$$

где $\delta \phi_{{\Sigma Р}}$ — суммарная кинематическая погрешность по вероятностному методу;

$j_{{\Sigma P}}$ — суммарная погрешность мертвого хода по вероятностному методу;

$\Delta_{{\phi' \Sigma}}$ — суммарная погрешность от скручивания валов.

Общая погрешность положения выходного вала ЭМП не должна превышать заданную погрешность с некоторым коэффициентом запаса:
$$
$$

где $\delta_{{0S}}$ — заданная по ТЗ погрешность положения выходного вала;

$n_{{запаса}}$ — коэффициент запаса $n_{{запаса}}=1.05...1.5$.

$$
$$

**Анализ результатов:** 

**Из полученных результатов видно, что общая погрешность превышает заданную в ТЗ. Самое большое значение получилось у погрешности мертвого хода. Скомпенсировать погрешность мертвого хода можно, выбрав более высокую точность или уменьшив диаметры ведомых ЗК (что, в свою очередь, возможно при выборе других передаточных отношений на передачах).**

# 8. Проверочный силовой расчет.

## 8.1. Проверочный расчёт опор.

Окружная и радиальная силы находятся по формулам:
$$
$$
$$
$$

где $M$ – момент на валу;

$d$ – диаметр ЗК;

$\alpha = {alpha} \ (радиан)$—  стандартный угол зацепления;

$\beta = {beta} \ (радиан)$  — угол наклона линии зуба;

$$
$$
$$
$$
$$
$$

$$
$$
$$
$$
$$
$$

### 8.1.1. Расчёт II вала.

**TODO вставить картинку с силами**

Рисунок 2. TODO.

Радиальные нагрузки в каждом креплении вала II на двух опорах можно найти как:
$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$


$L_{{II 1}} = {L_(II1)} \ мм$,

$L_{{II 2}} = {L_(II2)} \ мм$, 

$L_{{II 3}} = {L_(II3)} \ мм$

$$
$$
$$
$$

$$
$$
$$
$$

$$
$$
$$
$$


**За $F_{{r II}}$ примем бо́льшую радиальную нагрузку (в точке B), $F_{{r II}} = {F_(rII)} \ Н$**

### 8.1.2. Расчёт III вала.

**TODO вставить картинку с силами**

Рисунок 3. TODO.

Радиальные нагрузки в каждом креплении вала III на двух опорах можно найти как:
$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$L_{{III 1}} = {L_(III1)} \ мм$, 

$L_{{III 2}} = {L_(III2)} \ мм$

$$
$$
$$
$$

$$
$$
$$
$$

$$
$$
$$
$$


**За $F_{{r III}}$ примем бо́льшую радиальную нагрузку (в точке B), $F_{{r III}} = {F_(rIII)} \ Н$**

### 8.1.3. Расчёт КПД подшипников на валах.

Теперь найдем моменты подшипников для каждого из валов по формуле:
$$
$$

где  $M_0=0.04 \cdot D_0$ – начальный момент трения ненагруженного подшипника;

$f$ – коэффициент трения качения ($0.01 .. 0.02$ при радиальной нагрузке, принимаем $f = {f}$);

$D_0= \frac{{d_{{внутр}}+D_{{внешн}}}}2$ – диаметр окружности центров шарика ($d_{{внутр}}$ и $D_{{внешн}}$ – внутренний и внешний диаметры подшипника соответственно);

$d_ш$ – диаметр шариков;

$F_r$ – радиальная нагрузка на валу (осевая нагрузка в подшипнике возникает при зацеплении косозубых колес, для данного расчета $F_a=0$)

Таблица подшипников:

| № вала | Марка подшипника | $d_{{подш}}, \ мм$  | $D_{{подш}}, \ мм$  | $D_0 = \frac{{d_{{внутр}} + D_{{внешн}}}}{{2}}, \ мм$ | $d_{{ш}}, \ мм$ |
| ---    | ---              | ---                 | ---                 | ---                                                   | --- |
| II     | TODO             | {d_(подшII)}        | {D_(подшII)}        | {D_(0II)}                                             | {d_(шII)} |
| III    | TODO             | {d_(подшIII)}       | {D_(подшIII)}       | {D_(0III)}                                            | {d_(шIII)} |

Таблица 3. Параметры подшипников.

Проведем расчеты для всех валов:
$$
$$

$$
$$

Таким образом, определим рассчитанное КПД подшипников по формуле:
$$
$$

где $M$, $M_{{подш}}$ – моменты на валу и подшипнике соответственно

$$
$$

$$
$$

## 8.2. Проверка опор по грузоподъёмности.

Определим тип подшипника исходя из условий его режима работы. Обычно
различают 2 режима работы подшипников качения:

1. Режим работы со статической нагрузкой при частоте вращения вала:
$n \le 1 \frac{{об}}{{мин}}$

2. Режим работы с динамической нагрузкой при частоте вращения вала:
$n > 1 \frac{{об}}{{мин}}$

Из паспорта двигателя видим $n_{{дв}} = {n_(вд)}$, следовательно, расчет произведём по 2 режиму работы

Основное условие:
$$
$$

$C$ – Динамическая грузоподъёмность подшипника

Из проектного расчёта:

$C_{{II}} = {C_(II)} \ (Н)$

$C_{{III}} = {C_(III)} \ (Н)$

Аналитически динамическая грузоподъёмность определяется следующим
образом:
$$
$$

где $L_h$ -- долговечность в часах;

$n$ -- частота вращения, $\frac{{об}}{{мин}}$; 

$P$ -- эквивалентная динамическая нагрузка, Н.

Эквивалентная динамическая нагрузка определяется по формуле:
если $\frac{{F_a}}{{V \cdot F_r}} \le e$:
$$
$$

Если же $\frac{{F_a}}{{V \cdot F_r}} > e$:
$$
$$

где $e = {e}$

$V$ -- коэффициент, учитывающий какое из колец вращается:

$V = 1.2$ если вращается наружнее;

$V = 1$ если вращается внутреннее.

$k_T$ -- коэффициент, учитывающий рабочую температуру ш/п;

$k_{{\sigma}}$ -- коэффициент безопасности.

$$
$$

$\tg \beta = 0$ (т.к. все передачи прямозубые), следовательно:
$$
$$
$$
$$

А значит:
$$
$$
$$
$$

Тогда
$$
$$
$$
$$

Тогда эквивалентная динамическая нагрузка равна:
$$
$$
$$
$$

А динамическая грузоподъёмность равна:
$$
$$
$$
$$

Проверка:
$$
$$
$$
$$

**Верно**.

## 8.3. Проверка опор по ресурсу.

Рассчитаем базовый ресурс:
$$
$$

где $L_{{10}}$ -- базовый рассчётный ресурс, обороты;

$C$ -- динамическая грузоподъёмность, Ньютоны,

$P_r$ -- эквивалентная динамическая нагрузка, Ньютоны

$$
$$
$$
$$

Чтобы перевести обороты в часы:
$$
$$
$$
$$

Проверка:

$$
$$
$$
$$

**Верно**.

## 8.4. Определение КПД зубчатых передач.

КПД цилиндрических прямозубых передач внешнего зацепления:
$$
$$

где $\varepsilon_\nu = {varepsilon_(nu)}$ – коэффициент перекрытия;

$f_{{тр}} = f_(тр)$ – коэффициент трения для колеса из закаленной стали;

$C=\frac{{F+2.92}}{{F+0.174}}$ – коэффициент нагрузки;

$F=\frac{{2 \cdot M_{{i+1}}}}{{d_{{i+1}}}}$ – окружная сила, H. 

Если  $F>30 \ H$, то $C=1$.

$$
$$
$$
$$

$$
$$
$$
$$

$$
$$
$$
$$

**Вывод: Условия проверки выполняются, а значит расчет произведен правильно.**

## 8.5. Проверка условий редких пусков.

Проведем проверку выполнения условий для кратковременного режима работы при редких пусках:
$$
$$

$$
$$

Где $M_{{д.пр}}' = J_{{пр}} \cdot \varepsilon$ — динамический приведенный момент;

$M_{{с.пр}}'$ —  статический приведенный момент;

$J_{{пр}}$ — приведенный к валу двигателя момент инерции ЭМП

$$
$$

$$
$$

$$
$$

Моменты на шестернях можно рассчитать по формуле:
$$
$$

Где $М_{{ведущ}}$ - момент ведущего колеса;

$М_{{ведом}}$ - момент ведомого колеса;

$i_{{k}}$ – передаточное отношение передачи;

$\eta_{{k}}$ – КПД передачи;

$\eta_{{подш}}$ – КПД подшипника;

$J_k$ – момент инерции ЗК;

$\varepsilon_k = \varepsilon_н \prod_{{j=1}}^k i_{{j,j+1}}$ – ускорение передачи ($\varepsilon_н$ – ускорение нагрузки)

Момент инерции ЗК можно найти по формуле:
$$
$$

Где $b_k$ – ширина ЗК;

$d_k$ – делительный диаметр ЗК;

$\rho_k$ – плотность материала ЗК;

Проведем расчеты:
$$
$$
$$
$$
$$
$$
$$
$$


$$
$$
$$
$$
$$
$$


$$
$$

$$
$$

$$
$$

$$
$$

$$
$$

Проверка:
$$
$$
$$
$$

# 9. Проверочный расчёт вала на прочность.

$$
$$

$$
$$

$$
$$

$$
$$

Для заданного материала вала -- стали 40х:
$$
$$

## 9.1. Вал II:

$L_{{II 1}} = {L_(II1)} \ мм$,

$L_{{II 2}} = {L_(II2)} \ мм$,

$L_{{II 3}} = {L_(II3)} \ мм$

Расчёт окружных и радиальных сил:

**TODO вставить картинку рад**

Рисунок 4. TODO.

**TODO вставить картинку окр**

Рисунок 5. TODO.

### 9.1.1. Первый участок $x_1 \in [0, {L_(II1)})$
Поперечная сила $Q$:
$$
$$
$$
$$

Значения $Q$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

Изгибающий момент $M_{{изг}}$:
$$
$$
$$
$$

Значения $M_{{изг}}$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

### 9.1.2. Второй участок $x_1 \in [{L_(II1)}, {L_(II1)}+{L_(II2)})$
Поперечная сила $Q$:
$$
$$
$$
$$

Значения $Q$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

Изгибающий момент $M_{{изг}}$:
$$
$$
$$
$$

Значения $M_{{изг}}$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

### 9.1.3. Третий участок $x_1 \in [{L_(II1)}+{L_(II2)}, {L_(II1)}+{L_(II2)}+{L_(II3)}]$
Поперечная сила $Q$:
$$
$$
$$
$$

Значения $Q$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

Изгибающий момент $M_{{изг}}$:
$$
$$
$$
$$

Значения $M_{{изг}}$ на краях участка:
$$
$$
$$
$$
$$
$$
$$
$$

### 9.1.4. Проверка диаметров. 

Наиболее опасное сечение (на $x = 29.5$):
$$
$$
$$
$$

Диаметры вала и цапфы:
$$
$$
$$
$$

Проверка:
$$
$$
$$
$$

## 9.2. Вал III:

$L_{{III 1}} = {L_(III1)} \ мм$,

$L_{{III 2}} = {L_(III2)} \ мм$,

$L_{{III 3}} = {L_(III3)} \ мм$

Расчёт окружных и радиальных сил:

**TODO вставить картинку**

Рисунок 5. TODO.

### 9.2.1. Первый участок $x_1 \in [0, 8.9)$
### 9.2.2. Второй участок $x_1 \in [8.9, 29.5)$
### 9.2.3. Третий участок $x_1 \in [29.5, 33.5]$

**Вывод: Проверочный расчёт на прочность валов показал правильность
выбора диаметров валов и цапф, а также соответствующих
коэффициентов запаса.**

# 10. Проверочный расчёт вала на жёсткость.

Условия прогиба валов будем определять с помощью метода
Верещагина. Для этого существующие эпюры на разных валах дополним
эпюрами от единичной силы, приложенной в максимально нагруженной
точке:
$$
$$

где $M_{{F}}$ -- площадь по эпюре $M_{{изг}}$ в $yOz$ и $xOz$ координатах,

$M_{{1}}$ -- одината по центру тяжести площади фигуры,

$E = {E} \ МПа$ - подуль упругости первого рода для стали,

$J_{{p}}$ - полярный момент инерции сечения.

$$
$$
$$
$$

где $[\delta]$ -- предельно допустимая величина прогиба, обычно:

$$
$$

где $L$ -- расстояние между опорами и зубчатыми колёсами на валу

## 10.1. Вал II.

При приложении единичной силы:

**TODO картинка окружных сил с делением на фигуры**

**TODO картинка радиальных сил с делением на фигуры**

**TODO картинка единичной нагрузки**

$$
$$

$$
$$
$$
$$

откуда:
$$
$$

$$
$$
$$
$$

откуда:
$$
$$

Поскольку реакции опор и место приложения силы при единичной нагрузке совпадают в обоих сечениях, сделаем расчёт только для одного случая.

### 10.1.1. Первый участок $x_1 \in [0, {L_(II1)}+{L_(II2)})$

Поперечная сила $Q$:
$$
$$

Значения $Q$ на краях участка:
$$
$$
$$
$$

Изгибающий момент $M_{{изг}}$:
$$
$$

Значения $M_{{изг}}$ на краях участка:
$$
$$
$$
$$

### 10.1.2. Второй участок $x_1 \in [{L_(II1)}+{L_(II2)}, {L_(II1)}+{L_(II2)}+{L_(II3)}]$

Поперечная сила $Q$:
$$
$$

Значения $Q$ на краях участка:
$$
$$
$$
$$

Изгибающий момент $M_{{изг}}$:
$$
$$

Значения $M_{{изг}}$ на краях участка:
$$
$$
$$
$$

### 10.1.3. Расчёт прогиба вала.

Определим площади фигур для окружных моментов:
$$
$$
$$
$$
$$
$$
$$
$$

Определим площади фигур для радиальных моментов:
$$
$$
$$
$$
$$
$$
$$
$$

Абсциссы центров тяжести моментов одинаковы для обоих сечений:
$$
$$
$$
$$
$$
$$
$$
$$

Тогда значение изгибающего момента от единичной силы в точках центров тяжести:
$$
$$
$$
$$
$$
$$
$$
$$

Прогибы для плоскостей $yOz$ и $xOz$:
$$
$$
$$
$$

Суммарный изгиб:
$$
$$
$$
$$

Проверка:
$$
$$


**Вывод: Проверочный расчёт на жёсткость валов верен, что
говорит о правильности выбора диаметров и материалов для
этих конструкций. В ходе эксплуатации валы будут работать
нормально.**

# 11. Расчёт на быстродействие.

Для ЭП с двигателями постоянного тока время разгона определяется по формуле:
$$
$$

где $T_{{ЭМ}}$ – электромеханическая постоянная:
$$
$$

где $\omega_{{н}}$ — номинальная скорость вращения двигателя;

$M_{{пуск}}$ -- пусковой момент двигателя;

$M_{{с.пр.}}$ -- статический момент нагрузки, приведенный к валу двигателя;

$J_{{пр}}$ -- приведенный к валу двигателя момент инерции ЭП:
$$
$$

где $J_р$ –- момент инерции ротора двигателя;

$J_н$ –- момент инерции нагрузки;

$i_0$ -– общее передаточное отношение редуктора;

$J_{{р.пр.}}$ –- приведенный к валу двигателя момент инерции редуктора:
$$
$$

$$
$$

$$
$$

**Выводы:  быстродействие редуктора велико.**

# 12. Проверочный расчёт на контактную прочность.

Максимальные расчетные контактные напряжения должны быть
меньше предельно допустимых:
$$
$$

Контактные напряжения в зубчатой передаче определятся выражением:
$$
$$

где $b_{{зк}}$ -- ширина ведомого зубчатого колеса;

$i_{{j}}$ -- передаточное отношение;

$a_{{\omega j}}$ -- межосевое расстояние;

$K_{{комп}}$ -- коэффициент компенсации неточности моментов, задается из
допущений, $K_{{комп}} = 1.3..1.5$,  примем $K_{{комп}} = {K_(комп)}$;

$\zeta_H$ -- коэффициент, учитывающий форму соприкасающихся поверхностей,
при $\alpha = {alpha}$:
$$
$$

$\zeta_M$ -- коэффициент, учитывающий механические свойства материалов
колес.

$$
$$

где $\nu$ -- коэффициент Пуассона, выбирается по таблице, для стали $\nu = 0.3$;
Для стальных колес $\zeta_M = {zeta_(M)}$

$\zeta_{{\xi}}$ – коэффициент, учитывающий влияние торцевого перекрытия зубьев, примем равным {zeta_(xi)};

$$
$$
$$
$$

Проверка:
$$
$$
$$
$$

**Выводы:
Контактная прочность на всех звеньях ЭМП не превышает предельные
значения для параметров конструкции**

# 13. Проверочный расчёт на прочность при кратковременных перегрузках.

Статическая прочность зубьев при перегрузках моментом $M$
проверяется по условию:
$$
$$
$$
$$

где $K_{{пер}}$ -- коэффициент перегрузки;

$\sigma_H$ -- максимальные расчетные контактные напряжение при циклическом нагружении;

$\sigma_{{изг}}$ -- максимальные расчетные изгибные напряжение при циклическом нагружении, определяется по формуле:
$$
$$

где $M_{{вала}}$ -- момент на валу;

$Y_{{Fj}}$ -- коэффициент формы зуба для прямозубых цилиндрических колёс;

$K_{{изг}}$ -- коэффициент запаса, примем $K_{{изг}} = {K_(игз)}$;

$m_{{j}}$ -- модуль передачи;

$z_{{зк}}$ -- число зубьев ведомого зубчатого колеса;

$\psi_{{m}}$ -- коэффициент ширины зубчатого венца для мелкомодульных передач, $\psi_m = {psi_(m)}$;

$[\sigma_{{H max}}]$ -- предельно допустимые контактные напряжения при кратковременных перегрузках;

$[\sigma_{{изг max}}]$ -- предельно допустимые изгибные напряжения при кратковременных перегрузках;

Коэффициент перегрузки рассчитывается по формуле:
$$
$$

где $M_{{пуск}}$ -- пусковой момент двигателя;

$M_{{I}}$ -- суммарный момент нагрузки, приведенный к валу двигателя.

Для прирабатываемых зубчатых колес:
$$
$$
$$
$$

где $\sigma_т$ -- предел текучести материала зубчатого колеса.

$$
$$
$$
$$

$$
$$
$$
$$

Проверка:
$$
$$
$$
$$

$$
$$
$$
$$

Проверка:
$$
$$
$$
$$

**Выводы:
Рассчитанная система сможет выдержать кратковременные
перегрузки, следовательно, расчет был произведен верно и, как
следствие, мы имеем достаточный запас по допустимым напряжениям.**

# 14. Общие выводы.

1. По итогам проверки на точность оказалось, что общая погрешность положения выходного вала не удовлетворяет заданной в ТЗ. Основной вклад в общую погрешность вносит погрешность мертвого хода, которую можно уменьшить путем выбора другого разбиения передаточного отношения с целью уменьшения диаметров ведомых колес, либо выбрав другой вид сопряжения и повысив степень точность, либо используя безлюфтовые зубчатые колеса на выходном валу редуктора.
2. По результатам проверочного силового расчета выбранный двигатель удовлетворяет условию для режима редких пусков работы.
3. Быстродействие редуктора велико.
4. Контактная прочность зубчатых колёс удовлетворяет критерию проверки.
5. Контактная прочность при перегрузках не удовлетворяет условиям. Для удовлетворения необходимо брать двигтаель с меньшим пусковым моментом, увеличить момент на первом вале, увеличить ширину и модуль зубчатых колёс или изменить передаточное число.

# 15. Список литературы.

1. Кокорев Ю.А., Жаров В.А., Торгов А.М. Расчет электромеханического привода. Изд-во МГТУ, 1995, 132 с.
2. ГОСТ 21098-82.
3. ГОСТ 1643-81.

$$
$$
$$
$$
