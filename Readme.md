# kafka producer and consumer

## python

run as following
```
python3 producer.py [args]
```

usage
```
-h, --help
	show this help message and exit
--port PORT, -p PORT
	broker port
--ip IP, -i IP
	borker ip
--topic TOPIC, -t TOPIC
	topic
--message MESSAGE, -m MESSAGE
	if not set, send number that auto incremented as a message
```


run as following
```
python3 consumer.py [args]
```

usage
```
-h, --help
	show this help message and exit
--port PORT, -p PORT
	broker port
--ip IP, -i IP
	borker ip
--topic TOPIC, -t TOPIC
	topic
--group GROUP, -g GROUP
    group id
--offset OFFSET, -o OFFSET
    offset option\ l:latest\ e:earlist
```


