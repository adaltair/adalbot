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
  
  else:
    bot.reply_to(message, "Сізді түсінбедім! \nӨтініш \"171\", \"160b\" үлгісінде жазыңыз!")

bot.polling()