import requests
import json
import asyncio
import aiohttp
import time

loginUrl = '' #target url login endpoint
url = '' #target url
data = {
    "username": "",
    "password": ""
} # data send for login

headers = {
    'Content-Type': 'application/json'
}

# Fungsi untuk GET request
def getAPI(url):
    response = requests.get(url)
    if response.status_code == 200:
        return 1
    else:
        print(f"Error: {response.status_code}")
        return 0

# Fungsi untuk login
def login(url, data, headers={'Content-Type': 'application/json'}):
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print('Login successful')
    else:
        print(f"Error: {response.status_code}")

# Fungsi untuk Stress Test
async def stressTest(requestPerSecond, totalRequest, url):
    async with aiohttp.ClientSession() as session:
        success_count = 0
        error_count = 0
        request_sent = 0  # Total request yang telah dikirimkan
        start_time = time.time()
        
        # Fungsi untuk mengirim request asinkron
        async def send_request():
            nonlocal success_count, error_count, request_sent
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        success_count += 1
                    else:
                        error_count += 1
                    request_sent += 1
            except Exception as e:
                print(f"Error: {e}")
                error_count += 1
                request_sent += 1

        tasks = []
        for _ in range(totalRequest):
            task = asyncio.create_task(send_request())
            tasks.append(task)
            
            # Mengatur berapa banyak request yang bisa dikirim per detik
            if len(tasks) >= requestPerSecond:
                await asyncio.gather(*tasks)
                tasks = []  # Reset task list setelah mengirim

                # Monitor request sent per detik dan tampilkan laporan sementara
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time >= 1:  # Jika sudah satu detik
                    print(f"Requests Sent: {request_sent} | Success: {success_count} | Errors: {error_count} | Time Elapsed: {elapsed_time:.2f}s")
                    start_time = current_time  # Reset waktu laporan

        # Menunggu task yang tersisa jika ada
        if tasks:
            await asyncio.gather(*tasks)

        total_time = time.time() - start_time
        print(f"\nStress Test Completed: Total requests sent: {totalRequest}")
        print(f"Success count: {success_count}")
        print(f"Error count: {error_count}")
        print(f"Requests per second: {request_sent / total_time:.2f} requests/sec")

# Login dan test
login(loginUrl, data, headers)

# Stress Test dengan request per detik dan total request
asyncio.run(stressTest(1, 100, url))  # requests per detik dan total request


def stressTestLogin() :
    token = login(loginUrl, data, headers)
    if token:
        # Menambahkan token ke headers untuk otentikasi
        headers['Authorization'] = f"Bearer {token}"
        # Stress Test dengan request per detik dan total request
        asyncio.run(stressTest(1, 100, url, headers))  # requests per detik dan total request
    else:
        print("Login gagal, tidak dapat melakukan stress test.")