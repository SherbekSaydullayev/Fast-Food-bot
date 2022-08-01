import logging 
from config import API_TOKEN
from buttons import * 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)#диспетчер
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"<strong>{message.from_user.full_name} Botga xush kelibsiz,Buyurtma bering🛍</strong>",parse_mode='HTML',reply_markup=keyb)


@dp.message_handler(text = "🛍 Buyurtma berish")
async def send_welcome(message: types.Message):
    await message.reply("<b>Menuga marxamat 📒,nimadan boshlaymiz?</b>" ,parse_mode='HTML',reply_markup = mainmenu)




@dp.callback_query_handler(text="Lavash")
async def menu_tanlash(call:CallbackQuery):
   await call.message.answer_photo(
        photo = open('images/lavashlar/общийлаваш.jpg','rb'),
        caption = """""",parse_mode='HTML',reply_markup = lavash_klik)
   await call.message.delete()           

@dp.callback_query_handler(text="lavash_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)

@dp.callback_query_handler(text="Lavash_orignal")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_original_klik)

@dp.callback_query_handler(text="Lavash_orignal_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)


@dp.callback_query_handler(text="Lavash_orignal_mini_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_original_klik)
@dp.callback_query_handler(text="Lavash_orignal_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashoriginal_mini)
    await call.message.delete()


@dp.callback_query_handler(text="Lavash_original_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/lavashtov.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashoriginal_classic)
    await call.message.delete()


@dp.callback_query_handler(text="Lavash_orignal_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_original_klik)


@dp.callback_query_handler(text="Lavashtovuq_original")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_originaltovuq_klik)


@dp.callback_query_handler(text="Lavash_tovuqoriginal_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/lavashtov.jpg','rb'),
        caption = """<strong>Narxi: 22 000 so'm"
Tarkibi: Xamir, tovuq gosht, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashoriginaltovuq_classic)
    await call.message.delete()


@dp.callback_query_handler(text="Lavash_orignaltovuq_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_originaltovuq_klik)


@dp.callback_query_handler(text="Lavash_tovuqorignal_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashoriginaltovuq_mini)
    await call.message.delete()
    

@dp.callback_query_handler(text="Lavash_orignaltovuq_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)

@dp.callback_query_handler(text="Lavash_orignaltovuq_cls_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_originaltovuq_klik )



@dp.callback_query_handler(text="Lavash_qalampir")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_original_klik)


@dp.callback_query_handler(text="Lavash_qalampir_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, tovuq go`sht, chips,qalampir, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashqalampir_mini)
    await call.message.delete()

@dp.callback_query_handler(text="Lavash_orignal_mini_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_qalampir_klik)
@dp.callback_query_handler(text="Lavash_qalampir_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_qalampir_klik)


dp.callback_query_handler(text="Lavash_qalampir_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashqalampir_classic)
    await call.message.delete()
  
#вывести qalampir tovuq mini class
@dp.callback_query_handler(text="Lavash_tovuqqalampir_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)
@dp.callback_query_handler(text="Lavashtovuq_qalampir")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_tovuqqalampir_klik)
#tovuq qalampir classic
@dp.callback_query_handler(text="Lavash_tovuqqalampir_classic")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashtovuqqalampir_classic)
     await call.message.delete()

#mini tq
@dp.callback_query_handler(text="Lavash_tovuqqalampir_mini")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashtovuqqalampir_mini)
     await call.message.delete()

@dp.callback_query_handler(text="Lavash_tovuqqalampir_mini_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_tovuqqalampir_klik)

@dp.callback_query_handler(text="Lavash_tovuqqalampir_clas_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_tovuqqalampir_klik)
#pishloq lavash klassik mini
@dp.callback_query_handler(text="Lavash_pishloq")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pishloq_lavash)


@dp.callback_query_handler(text="Lavash_pishloq_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)


@dp.callback_query_handler(text="Lavash_pishloq_classic")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashpishloq_classic)
     await call.message.delete()
   
@dp.callback_query_handler(text="Lavash_pishloq_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pishloq_lavash)
@dp.callback_query_handler(text="Lavash_pishloq_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashpishloq_mini)
    await call.message.delete()
   

@dp.callback_query_handler(text="Lavash_pishloq_mini_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pishloq_lavash)
@dp.callback_query_handler(text="Lavashtovuq_pishloq")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pishloqtovuq_lavash)
@dp.callback_query_handler(text="Lavashtovuq_pishloq_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)
@dp.callback_query_handler(text="Lavashtovuq_pishloq_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup = lavashtovuqpishloq_classic)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi:   22 000 so'm \nTarkibi: Xamir, Tovuq go`sht, garimdor, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting</strong>:",parse_mode='HTML',reply_markup=lavashtovuqpishloq_classic)
@dp.callback_query_handler(text="Lavashtovuq_pishloq_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pishloqtovuq_lavash )
@dp.callback_query_handler(text="Lavashtovuq_pishloq_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/originlavsh.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup =lavashtovuqpishloq_mini)
    await call.message.delete()
    

@dp.callback_query_handler(text="fitter")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/lavashlar/fitter.jpg','rb'),
        caption = """<strong>Narxi: 20 000 so'm"
Tarkibi: Xamir, mol go`sht,qalampir, chips, pomidor, bodring, sous, mayonez,salat"
Miqdorini tanlang yoki kiriting</strong>""",parse_mode='HTML',reply_markup =fitter_lavash)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi:   22 000 so'm \nTarkibi: Xamir, Tovuq go`sht, garimdor, chips, pomidor, bodring, sous, mayonez \nMiqdorini tanlang yoki kiriting</strong>:",parse_mode='HTML',reply_markup=fitter_lavash)
@dp.callback_query_handler(text="fitter_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=lavash_klik)
#for hotdogs
@dp.callback_query_handler(text="Hot-dog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Bizning xotdoglarimiz:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)
#dabl babt hd
@dp.callback_query_handler(text="Dabl_hotdog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/hd/baget.jpg','rb'),
        caption = """<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 17 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=dabl_hd)
    await call.message.delete()
@dp.callback_query_handler(text="Hot-dog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Bizning xotdoglarimiz:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)


@dp.callback_query_handler(text="hotdog_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="dablhd_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)
@dp.callback_query_handler(text="class_hotdog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/hd/classic.jpg','rb'),
        caption = """<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 17 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=classic_hd)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 17 000 so'm.</strong>:",parse_mode='HTML',reply_markup=classic_hd)
@dp.callback_query_handler(text="clshotd_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)
@dp.callback_query_handler(text="kinghd_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)
@dp.callback_query_handler(text="tovuqhd_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=hotdog_klik)
@dp.callback_query_handler(text="king_hotdog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/hd/classic.jpg','rb'),
        caption = """<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 17 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=king_hd)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 12 000 so'm.</strong>:",parse_mode='HTML',reply_markup=king_hd)
@dp.callback_query_handler(text="tovuq_hotdog")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/hd/classic.jpg','rb'),
        caption = """<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 17 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=tovuq_hd)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz.\n Narxi: 20 000 so'm.</strong>:",parse_mode='HTML',reply_markup=tovuq_hd)


@dp.callback_query_handler(text="Sendwichlar")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=sendwich)
@dp.callback_query_handler(text="sendwich_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=mainmenu)


@dp.callback_query_handler(text="tovuq_sendwc")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/sendwich/sendwich.jpg','rb'),
        caption = """<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 22 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=tovuq_senwich)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 22 000 so'm.</strong>:",parse_mode='HTML',reply_markup=tovuq_senwich)
@dp.callback_query_handler(text="tovuqsendwich_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=sendwich)
@dp.callback_query_handler(text="sendwich_cls")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('images/sendwich/sendwich.jpg','rb'),
        caption = """<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 22 000 so'm.</strong>:""",parse_mode='HTML',reply_markup=cls_senwich)
     await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 24 000 so'm.</strong>:",parse_mode='HTML',reply_markup=cls_senwich)

@dp.callback_query_handler(text="Burger")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=burgerlar)
@dp.callback_query_handler(text="burgerlar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=mainmenu)

@dp.callback_query_handler(text="gamb")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/burgerlar/br.jpg','rb'),
        caption = """<strong>Kulcha, go'shti, gamburger, pomidor, garimdori, sous,  piyoz.\n Narxi: 24 000 so'm</strong>""",parse_mode='HTML',reply_markup = gambu)
    await call.message.delete()
   

@dp.callback_query_handler(text="gambu_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=burgerlar)
@dp.callback_query_handler(text="chiz")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/burgerlar/br.jpg','rb'),
        caption = """<strong>Kulcha, go'shti, gamburger, pomidor, garimdori, sous,  piyoz.\n Narxi: 24 000 so'm</strong>""",parse_mode='HTML',reply_markup = chizbu)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, go'shti, chizburger, pomidor, garimdori, sous,  piyoz.\n Narxi: 21 000 so'm.</strong>:",parse_mode='HTML',reply_markup=chizbu)
#donar

@dp.callback_query_handler(text="Donar")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=donarlar)
@dp.callback_query_handler(text="Donar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="Donar_tovuqlik")
async def menu_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo = open('images/donar/donar.jpg','rb'),
        caption = """<strong>Kulcha, tovuq gosht, pomidor, garimdori, sous,  piyoz.\n Narxi: 30 000 so'm.</strong>""",parse_mode='HTML',reply_markup = tovuqdon)
     await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 30 000 so'm.</strong>:",parse_mode='HTML',reply_markup=tovuqdon)
@dp.callback_query_handler(text="donarlardan_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=donarlar)
@dp.callback_query_handler(text="Donar_gosht")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/donar/donar.jpg','rb'),
        caption = """<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 30 000 so'm.</strong>""",parse_mode='HTML',reply_markup = goshtdon)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kulcha, go'shti, pomidor, garimdori, sous,  piyoz.\n Narxi: 30 000 so'm.</strong>:",parse_mode='HTML',reply_markup=goshtdon)
#free
@dp.callback_query_handler(text="Kartoshka")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=freelar)
@dp.callback_query_handler(text="fricls")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/gazaklar/free.jpg','rb'),
        caption = """<strong>Fri 150gr: 6000som</strong>""",parse_mode='HTML',reply_markup = gaz)
    await call.message.delete()
    #await call.message.answer(f"<strong>Fri 150gr </strong>:",parse_mode='HTML',reply_markup=gaz)
@dp.callback_query_handler(text="derevnya")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/gazaklar/free.jpg','rb'),
        caption = """<strong>Po derevnski narxi: 6000som</strong>""",parse_mode='HTML',reply_markup = gaz)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kartoshka po derevnski</strong>:",parse_mode='HTML',reply_markup=gaz)
@dp.callback_query_handler(text="kattagr")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/gazaklar/free.jpg','rb'),
        caption = """<strong>Katta gruch</strong>""",parse_mode='HTML',reply_markup = gaz)
    await call.message.delete()
    #await call.message.answer(f"<strong>Katta guruch</strong>:",parse_mode='HTML',reply_markup=gaz)
@dp.callback_query_handler(text="kichikgr")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/gazaklar/free.jpg','rb'),
        caption = """<strong>Kichik gruch</strong>""",parse_mode='HTML',reply_markup = gaz)
    await call.message.delete()
    #await call.message.answer(f"<strong>Kichik gruch</strong>:",parse_mode='HTML',reply_markup=gaz)
@dp.callback_query_handler(text="fri_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="gazaklar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=freelar)
@dp.callback_query_handler(text="Pizza")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pizzalar)
@dp.callback_query_handler(text="pitsmen_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="pizza_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=pizzalar)
@dp.callback_query_handler(text="peperoni")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/pizza/pizza.jpg','rb'),
        caption = """<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>""",parse_mode='HTML',reply_markup = pitsa)
    await call.message.delete()
    #await call.message.answer(f"<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>:",parse_mode='HTML',reply_markup=pitsa)
@dp.callback_query_handler(text="Ovosh")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/pizza/pizza.jpg','rb'),
        caption = """<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>""",parse_mode='HTML',reply_markup = pitsa)
    await call.message.delete()
    #await call.message.answer(f"<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>:",parse_mode='HTML',reply_markup=pitsa)
