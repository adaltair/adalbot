import telebot

API_KEY = "6229234842:AAFFPRQjrIxElWYP3DRNVive3B12sA_KP9c"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet(message):
  bot.reply_to(message, "Ассаламуғайлейкум! Е қоспасының реттік нөмірін жазыңыз. Мысалы, 171 немесе 160b")

@bot.message_handler(content_types=['text'])
def handle_message(message):
  if message.text == "120":
    bot.reply_to(message, "Харам \nКармин Е-120")
  elif message.text == "150":
    bot.reply_to(message, "Халал \nҚантты колер Е-150")
  elif message.text == "160b":
    bot.reply_to(message, "Халал \nЭкстракт аннато Е-160b")
  elif message.text == "171":
    bot.reply_to(message, "Халал \nДиоксид титана Е-171")
  elif message.text == "172":
    bot.reply_to(message, "Халал \nТемір оксиді мен гидроксиді Е-172")
  elif message.text == "173":
    bot.reply_to(message, "Халал \nАлюминий Е-173")
  elif message.text == "174":
    bot.reply_to(message, "Халал \nКүміс Е-174")
  elif message.text == "175":
    bot.reply_to(message, "Халал \nАлтын Е-175")
  elif message.text == "200":
    bot.reply_to(message, "Халал \nСорбин қышқылы Е-200")
  elif message.text == "201":
    bot.reply_to(message, "Халал \nНатрий сорбаты Е-201")
  elif message.text == "202":
    bot.reply_to(message, "Халал \nКалий сорбаты Е-202")
  elif message.text == "203":
    bot.reply_to(message, "Халал \nСорбат кальциі Е-203")

  elif message.text == "210":
    bot.reply_to(message, "Халал \nБензойлы қышқыл Е-210")

  elif message.text == "211":
    bot.reply_to(message, "Халал \nБензоат натрийі Е-211")

  elif message.text == "212":
    bot.reply_to(message, "Халал \nБензоат калийі Е-212")

  elif message.text == "220":
    bot.reply_to(message, "Халал \nСер диоксиді Е-220")

  elif message.text == "221":
    bot.reply_to(message, "Халал \nНатрий сульфиті Е-221")

  elif message.text == "222":
    bot.reply_to(message, "Халал \nНатрий гидросульфит Е-222")

  elif message.text == "223":
    bot.reply_to(message, "Халал \nНатрий пиросульфит Е-223")

  elif message.text == "224":
    bot.reply_to(message, "Халал \nКалий пиросульфит Е-224")

  elif message.text == "226":
    bot.reply_to(message, "Халал \nСульфит кальция Е-226")

  elif message.text == "239":
    bot.reply_to(message, "Халал \nГексамин Е-239")

  elif message.text == "249":
    bot.reply_to(message, "Халал \nКалий нитриті Е-249")

  elif message.text == "250":
    bot.reply_to(message, "Халал \nНатрий нитриті Е-250")

  elif message.text == "251":
    bot.reply_to(message, "Халал \nНатрий нитраты Е-251")

  elif message.text == "252":
    bot.reply_to(message, "Халал \nКалий нитраты Е-252")

  elif message.text == "260":
    bot.reply_to(message, "Халал \nУксус қышқылы Е-260")

  elif message.text == "261":
    bot.reply_to(message, "Халал \nКалий ацетаты Е-261")

  elif message.text == "263":
    bot.reply_to(message, "Халал \nКальций ацетаты Е-263")

  elif message.text == "280":
    bot.reply_to(message, "Халал \nПропинді қышқыл Е-280")

  elif message.text == "281":
    bot.reply_to(message, "Халал \nНатрий пропинаты Е-281")

  elif message.text == "283":
    bot.reply_to(message, "Халал \nКалий пропинаты Е-283")

  elif message.text == "290":
    bot.reply_to(message, "Халал \nКөмір диоксиді Е-290")

  elif message.text == "300":
    bot.reply_to(message, "Халал \nАскорбин қышқылы (Витамин C) Е-300")

  elif message.text == "301":
    bot.reply_to(message, "Халал \nНатрий аскорбаты Е-301")

  elif message.text == "310":
    bot.reply_to(message, "Халал \nПропилгаллат Е-301")

  elif message.text == "330":
    bot.reply_to(message, "Халал \nЛимон қышқылы Е-330")

  elif message.text == "331":
    bot.reply_to(message, "Халал \nНатрий цитраты Е-331")

  elif message.text == "332":
    bot.reply_to(message, "Халал \nКалий цитраты Е-332")

  elif message.text == "338":
    bot.reply_to(message, "Халал \nОртофосфор қышқылы Е-338")

  elif message.text == "339":
    bot.reply_to(message, "Халал \nНатрий ортофосфаты Е-339")

  elif message.text == "340":
    bot.reply_to(message, "Халал \nКалий ортофосфаты Е-340")

  elif message.text == "400":
    bot.reply_to(message, "Халал \nАльгин қышқылы Е-400")

  elif message.text == "401":
    bot.reply_to(message, "Халал \nАльгинат натрийі Е-401")

  elif message.text == "402":
    bot.reply_to(message, "Халал \nАльгинат калийі Е-402")

  elif message.text == "403":
    bot.reply_to(message, "Халал \nАльгинат аммонийі Е-403")

  elif message.text == "405":
    bot.reply_to(message, "Халал \nАльгинат пропиленгликольі Е-405")

  elif message.text == "406":
    bot.reply_to(message, "Халал \nАгар Е-406")

  elif message.text == "407":
    bot.reply_to(message, "Халал \nКаррагинан Е-407")

  elif message.text == "410":
    bot.reply_to(message, "Халал \nШегіртке бұршақ камедьі Е-410")

  elif message.text == "412":
    bot.reply_to(message, "Халал \nГуар камедьі Е-412")

  elif message.text == "413":
    bot.reply_to(message, "Халал \nТрагакант камедьі Е-413")

  elif message.text == "414":
    bot.reply_to(message, "Халал \nГуммиарабик Е-414")

  elif message.text == "415":
    bot.reply_to(message, "Халал \nКсантан камедьі Е-415")

  elif message.text == "420":
    bot.reply_to(message, "Халал \nСорбит Е-420")

  elif message.text == "421":
    bot.reply_to(message, "Халал \nМаннит Е-421")

  elif message.text == "440a":
    bot.reply_to(message, "Халал \nПектин Е-440a")

  elif message.text == "440b":
    bot.reply_to(message, "Халал \nАмидирлі пектин Е-440b")

  elif message.text == "450a" or message.text == "450b" or message.text == "450c":
    bot.reply_to(message, "Халал \nКалий және натрийдің фосфаты және полифосфаты Е-450")

  elif message.text == "460":
    bot.reply_to(message, "Халал \nЦеллюлоза Е-460")

  elif message.text == "461":
    bot.reply_to(message, "Халал \nМетилцеллюлоза Е-461")

  elif message.text == "463":
    bot.reply_to(message, "Халал \nГидроксипропилцелюлозa Е-463")

  elif message.text == "464":
    bot.reply_to(message, "Халал \nГидроксипропилметилцеллюлоза Е-464")

  elif message.text == "465":
    bot.reply_to(message, "Халал \nМетилэтилцеллюлоза Е-465")

  elif message.text == "466":
    bot.reply_to(message, "Халал \nНатрий-карбоксиметилцеллюлоза Е-466")

  elif message.text == "234":
    bot.reply_to(message, "Халал \nНизин Е-234")

  elif message.text == "262":
    bot.reply_to(message, "Халал \nНатрий ацетаты Е-262")

  elif message.text == "296":
    bot.reply_to(message, "Халал \nАлма қышқылы Е-296")

  elif message.text == "297":
    bot.reply_to(message, "Халал \nФумар қышқылы Е-297")

  elif message.text == "350":
    bot.reply_to(message, "Халал \nНатрий малаты Е-350")

  elif message.text == "351":
    bot.reply_to(message, "Халал \nКалий малаты Е-351")

  elif message.text == "352":
    bot.reply_to(message, "Халал \nКальций малаты Е-352")

  elif message.text == "353":
    bot.reply_to(message, "Халал \nМета-винді қышқыл Е-353")

  elif message.text == "355":
    bot.reply_to(message, "Халал \nАдипин қышқылы Е-355")

  elif message.text == "363":
    bot.reply_to(message, "Халал \nЯнтарь қышқылы Е-363")

  elif message.text == "370":
    bot.reply_to(message, "Халал \nГептонолактон Е-370")

  elif message.text == "375":
    bot.reply_to(message, "Халал \nНикотин қышқылы Е-375")

  elif message.text == "380":
    bot.reply_to(message, "Халал \nЦитрат аммонийі Е-380")

  elif message.text == "381":
    bot.reply_to(message, "Халал \nАммоний темірінің цитраты Е-381")

  elif message.text == "385":
    bot.reply_to(message, "Халал \nКальций динатрий тұзы Е-385")

  elif message.text == "416":
    bot.reply_to(message, "Халал \nКарайи камедьі Е-416")

  elif message.text == "500":
    bot.reply_to(message, "Халал \nНатрий карбонаты және бикарбонаты Е-500")

  elif message.text == "501":
    bot.reply_to(message, "Халал \nКалий карбонаты және бикарбонаты Е-501")

  elif message.text == "503":
    bot.reply_to(message, "Халал \nАммоний карбонаты Е-503")

  elif message.text == "504":
    bot.reply_to(message, "Халал \nМагний карбонат Е-504")

  elif message.text == "507":
    bot.reply_to(message, "Халал \nТұз қышқылы Е-507")

  elif message.text == "508":
    bot.reply_to(message, "Халал \nКалий хлориді Е-508")

  elif message.text == "509":
    bot.reply_to(message, "Халал \nКальций хлориді Е-509")

  elif message.text == "510":
    bot.reply_to(message, "Халал \nАммоний хлориді Е-510")

  elif message.text == "513":
    bot.reply_to(message, "Халал \nКүкірт қышқылы Е-513")

  elif message.text == "514":
    bot.reply_to(message, "Халал \nНатрий сульфаты Е-514")

  elif message.text == "515":
    bot.reply_to(message, "Халал \nКалий сульфаты Е-515")

  elif message.text == "516":
    bot.reply_to(message, "Халал \nКальций сульфаты Е-516")

  elif message.text == "518":
    bot.reply_to(message, "Халал \nМагний сульфаты Е-518")

  elif message.text == "524":
    bot.reply_to(message, "Халал \nНатрий гидроксиді Е-524")

  elif message.text == "525":
    bot.reply_to(message, "Халал \nКалий гидроксиді Е-525")

  elif message.text == "526":
    bot.reply_to(message, "Халал \nКальций гидроксиді Е-526")

  elif message.text == "527":
    bot.reply_to(message, "Халал \nАммний гидроксиді Е-527")

  elif message.text == "528":
    bot.reply_to(message, "Халал \nМагний гидроксиді Е-528")

  elif message.text == "529":
    bot.reply_to(message, "Халал \nКальций оксиді Е-529")

  elif message.text == "530":
    bot.reply_to(message, "Халал \nМагний оксиді Е-530")

  elif message.text == "535":
    bot.reply_to(message, "Халал \nНатрий ферроцианиді Е-535")

  elif message.text == "536":
    bot.reply_to(message, "Халал \nКалий ферроцианиді Е-536")

  elif message.text == "540":
    bot.reply_to(message, "Халал \nДикальций дифосфаты Е-540")

  elif message.text == "541":
    bot.reply_to(message, "Халал \nАлюмофосфат натрийі Е-541")

  elif message.text == "545":
    bot.reply_to(message, "Халал \nПолифосфат аммонийі Е-545")

  elif message.text == "551":
    bot.reply_to(message, "Халал \nКремний диоксид Е-551")

  elif message.text == "552":
    bot.reply_to(message, "Халал \nКальций силикаты Е-552")

  elif message.text == "553":
    bot.reply_to(message, "Халал \nМагний силикаты, магний трисиликаты Е-553")

  elif message.text == "554":
    bot.reply_to(message, "Халал \nНатрий алюмосиликаты Е-554")

  elif message.text == "558":
    bot.reply_to(message, "Халал \nБентонит Е-558")

  elif message.text == "559":
    bot.reply_to(message, "Халал \nКаолин Е-559")

  elif message.text == "575":
    bot.reply_to(message, "Халал \nГлюконо-d-лактон Е-575")

  elif message.text == "576":
    bot.reply_to(message, "Халал \nНатрий глюконаты Е-576")

  elif message.text == "577":
    bot.reply_to(message, "Халал \nКалий глюконаты Е-577")

  elif message.text == "578":
    bot.reply_to(message, "Халал \nКальций глюконаты Е-578")

  elif message.text == "636":
    bot.reply_to(message, "Халал \nМальтол Е-636")

  elif message.text == "637":
    bot.reply_to(message, "Халал \nЭтилмальтол Е-637")

  elif message.text == "900":
    bot.reply_to(message, "Халал \nПолидиметилсилоксан Е-900")

  elif message.text == "901":
    bot.reply_to(message, "Халал \nБалауыз Е-901")

  elif message.text == "903":
    bot.reply_to(message, "Халал \nКарнауба балауызы Е-903")

  elif message.text == "905":
    bot.reply_to(message, "Халал \nМинералды көмірсутек Е-905")

  elif message.text == "924":
    bot.reply_to(message, "Халал \nКалий броматы Е-924")

  elif message.text == "925":
    bot.reply_to(message, "Халал \nХлор Е-925")

  elif message.text == "926":
    bot.reply_to(message, "Халал \nХлор диоксиді Е-926")

  elif message.text == "927":
    bot.reply_to(message, "Халал \nАзодикарбонамид Е-927")
    
  elif message.text == "107":
    bot.reply_to(message, "Күмәнді \nЖелтый Е-107")
    
  elif message.text == "133":
    bot.reply_to(message, "Күмәнді \nБриллиантовый голубой Е-133")
    
  elif message.text == "154":
    bot.reply_to(message, "Күмәнді \nКоричневый FK Е-154")
    
  elif message.text == "495":
    bot.reply_to(message, "Күмәнді \nСорбитан монопальмитат Е-495")
    
  elif message.text == "920":
    bot.reply_to(message, "Күмәнді \nL-цистеина гидрохлорид Е-920")
    
  elif message.text == "100":
    bot.reply_to(message, "Күмәнді \nКуркумин, турмерик Е-100")
    
  elif message.text == "101":
    bot.reply_to(message, "Күмәнді \nРибофлавин (витамин B2) Е-101")
    
  elif message.text == "102":
    bot.reply_to(message, "Күмәнді \nТартразин Е-102")
    
  elif message.text == "104":
    bot.reply_to(message, "Күмәнді \nЖелтый хинолиновый Е-104")
    
  elif message.text == "110":
    bot.reply_to(message, "Күмәнді \nЖёлтый «солнечный закат» Е-110")
    
  elif message.text == "122":
    bot.reply_to(message, "Күмәнді \nКармазин Е-122")
    
  elif message.text == "123":
    bot.reply_to(message, "Күмәнді \nАмарант Е-123")
    
  elif message.text == "124":
    bot.reply_to(message, "Күмәнді \nПонсо 4R Е-124")
    
  elif message.text == "127":
    bot.reply_to(message, "Күмәнді \nЭритрозин Е-127")
    
  elif message.text == "128":
    bot.reply_to(message, "Күмәнді \nКрасный 2G Е-128")
    
  elif message.text == "131":
    bot.reply_to(message, "Күмәнді \nПантенттелген көк V Е-131")
    
  elif message.text == "132":
    bot.reply_to(message, "Күмәнді \nИндигокармин Е-132")
    
  elif message.text == "140":
    bot.reply_to(message, "Күмәнді \nХлорофилл Е-140")
    
  elif message.text == "141":
    bot.reply_to(message, "Күмәнді \nХлорофилдің мысты кешені Е-141")
    
  elif message.text == "142":
    bot.reply_to(message, "Күмәнді \nЖасыл S Е-142")
    
  elif message.text == "151":
    bot.reply_to(message, "Күмәнді \nБриллиантты BN Е-151")
    
  elif message.text == "153":
    bot.reply_to(message, "Күмәнді \nКөмір қара Е-153")
    
  elif message.text == "160a":
    bot.reply_to(message, "Күмәнді \nАльфа-, бета-, гамма- каротиндер Е-160a")
    
  elif message.text == "160c":
    bot.reply_to(message, "Күмәнді \nКапсантин, капсорубин Е-160c")
    
  elif message.text == "160d":
    bot.reply_to(message, "Күмәнді \nЛикопин Е-160d")
    
  elif message.text == "160e":
    bot.reply_to(message, "Күмәнді \nБета-апо-8-каротинді альдегид Е-160e")
    
  elif message.text == "160f":
    bot.reply_to(message, "Күмәнді \nЭтильді эфир бета-апо-8-каротинді қышқыл Е-160f")
    
  elif message.text == "161a":
    bot.reply_to(message, "Күмәнді \nФлавоксантин Е-161a")
    
  elif message.text == "161b":
    bot.reply_to(message, "Күмәнді \nЛютеин Е-161b")
    
  elif message.text == "161c":
    bot.reply_to(message, "Күмәнді \nКриптоксантин Е-161c")
    
  elif message.text == "161d":
    bot.reply_to(message, "Күмәнді \nРубиксантин Е-161d")
    
  elif message.text == "161e":
    bot.reply_to(message, "Күмәнді \nВиолоксантин Е-161e")
    
  elif message.text == "161f":
    bot.reply_to(message, "Күмәнді \nРодоксантин Е-161f")
    
  elif message.text == "161g":
    bot.reply_to(message, "Күмәнді \nКантаксантин Е-161g")
    
  elif message.text == "162":
    bot.reply_to(message, "Күмәнді \nҚызылшалы қызыл(бетанин) Е-162")
    
  elif message.text == "163":
    bot.reply_to(message, "Күмәнді \nАнтоциандар Е-163")
    
  elif message.text == "170":
    bot.reply_to(message, "Күмәнді \nКарбонат кальциі Е-170")
    
  elif message.text == "180":
    bot.reply_to(message, "Күмәнді \nРубинді литол BK Е-180")
    
  elif message.text == "213":
    bot.reply_to(message, "Күмәнді \nБензоат кальциі Е-213")
    
  elif message.text == "214":
    bot.reply_to(message, "Күмәнді \nЭтилпарабен Е-214")
    
  elif message.text == "215":
    bot.reply_to(message, "Күмәнді \nПара-гидроксибензил қышқылды этил эфирінің натри тұзы Е-215")
    
  elif message.text == "216":
    bot.reply_to(message, "Күмәнді \nПропилпарабен Е-216")
    
  elif message.text == "217":
    bot.reply_to(message, "Күмәнді \nПара-гидроксибензил қышқылды пропил эфирінің натри тұзы Е-217")
    
  elif message.text == "218":
    bot.reply_to(message, "Күмәнді \nМетилпарабен Е-218")
    
  elif message.text == "219":
    bot.reply_to(message, "Күмәнді \nПара-гидроксибензойной кислоты метилового эфира натриевая соль Е-219")
    
  elif message.text == "227":
    bot.reply_to(message, "Күмәнді \nГидросульфит кальция Е-227")
    
  elif message.text == "230":
    bot.reply_to(message, "Күмәнді \nБифенил (дифенил) Е-230")
    
  elif message.text == "231":
    bot.reply_to(message, "Күмәнді \nОртофенилфенол Е-231")
    
  elif message.text == "232":
    bot.reply_to(message, "Күмәнді \nОртофенилфенол натри тұзы Е-232")
    
  elif message.text == "233":
    bot.reply_to(message, "Күмәнді \nТиабендазол Е-233")
    
  elif message.text == "270":
    bot.reply_to(message, "Күмәнді \nСүт қышқылы Е-270")
    
  elif message.text == "282":
    bot.reply_to(message, "Күмәнді \nПропионат кальциі Е-282")
    
  elif message.text == "302":
    bot.reply_to(message, "Күмәнді \nАскорбат кальциі Е-302")
    
  elif message.text == "304":
    bot.reply_to(message, "Күмәнді \nАскорбилпальмитат Е-304")
    
  elif message.text == "306":
    bot.reply_to(message, "Күмәнді \nТокоферолдың табиғи концентраты Е-306")
    
  elif message.text == "307":
    bot.reply_to(message, "Күмәнді \nСинтетикалық альфатокоферол Е-307")
    
  elif message.text == "308":
    bot.reply_to(message, "Күмәнді \nСинтетикалық гамматокоферол Е-308")
    
  elif message.text == "309":
    bot.reply_to(message, "Күмәнді \nСинтетикалық гамматокоферол Е-309")
    
  elif message.text == "311":
    bot.reply_to(message, "Күмәнді \nОктилгаллат Е-311")
    
  elif message.text == "312":
    bot.reply_to(message, "Күмәнді \nДодецилгаллат Е-312")
    
  elif message.text == "320":
    bot.reply_to(message, "Күмәнді \nБутилгидроксианизол Е-320")
    
  elif message.text == "321":
    bot.reply_to(message, "Күмәнді \nБутилгидрокситолуол Е-321")
    
  elif message.text == "322":
    bot.reply_to(message, "Күмәнді \nЛецитин Е-322")
    
  elif message.text == "325":
    bot.reply_to(message, "Күмәнді \nЛактат натрия Е-325")
    
  elif message.text == "326":
    bot.reply_to(message, "Күмәнді \nЛактат калия Е-326")
    
  elif message.text == "327":
    bot.reply_to(message, "Күмәнді \nЛактат кальция Е-327")
    
  elif message.text == "333":
    bot.reply_to(message, "Күмәнді \nКальций цитраты Е-333")
    
  elif message.text == "334":
    bot.reply_to(message, "Күмәнді \nВино қышқылы Е-334")
    
  elif message.text == "335":
    bot.reply_to(message, "Күмәнді \nНатрий тартраты Е-335")
    
  elif message.text == "336":
    bot.reply_to(message, "Күмәнді \nКалий тартраты Е-336")
    
  elif message.text == "337":
    bot.reply_to(message, "Күмәнді \nКалий-натрий тартраты Е-337")
    
  elif message.text == "341":
    bot.reply_to(message, "Күмәнді \nОртофосфат кальцийі Е-341")
    
  elif message.text == "422":
    bot.reply_to(message, "Күмәнді \nГлицерин Е-422")
    
  elif message.text == "470":
    bot.reply_to(message, "Күмәнді \nНатри, калий и кальций май қышқылының тұздары Е-470")
    
  elif message.text == "471":
    bot.reply_to(message, "Күмәнді \nМоно- и диглицерид май қышқылдары Е-471")
    
  elif message.text == "472":
    bot.reply_to(message, "Күмәнді \nМоно- и диглицерид май қышқылдарының түрлі эфирлері Е-472")
    
  elif message.text == "473":
    bot.reply_to(message, "Күмәнді \nСахароза және май қышқылының эфирлері Е-473")
    
  elif message.text == "474":
    bot.reply_to(message, "Күмәнді \nҚантты глицеридтер Е-474")
    
  elif message.text == "475":
    bot.reply_to(message, "Күмәнді \nПолиглицерид және май қышқылдарының эфирлері Е-475")
    
  elif message.text == "476":
    bot.reply_to(message, "Күмәнді \nПолиглицериннің күрделі эфирлері және эфирленген рицинол қышқылдары Е-476")
    
  elif message.text == "477":
    bot.reply_to(message, "Күмәнді \nПропиленгликол және май қышқылының эфирлері Е-477")
    
  elif message.text == "478":
    bot.reply_to(message, "Күмәнді \nЭфиры лактилированных жирных кислот, глицерина и пропиленгликоля Е-478")
    
  elif message.text == "481":
    bot.reply_to(message, "Күмәнді \nНатри лактитаты Е-481")
    
  elif message.text == "482":
    bot.reply_to(message, "Күмәнді \nКальци лактитаты Е-482")
    
  elif message.text == "483":
    bot.reply_to(message, "Күмәнді \nСтеарилтартрат Е-483")
    
  elif message.text == "491":
    bot.reply_to(message, "Күмәнді \nСорбитан моностеарат Е-491")
    
  elif message.text == "492":
    bot.reply_to(message, "Күмәнді \nСорбитан тристеарат Е-492")
    
  elif message.text == "493":
    bot.reply_to(message, "Күмәнді \nСорбитан монолаурат Е-493")
    
  elif message.text == "494":
    bot.reply_to(message, "Күмәнді \nСорбитан моноолеат Е-494")
    
  elif message.text == "542":
    bot.reply_to(message, "Күмәнді \nФосфат натрия Е-542")
    
  elif message.text == "544":
    bot.reply_to(message, "Күмәнді \nПолифосфат кальция Е-544")
    
  elif message.text == "556":
    bot.reply_to(message, "Күмәнді \nАлюмосиликат кальция Е-556")
    
  elif message.text == "620":
    bot.reply_to(message, "Күмәнді \nL-глутаминовая кислота Е-620")
    
  elif message.text == "621":
    bot.reply_to(message, "Күмәнді \nГлутаминат натрия однозамещенный Е-621")
    
  elif message.text == "622":
    bot.reply_to(message, "Күмәнді \nГлутаминат калия однозамещенный Е-622")
    
  elif message.text == "623":
    bot.reply_to(message, "Күмәнді \nГлутаминат кальция однозамещенный Е-623")
    
  elif message.text == "627":
    bot.reply_to(message, "Күмәнді \nГуанилат натрия Е-627")
    
  elif message.text == "631":
    bot.reply_to(message, "Күмәнді \nИнозинат натрия двузамещенный Е-631")
    
  elif message.text == "635":
    bot.reply_to(message, "Күмәнді \nРибонуклеотид натрия двузамещенный Е-635")
    
  elif message.text == "904":
    bot.reply_to(message, "Күмәнді \nШеллак Е-904")
    
  else:
    bot.reply_to(message, "Сізді түсінбедім! \nӨтініш \"171\", \"160b\" үлгісінде жазыңыз!\nНемесе бұл қоспа туралы ақпарат жоқ")

bot.polling()