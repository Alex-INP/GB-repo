from requests import get, utils
from datetime import date
from decimal import *

content = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(input_curr_code):
	curr_code = input_curr_code.upper()

	date_list = content[content.find('Date=') + 6:content.find('Date=') + 16].split(".")
	d, m, y = date_list

	if curr_code in content:
		str_zone = content[content.find(curr_code):content.find("</Value>", content.find(curr_code))]
		str_number = str_zone[str_zone.find("<Value>") + 7:]
		dec_num = Decimal(str_number.replace(",", ".")).quantize(Decimal("1.00"))
		return dec_num, date(year=int(y), month=int(m), day=int(d))


print(currency_rates("USD"))
print(currency_rates("usd"))
print(currency_rates("EUR"))
print(currency_rates("EuR"))
print((currency_rates("DDDDF")))
