# SQLInjection

BlindSQLInjection Python3 Script to find a password 

## Objective

To **Hack the system** with **admin** account 
![image](https://user-images.githubusercontent.com/79100627/189540786-ad9cf476-7f32-4fa8-bbc0-2e9e1c0cf91f.png)

## Service Summary 

```
/login - Get Input (ID/PW) and retrieve data from the database to authenticate user
```

## Identification

Before we make an automated query, we need to figure out post data 

1. Open the network tap, select Preserve Log
2. Enter userid guest,password  and login 
3. From the message find the ```/login``` POST request 
4. Check the Form Data 

![image](https://user-images.githubusercontent.com/79100627/189540474-f6bc46c4-c9b6-4a1d-bb15-4ba77d27853e.png)

![image](https://user-images.githubusercontent.com/79100627/189540662-fa970fd9-17f5-4d59-bf16-b0e077fd03a2.png)


## Finding a password Length 

Find the length of the password using the script 

## Finding a password 

Find a password with one steps (Comparing one byte each)
![image](https://user-images.githubusercontent.com/79100627/189540748-efc3031c-045c-48ba-a229-acc8bce6535f.png)