@dp.callback_query_handler(text="anas")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/pizza/pizza.jpg','rb'),
        caption = """<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>""",parse_mode='HTML',reply_markup = pitsa)
    await call.message.delete()
    #await call.message.answer(f"<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>:",parse_mode='HTML',reply_markup=pitsa)
@dp.callback_query_handler(text="Marga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/pizza/pizza.jpg','rb'),
        caption = """<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>""",parse_mode='HTML',reply_markup = pitsa)
    await call.message.delete()
    #await call.message.answer(f"<strong>Пицца \nПепперониПицца Пепперони \n33см.Соус \nТоматный Для ПиццыТонкое \nтестоСыр 110 гр.\nNarxi: 65 000 so'm</strong>:",parse_mode='HTML',reply_markup=pitsa)
#sladkiy
@dp.callback_query_handler(text="Desert")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shirin.jpg','rb'),
        caption = """<strong>Shirinliklar</strong>""",parse_mode='HTML',reply_markup = sladkiy)
    await call.message.delete()
    #await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=sladkiy)
@dp.callback_query_handler(text="asallar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="chocol")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Аnʼnaviy taʼm - asal asosidagi biskvit va krem\nNarxi: 14 000 so'm</strong>:",parse_mode='HTML',reply_markup=sladkiy_knopka)
@dp.callback_query_handler(text="asal")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Аnʼnaviy taʼm - asal asosidagi biskvit va krem\nNarxi: 20 000 so'm</strong>:",parse_mode='HTML',reply_markup=sladkiy_knopka)
@dp.callback_query_handler(text="qulup")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Аnʼnaviy taʼm - asal asosidagi biskvit va krem\nNarxi: 15 000 so'm</strong>:",parse_mode='HTML',reply_markup=sladkiy_knopka)
@dp.callback_query_handler(text="ice")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Аnʼnaviy taʼm - asal asosidagi morojniy va krem\nNarxi: 10 000 so'm</strong>:",parse_mode='HTML',reply_markup=sladkiy_knopka)
@dp.callback_query_handler(text="slad_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Аnʼnaviy taʼm - asal asosidagi biskvit va krem\nNarxi: 15 000 so'm</strong>:",parse_mode='HTML',reply_markup=sladkiy)
@dp.callback_query_handler(text="Shaurma")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/obshiy.jpg','rb'),
        caption = """<strong>Shaurmalar</strong>""",parse_mode='HTML',reply_markup = shaurma_klik)
    await call.message.delete()
    #await call.message.answer(f"<strong>Shaurmalar:</strong>:",parse_mode='HTML',reply_markup=shaurma_klik)
