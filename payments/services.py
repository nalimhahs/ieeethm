import razorpay

client = razorpay.Client(auth=("rzp_test_pKWOPyipkLGMXB", "Xvpgatw44IzoXBp16YrETL7a"))
client.set_app_details({"title" : "Django", "version" : "2.2.4"})

def get_order():
  data = {
    "amount" : 100,
    "currency" : "INR",
    "receipt" : "ieeethm#1",
    "payment_capture" : 1,
    "notes" : {}
  }
  order = client.order.create(data=data)
  print(order)

get_order()