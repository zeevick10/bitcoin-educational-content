---
name: Remix - Whirlpool
description: Сколько ремиксов следует выполнить в Whirlpool?
---
![cover remix- wp](assets/cover.webp)

***ВНИМАНИЕ:** После ареста основателей кошелька Samourai и изъятия их серверов 24 апреля, инструмент Whirlpool Stats Tool больше недоступен для скачивания, так как он был размещен на Gitlab Samourai. Даже если вы ранее скачали этот инструмент на свой компьютер или он был установлен на вашем узле RoninDojo, WST в настоящее время не будет функционировать. Его работа зависела от данных, предоставляемых сайтом OXT.me, который теперь недоступен. В настоящее время WST не особенно полезен, поскольку протокол Whirlpool неактивен. Тем не менее, возможно, что эти программы могут быть восстановлены в ближайшие недели. Кроме того, теоретическая часть этой статьи остается актуальной для понимания принципов и целей coinjoins в целом (не только Whirlpool), а также для понимания эффективности модели Whirlpool. Вы также можете узнать, как количественно оценить конфиденциальность, предоставляемую циклами coinjoin.*

_Мы тщательно следим за развитием этого дела, а также за развитием связанных с ним инструментов. Будьте уверены, что мы обновим этот учебник, как только появится новая информация._

_Этот учебник предоставляется только для образовательных и информационных целей. Мы не поддерживаем и не поощряем использование этих инструментов в преступных целях. Каждый пользователь несет ответственность за соблюдение законов в своей юрисдикции._

---

> *"Разорвите связь, которую оставляют за собой ваши монеты"*

Это вопрос, который мне часто задают. **Сколько ремиксов следует выполнить при использовании Whirlpool, чтобы достичь удовлетворительных результатов?**

Цель coinjoin заключается в предоставлении вероятной отрицаемости путем смешивания вашей монеты с группой неразличимых монет. Цель этого действия - разорвать связи трассировки, как из прошлого в настоящее, так и из настоящего в прошлое. Другими словами, аналитик, знающий вашу исходную транзакцию на входе циклов coinjoin, не должен иметь возможности однозначно идентифицировать ваш UTXO на выходе из циклов ремикса (анализ с входных циклов на выходные циклы).
![past-present links diagram](assets/en/1.webp)

В свою очередь, аналитик, знающий ваш UTXO на выходе из циклов coinjoin, не должен иметь возможности определить исходную транзакцию на входе циклов (анализ с выходных циклов на входные циклы).
![present-past links diagram](assets/en/2.webp)
Однако количество ремиксов не является надежным критерием для оценки сложности, с которой аналитик столкнется при установлении связей между прошлым и настоящим или наоборот. Более релевантным показателем будет размер групп, в которых скрывается ваша монета. Эти показатели называются "anonsets". В случае с Whirlpool существует два типа anonsets.

Во-первых, мы можем определить размер группы, в которой ваш UTXO скрыт на выходе из циклов coinjoin, то есть количество неразличимых монет, присутствующих в этой группе.
![probable UTXOs at exit](assets/en/3.webp)
Этот индикатор, называемый на французском "prospective anonset", на английском "forward anonset" или "перспективные метрики", позволяет нам оценить устойчивость вашей монеты к анализам, отслеживающим ее путь от входа до выхода из циклов coinjoin. Эта метрика оценивает степень защиты вашего UTXO от попыток реконструкции его истории от точки входа до точки выхода в процессе coinjoin. Например, если ваша транзакция участвовала в своем первом цикле coinjoin и было выполнено два дополнительных последующих цикла, перспективный anonset вашей монеты будет `13`: ![forward anonset](assets/en/4.webp)
Во-вторых, другой индикатор может быть рассчитан для оценки устойчивости вашей монеты к анализу от настоящего к прошлому. Зная ваш UTXO в конце циклов, этот индикатор определяет количество потенциальных транзакций Tx0, которые могли бы составить ваш вход в циклах coinjoin (анализ с конца к началу циклов). Этот индикатор измеряет, насколько сложно аналитику проследить происхождение вашей монеты после ее прохождения через coinjoins. ![Probable sources at input](assets/en/5.webp)
Название этого индикатора - "backward anonset" или "ретроспективные метрики". На французском мне нравится называть его "anonset rétrospectif". На диаграмме ниже это соответствует всем оранжевым пузырям Tx0:
![backward anonset](assets/en/6.webp)
Чтобы узнать больше о методе расчета этих индикаторов, я рекомендую прочитать [мою тему в Twitter](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) по этому вопросу. Мы также готовим более подробную статью о сети PlanB.

Я понимаю, что предоставленный ответ может показаться неудовлетворительным, поскольку вы надеялись получить конкретное количество ремиксов, и я направляю вас к документации. Причина этого в том, что количество ремиксов является ненадежным индикатором для оценки полученной анонимности в циклах coinjoin. Поэтому невозможно определить фиксированное количество ремиксов как абсолютный и универсальный порог безопасности.

