from smartphone import Smartphone

catalog = [Smartphone("Apple", "iPhone 15 Pro", "+7987 654 32 19"),
           Smartphone("Samsung", "Galaxy S24 Ultra", "+7912 345 67 89"),
           Smartphone("Google", "Pixel 8 Pro", "+7987 642 23 45"),
           Smartphone("Motorola", "Edge 40 Pro", "+7987 632 28 19"),
           Smartphone("Sony", "Xperia 1 V", "+7987 258 65 63"),
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")