@dp.callback_query_handler(text="shaurma_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Shaurmalar:</strong>:",parse_mode='HTML',reply_markup=shaurma_ortga)
@dp.callback_query_handler(text="shaurma_orignal")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Mol goshtlik shaurmalar</strong>:",parse_mode='HTML',reply_markup=molshaumra)
@dp.callback_query_handler(text="molshaurma_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Shaurmalar:</strong>:",parse_mode='HTML',reply_markup=shaurma_klik)
@dp.callback_query_handler(text="shaurmamain_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="molshaurma_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="molshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="shaurma_classic_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=molshaumra)
@dp.callback_query_handler(text="shaurmamain_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=mainmenu)
@dp.callback_query_handler(text="molshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="molshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)

@dp.callback_query_handler(text="shaurmatovuq_original")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shaurmatovuq)

@dp.callback_query_handler(text="shaurma_qalampir")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shaurmaqalampir)

@dp.callback_query_handler(text="shaurmatovuq_qalampir")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shtovuqqalampir)

@dp.callback_query_handler(text="tovuqshaurma_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shaurma_klik)

@dp.callback_query_handler(text="qalamshaurma_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shaurma_klik)

@dp.callback_query_handler(text="tovshaurma_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimadan boshlaymiz?</strong>:",parse_mode='HTML',reply_markup=shaurma_klik)

@dp.callback_query_handler(text="tovuqshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 18 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="tovuqshaurma_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)

@dp.callback_query_handler(text="qalamshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Narxi: 18 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="qalamshaurma_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open('images/shaurma/shaurma.jpg','rb'),
        caption = """<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>""",parse_mode='HTML',reply_markup = shaurma_originall)
    await call.message.delete()
    #await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)

@dp.callback_query_handler(text="tovqshaurma_mini")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Narxi: 18 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)
@dp.callback_query_handler(text="tovshaurma_classic")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Narxi: 22 000so'm\n Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez \n Miqdorini tanlang</strong>:",parse_mode='HTML',reply_markup=shaurma_originall)

@dp.callback_query_handler(text="Cola")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=ichim)

