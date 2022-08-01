from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton #ReplyKeyboardButton
mainmenu = InlineKeyboardMarkup(#menu osnovnoy
 	inline_keyboard = [
 	      [
 	      InlineKeyboardButton(text="Lavash🌯",callback_data="Lavash"),
 	      InlineKeyboardButton(text="Xot-dog🌭",callback_data="Hot-dog"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Senvich-klub🥪",callback_data="Sendwichlar"),
 	      InlineKeyboardButton(text="Shaurma🌮",callback_data="Shaurma"),
 	      ],
 	      [
          InlineKeyboardButton(text="Burger🍔",callback_data="Burger"),
 	      InlineKeyboardButton(text="Donar🥙",callback_data="Donar"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Gazaklar🍟",callback_data="Kartoshka"),
 	      InlineKeyboardButton(text="Ichimliklar🥤",callback_data="Cola"),
 	      ],
 	      [
 	      InlineKeyboardButton(text="Desertlar🍰",callback_data="Desert"),
 	      InlineKeyboardButton(text="Pizza🍕",callback_data="Pizza")
 	      ],
 	 ],
 )
#ichimliklar
ichim = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Choy va kofe☕️',callback_data='choy_kofe'),
    InlineKeyboardButton(text='Sovuq ichimliklar🍹',callback_data='sovuqich')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='ichim_ortga')
	],
	],

	)
koffe = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Capuccino☕️',callback_data='cap'),
    InlineKeyboardButton(text='Late☕️',callback_data='cap')
	],
	[
    InlineKeyboardButton(text='Ekspresso☕️',callback_data='cap'),
    InlineKeyboardButton(text='Limon choy🍵',callback_data='choy')
	],
	[
    InlineKeyboardButton(text='Kora choy🍵',callback_data='choy'),
    InlineKeyboardButton(text='Kok choy🍵',callback_data='choy')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='koffelar_ortga')
	],
    ],

)
sovuqlar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Coca-cola 0.5',callback_data='cocacolar'),
    InlineKeyboardButton(text='Fanta 0.5',callback_data='cocacolar')
	],
	[
    InlineKeyboardButton(text='Sprite 0.5',callback_data='cocacolar'),
    InlineKeyboardButton(text='Pepsi 0.5',callback_data='cocacolar')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='cocacolar_ortga')
	],
    ],

)
ichl = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='ich_ortga')
	],
	],
) 
koffe_uchun = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='cap_ortga')
	],
	],
) 

lavash_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Mol Goshtlik original🥩',callback_data='Lavash_orignal'),
    InlineKeyboardButton(text='Tovuq Goshtlik original🍗',callback_data='Lavashtovuq_original')
	],
	[
    InlineKeyboardButton(text='Qalampir+Mol🥩🌶',callback_data='Lavash_qalampir'),
    InlineKeyboardButton(text='Qalampir+Tovuq🍗🌶',callback_data='Lavashtovuq_qalampir')
	],
	[
    InlineKeyboardButton(text='Pishloq+Mol🥩🧀',callback_data='Lavash_pishloq'),
    InlineKeyboardButton(text='Pishloq+Tovuq🍗🧀',callback_data='Lavashtovuq_pishloq')
	],
	[
	InlineKeyboardButton(text='Fitter🥬',callback_data='fitter')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='lavash_ortga')
	],
    ],

)
#shaurma
shaurma_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Mol Goshtlik original🥩',callback_data='shaurma_orignal'),
    InlineKeyboardButton(text='Tovuq Goshtlik original🍗',callback_data='shaurmatovuq_original')
	],
	[
    InlineKeyboardButton(text='Qalampir+Mol🥩🌶',callback_data='shaurma_qalampir'),
    InlineKeyboardButton(text='Qalampir+Tovuq🍗🌶',callback_data='shaurmatovuq_qalampir')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='shaurmamain_ortga')
	],
    ],

)
#miniclassic shaurma
molshaumra = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='molshaurma_mini'),
    InlineKeyboardButton(text='classic',callback_data='molshaurma_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='molshaurma_ortga')
	],
	],

	)
shaurmatovuq = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='tovuqshaurma_mini'),
    InlineKeyboardButton(text='classic',callback_data='tovuqshaurma_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovuqshaurma_ortga')
	],
	],

	)
shaurmaqalampir = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='qalamshaurma_mini'),
    InlineKeyboardButton(text='classic',callback_data='qalamshaurma_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='qalamshaurma_ortga')
	],
	],

	)
shtovuqqalampir = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='tovqshaurma_mini'),
    InlineKeyboardButton(text='classic',callback_data='tovshaurma_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovshaurma_ortga')
	],
	],

	)
suv = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='tovqshaurma_mini'),
    InlineKeyboardButton(text='classic',callback_data='tovshaurma_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovshaurma_ortga')
	],
	],

	)
#mini classic для лаваш orignal
lavash_original_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavash_orignal_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavash_original_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignal_ortga')
	],
	],

	)
