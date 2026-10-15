from address import Address
from mailing import Mailing

mailing = Mailing(Address("452120", "Раевский", "пер.Чкалова", "1A", "9"),
                  Address("109004", "Москва", "ул.Александра Солженицына", "23A", "стр.4"),
                  500, "№123456789")

fr = mailing.from_address
to = mailing.to_address

print(f"Отправление {mailing.track} из {fr.postal_code}, {fr.city}, {fr.street}, {fr.building_number} - {fr.apt_number} "
      f"в {to.postal_code}, {to.city}, {to.street}, {to.building_number} - {to.apt_number}. "
      f"Стоимость {mailing.cost} рублей.")