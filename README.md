# Test-Kafka

# Tạo topic "views" với 3 partition
<img width="1430" alt="Screen Shot 2022-05-19 at 21 08 31" src="https://user-images.githubusercontent.com/53045534/169313756-a63112d7-87f0-4a76-add5-53d25ec7a620.png">



## producer.py


```python
for number in range(100):
    data = {'number': number}
    data = json.dumps(data)

    p.produce(topic, data, callback=delivery_callback)
    p.poll(0)

    sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
    p.flush()
```

## Bên trong producer.py vòng for lần lượt theo thứ tự từ 1-100 nhưng consumer lại nhận kết quả theo thứ tự khác

<img width="716" alt="Screen Shot 2022-05-19 at 21 13 50" src="https://user-images.githubusercontent.com/53045534/169314920-da1090c7-1805-43d7-8a4e-dc18ec440494.png">



## Phân bố message giữa các partition cũng không đồng đều

<img width="1439" alt="Screen Shot 2022-05-19 at 21 15 51" src="https://user-images.githubusercontent.com/53045534/169315396-bebec4e6-05f6-45dc-b39f-3f674dc2eae1.png">
