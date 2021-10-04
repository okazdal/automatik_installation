# InfluxDB Configuration

- [Open page](http://localhost:8086)
  
![InfluxDb setup 1](images/setup_1.png)

- Create initial username, password, organization name and bucket name
- Organization name must be "automatik"

![InfluxDB setup 2](images/setup_2.png)
![InfluxDB setup 3](images/setup_3.png)

- Click on 'Data'

![InfluxDB setup 4](images/setup_4.png)

- Create bucket named 'monitoring' and 'rates'. Optionally you can set a retention period.

![InfluxDB setup 5](images/setup_5.png)

![InfluxDB setup 6](images/setup_6.png)

![InfluxDB setup 4](images/setup_7.png)

- Create a token that we will use to read and write data to InfluxDB

![InfluxDB setup 4](images/setup_8.png)

![InfluxDB setup 4](images/setup_9.png)

- Copy token somewhere safe. You will use this token in a minute.

![InfluxDB setup 4](images/setup_10.png)

## Next Step

[Configure Minio](minio_config.md)
