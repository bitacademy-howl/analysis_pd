import os

# configuration
CONFIG = {
    'district' : '서울특별시',
    'countries' : [('중국', 112), ('일본', 130), ('미국', 275)],
    'common' : {
        'service_key' : '%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
        'start_year' : 2017, # CONFIG['common']['start_year']
        'end_year' : 2017,
        'fetch' : False,
        'result_directory' : '__results__/crawling'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])