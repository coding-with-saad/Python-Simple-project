import qrcode

account_number = input("Enter phone number: ")

easypaisa_url = f'https://easypaisa.com.pk/pay?number={account_number}'
jazzcash_url = f'https://jazzcash.com.pk/pay?number={account_number}'
hbl_url = f'https://hbl.com/pay?number={account_number}'

easypaisa_qr = qrcode.make(easypaisa_url)
jazzcash_qr = qrcode.make(jazzcash_url)
hbl_qr = qrcode.make(hbl_url)

easypaisa_qr.save("easy.png")
jazzcash_qr.save("jazz.png")
hbl_qr.save("hbl.png")

easypaisa_qr.show()
jazzcash_qr.show()
hbl_qr.show()
