str_first="Hi"
cust_name="Vaibhav Tyagi"
print(f"{cust_name} is saying {str_first}")
print(cust_name[0])
print(cust_name[-1])
print(cust_name[0:8])
print(cust_name[:8])
print(cust_name[0:])
print(cust_name[::-1])
print(cust_name[::2])
label_text="hello 你好"
print(label_text)
encoded_label_text=label_text.encode("utf-8")
print(encoded_label_text)
decoded_label_text=encoded_label_text.decode("utf-8")
print(decoded_label_text)