#лаваш с курицей выбор классик или мини
lavash_originaltovuq_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavash_tovuqorignal_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavash_tovuqoriginal_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignaltovuq_ortga')
	],
	],

	)
#qalampir+mol lavash
lavash_qalampir_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavash_qalampir_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavash_qalampir_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_qalampir_ortga')
	],
	],

	)
lavash_tovuqqalampir_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavash_tovuqqalampir_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavash_tovuqqalampir_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_tovuqqalampir_ortga')
	],
	],

	)
burgerlar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Gamburger🍔',callback_data='gamb'),
    InlineKeyboardButton(text='Chizburger🍔',callback_data='chiz')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='burgerlar_ortga')
	],
	],

	)
pishloq_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavash_pishloq_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavash_pishloq_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_pishloq_ortga')
	],
	],

	)
pishloqtovuq_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='mini',callback_data='Lavashtovuq_pishloq_mini'),
    InlineKeyboardButton(text='classic',callback_data='Lavashtovuq_pishloq_classic')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavashtovuq_pishloq_ortga')
	],
	],

	)
#для хотдогов
hotdog_klik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Hot dog baget Dabl🌭🌭',callback_data='Dabl_hotdog'),
    InlineKeyboardButton(text='Classic Hot dog🌭',callback_data='class_hotdog')
	],
	[
    InlineKeyboardButton(text='Karalevski hot-dog🌭🌭',callback_data='king_hotdog'),
    InlineKeyboardButton(text='Tovuqli xot dog🌭🍗',callback_data='tovuq_hotdog')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='hotdog_ortga')
	],
	]
)
#для сендвич клабов
sendwich = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Tovuqli sendwich club🥪 ',callback_data='tovuq_sendwc'),
    InlineKeyboardButton(text='Classic sendwich club🥪 ',callback_data='sendwich_cls')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='sendwich_ortga')
	],
	],

	)
#donar
donarlar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Tovuqlik Donar🥙',callback_data='Donar_tovuqlik'),
    InlineKeyboardButton(text='Goshtlik Donar🥙',callback_data='Donar_gosht')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Donar_ortga')
	],
	],

	)
#mini classic оригинальный лаваш выбор сколько нужно
lavashoriginal_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignal_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_original_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_original_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignal_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_original_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_original_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignal_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_original_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_original_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignal_mini_ortga')
	],
	],
)
#тоже что и сверху только для classic
lavashoriginal_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignal_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_original_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_original_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignal_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_original_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_original_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignal_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_original_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_original_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignal_classic_ortga')
	],
	],
)
#куринный классик лаваш
lavashoriginaltovuq_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignaltovuq_classic_ortga')
	],
	],
)
lavashoriginaltovuq_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_orignaltovuq_cls_ortga')
	],
	],
)
#qalampir+mol lavash
lavashqalampir_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_qalampir_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_qalampir_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_qalampir_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_qalampir_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_qalampir_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_qalampir_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_qalampir_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_qalampir_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_qalampir_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_qalampir_mini_ortga')
	],
	],
)
lavashqalampir_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_qalampir_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_qalampir_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_qalampir_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_qalampir_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_qalampir_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_qalampir_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_qalampir_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_qalampir_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_qalampir_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_qalampir_classic_ortga')
	],
	],
)
lavashtovuqqalampir_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_tovuqqalampir_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_tovuqqalampir_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_tovuqqalampir_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_tovuqqalampir_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_tovuqqalampir_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_tovuqqalampir_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_tovuqqalampir_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_tovuqqalampir_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_tovuqqalampir_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_tovuqqalampir_clas_ortga')
	],
	],
)
lavashtovuqqalampir_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_tovuqqalampir_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_tovuqqalampir_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_tovuqqalampir_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_tovuqqalampir_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_tovuqqalampir_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_tovuqqalampir_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_tovuqqalampir_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_tovuqqalampir_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_tovuqqalampir_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_tovuqqalampir_mini_ortga')
	],
	],
)
#pishloq lavash classic
lavashpishloq_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_pishloq_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_pishloq_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_pishloq_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_pishloq_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_pishloq_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_pishloq_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_pishloq_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_pishloq_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_pishloq_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_pishloq_classic_ortga')
	],
	],
)
lavashpishloq_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_mini_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_mini_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_mini_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_mini_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_mini_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_mini_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_mini_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_mini_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_mini_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavash_pishloq_mini_ortga')
	],
	],
)
#tovuq lavash pishloq
lavashtovuqpishloq_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavashtovuq_pishloq_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavashtovuq_pishloq_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavashtovuq_pishloq_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavashtovuq_pishloq_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavashtovuq_pishloq_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavashtovuq_pishloq_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavashtovuq_pishloq_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavashtovuq_pishloq_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavashtovuq_pishloq_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavashtovuq_pishloq_classic_ortga')
	],
	],
)
lavashtovuqpishloq_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavashtovuq_mini_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavashtovuq_mini_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavashtovuq_mini_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavashtovuq_mini_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavashtovuq_mini_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavashtovuq_mini_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavashtovuq_mini_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavashtovuq_mini_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavashtovuq_mini_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='Lavashtovuq_pishloq_classic_ortga')
	],
	],
)
fitter_lavash = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='fitter_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='fitter_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='fitter_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='fitter_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='fitter_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='fitter_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='fitter_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='fitter_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='fitter_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='fitter_classic_ortga')
	],
	],
)
dabl_hd = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='dablhd_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='dablhd_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='dablhd_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='dablhd_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='dablhd_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='dablhd_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='dablhd_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='dablhd_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='dablhd_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='dablhd_ortga')
	],
	],
)
classic_hd = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='clshotd_ortga')
	],
	],
)
king_hd = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='kinghd_ortga')
	],
	],
)
tovuq_hd = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovuqhd_ortga')
	],
	],
)
tovuq_senwich = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovuqsendwich_ortga')
	],
	],
)
cls_senwich = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='tovuqsendwich_ortga')
	],
	],
)
#for burgers
gambu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='gambu_ortga')
	],
	],
)
chizbu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='gambu_ortga')
	],
	],
)
#for donar
tovuqdon = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='donarlardan_ortga')
	],
	],
)
goshtdon = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='donarlardan_ortga')
	],
	],
)
#free kartoshki
freelar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Fri 150gr🍟 ',callback_data='fricls'),
    InlineKeyboardButton(text='Fri po Derevenski🍟',callback_data='derevnya')
	],
		[
    InlineKeyboardButton(text='Katta guruch🍟',callback_data='kattagr'),
    InlineKeyboardButton(text='Kichik guruch🍟',callback_data='kichikgr')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='fri_ortga')
	],
	],

	)