Действительно, каждый дополнительный ремикс вашей монеты увеличивает ее наборы анонимности. Однако важно понимать, что в первую очередь к росту вашего перспективного anonset приводят ремиксы, выполненные вашими пирами. С моделью Whirlpool ваша транзакция может достичь значительных уровней перспективного anonset всего лишь с двумя или тремя циклами coinjoin, исключительно благодаря деятельности участников предыдущих coinjoins.

С другой стороны, ретроспективный anonset в нашем случае не вызывает беспокойства. Фактически, начиная с вашего первоначального coinjoin, вы получаете наследие предыдущих транзакций в пуле, сразу же придавая вашей монете высокий backward anonset, с маргинальным увеличением в каждом последующем цикле.
Также важно понимать, что создание правдоподобного отрицания никогда не бывает завершенным. Это зависит от вероятности отслеживания ваших монет. Эта вероятность уменьшается по мере увеличения размера групп, скрывающих их. Поэтому вам следует корректировать свои цели в терминах анонимных наборов в соответствии с вашими личными ожиданиями. Спросите себя о причинах, которые побудили вас использовать coinjoins и уровни анонимности, необходимые для достижения этих целей. Например, если использование coinjoins направлено просто на сохранение конфиденциальности вашего кошелька при отправке нескольких сатоши вашему крестнику на день рождения, очень высокие уровни анонимности не нужны. Ваш крестник, вероятно, не сможет провести глубокий анализ цепочки, и даже если бы смог, последствия для вашей жизни не были бы катастрофическими. Однако, если вы являетесь целью авторитарного режима, где малейшая информация может привести к заключению под стражу, ваши действия должны руководствоваться гораздо более строгими критериями.
Чтобы определить эти знаменитые индикаторы анонимного набора, вы можете использовать инструмент на Python под названием **WST** (Whirlpool Stats Tool).

Однако не всегда необходимо вычислять анонимные наборы каждой из ваших монет, объединенных с помощью coinjoin. Дизайн Whirlpool сам по себе уже предоставляет вам гарантии. Как было сказано ранее, ретроспективный анонимный набор редко бывает предметом беспокойства. С вашего первоначального смешивания вы уже получаете особенно высокий ретроспективный балл. Что касается перспективного анонимного набора, вам просто нужно держать вашу монету на послесмешиваемом счете достаточно долгое время. Например, вот баллы анонимного набора одной из моих монет `100,000 сатоши` после проведения двух месяцев в пуле coinjoin:
![WST anonsets](assets/en/7.webp)
Это показывает ретроспективный балл `34,593` и перспективный балл `45,202`. Конкретно это означает две вещи:
- Если аналитик знает мою монету в конце циклов и пытается проследить ее происхождение, он столкнется с `34,593` потенциальными источниками, каждый из которых с равной вероятностью может быть моим.
- Если аналитик знает мою монету в начале циклов и пытается определить ее соответствие в конце, он столкнется с `45,202` возможными UTXO, каждый из которых с той же вероятностью может быть моим.
Вот почему я считаю использование Whirlpool особенно актуальным в стратегии `Hodl -> Mix -> Spend -> Replace`. На мой взгляд, наиболее логичный подход - держать большую часть сбережений в биткоинах в холодном кошельке, одновременно постоянно поддерживая определенное количество монет в coinjoin на Samourai для покрытия повседневных расходов. Как только биткоины из coinjoins потрачены, они заменяются на новые, чтобы вернуться к определенному порогу смешанных монет. Этот метод позволяет нам освободиться от беспокойства о анонимных наборах наших UTXO, делая время, необходимое для эффективности coinjoins, гораздо менее ограничивающим.

Я надеюсь, что этот ответ прояснил модель Whirlpool. Если вы хотите узнать больше о том, как работают coinjoins на Bitcoin, я рекомендую прочитать мою подробную статью на эту тему: 
https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Внешние ресурсы:**
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
Как квалифицированный профессиональный переводчик, ваша основная задача - точно переводить технический контент из английского на ваш родной язык, русский. Пожалуйста, следуйте следующим рекомендациям, чтобы обеспечить высокое качество перевода:

Исходный язык: Контент изначально на английском.
Характер контента: Вы столкнетесь с техническим материалом, потенциально включая специфическую отраслевую терминологию.
Ссылки и технические термины: Не переводите URL-адреса или высокоспециализированные технические термины. В случае сомнений сохраняйте оригинальный термин.
Сохранение форматирования: Сохраняйте тот же макет и форматирование markdown, что и в оригинальном тексте. Сохранение структуры крайне важно.
Свойства YML: Если строка начинается со свойства YAML (например, 'name:', 'goal:', 'objectives:'), сохраните название свойства на английском языке.
Культурный контекст: Для культурных или контекстно-специфических ссылок, которые могут не иметь прямого перевода, перефразируйте, чтобы сохранить предполагаемый смысл или предоставьте краткое объяснение.
Акцент должен быть сделан на сохранении целостности технического контента, при этом обеспечивая, чтобы перевод был понятным и контекстуально точным на русском.