@dp.callback_query_handler(text="ichim_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=mainmenu)

@dp.callback_query_handler(text="choy_kofe")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=koffe)
@dp.callback_query_handler(text="kof_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=ichim)

@dp.callback_query_handler(text="cap")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Amerikano☕️ 12000mig so'm</strong>",parse_mode='HTML',reply_markup=koffe_uchun)
@dp.callback_query_handler(text="choy")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Choy qora 3000mig so'm</strong>",parse_mode='HTML',reply_markup=koffe_uchun)

@dp.callback_query_handler(text="koffelar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=ichim)
@dp.callback_query_handler(text="cap_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=koffe)

@dp.callback_query_handler(text="sovuqich")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=sovuqlar)
@dp.callback_query_handler(text="cocacolar_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Nimidan boshlaymiz?:</strong>",parse_mode='HTML',reply_markup=ichim)
@dp.callback_query_handler(text="cocacolar")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Napitka 0.5 \n Narxi:5000som </strong>",parse_mode='HTML',reply_markup=ichl)

@dp.callback_query_handler(text="ich_ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Napitka 0.5 \n Narxi:5000som </strong>",parse_mode='HTML',reply_markup=sovuqlar)

@dp.message_handler(text = "▶️ Sozlamalar")#вывод кнопок из menuosnovnoy
async def send_welcome(message: types.Message):
    await message.reply("<b>Эта часть пока не работает.Бот для портфолио обратитесь к создателю.Для продолжения теста нажмите 'Buyurtma berish'</b>" ,parse_mode='HTML')
@dp.message_handler(text = "☎️ Biz bn aloqa")#вывод кнопок из menuosnovnoy
async def send_welcome(message: types.Message):
    await message.reply("<b>Tg: @zaliv_dev</b>" ,parse_mode='HTML')

@dp.callback_query_handler(text="Lavash_orignal_mini_1")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 1 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_2")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 2 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_3")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 3 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_4")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 4 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_5")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 5 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_6")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 6 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_7")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 7 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')
@dp.callback_query_handler(text="Lavash_orignal_mini_8")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<strong>Sizning xaridingiz 8 molgoshtlik lavash \n Narxi:20000som </strong>",parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)