# на free общий InlineMarkup просто чтоб быстрее закончить на проекте будет отдельно
gaz = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='gazaklar_ortga')
	],
	],
) 
pizzalar = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Peperoni🍕',callback_data='peperoni'),
    InlineKeyboardButton(text='Ananslik🍕',callback_data='anas')
	],
		[
    InlineKeyboardButton(text='Margaritta🍕',callback_data='Marga'),
    InlineKeyboardButton(text='Ovoshnoy🍕',callback_data='Ovosh')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='pitsmen_ortga')
	],
	],

	)
# на pitsa общий InlineMarkup просто чтоб быстрее закончить на проекте будет отдельно
pitsa = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='pizza_ortga')
	],
	],
) 
#сладкое
sladkiy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
    InlineKeyboardButton(text='Assalim🍨',callback_data='asal'),
    InlineKeyboardButton(text='Choco🍨',callback_data='chocol')
	],
		[
    InlineKeyboardButton(text='Qulupnay🍨',callback_data='qulup'),
    InlineKeyboardButton(text='Ice-cream🍨',callback_data='ice')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='asallar_ortga')
	],
	],

	)
# на pitsa общий InlineMarkup просто чтоб быстрее закончить на проекте будет отдельно
sladkiy_knopka = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_orignaltovuq_mini_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_originaltovuq_mini_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_originaltovuq_mini_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_orignaltovuq_mini_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_originaltovuq_mini_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_originaltovuq_mini_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_orignaltovuq_mini_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_originaltovuq_mini_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_originaltovuq_mini_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='slad_ortga')
	],
	],
) 
shaurma_originall = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	 InlineKeyboardButton(text='1️⃣',callback_data='Lavash_qalampir_classic_1'),
     InlineKeyboardButton(text='2️⃣',callback_data='Lavash_qalampir_classic_2'),
     InlineKeyboardButton(text='3️⃣',callback_data='Lavash_qalampir_classic_3')
	],
	[
	 InlineKeyboardButton(text='4️⃣',callback_data='Lavash_qalampir_classic_4'),
     InlineKeyboardButton(text='5️⃣',callback_data='Lavash_qalampir_classic_5'),
     InlineKeyboardButton(text='6️⃣',callback_data='Lavash_qalampir_classic_6')
	],
	[
	 InlineKeyboardButton(text='7️⃣',callback_data='Lavash_qalampir_classic_7'),
     InlineKeyboardButton(text='8️⃣',callback_data='Lavash_qalampir_classic_8'),
     InlineKeyboardButton(text='9️⃣',callback_data='Lavash_qalampir_classic_9')
	],
	[
	InlineKeyboardButton(text='Ortga◀️',callback_data='shaurma_classic_ortga')
	],
	],
)
# кнопки которые внизу для заказа вначале
keyb = ReplyKeyboardMarkup(
	keyboard = [
	      [
	      KeyboardButton(text="🛍 Buyurtma berish"),
	      ],
	      [
	      KeyboardButton(text="▶️ Sozlamalar"),
	      KeyboardButton(text="☎️ Biz bn aloqa")
	      ],
	 ],
	 resize_keyboard = True #адаптивность
)