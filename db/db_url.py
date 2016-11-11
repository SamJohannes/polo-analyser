import os

def db_url():
    try: 
        db = {
            'ENGINE': 'postgres',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PSWD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ[
                'RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }

    except:
        raise OSError('Database environment variables not set')


    if db['USER'] == 'test':
        databaseUrl = 'postgresql://{}@{}/{}'.format(db['USER'], db['HOST'], \
                                                     db['NAME'])
    else: 
        databaseUrl = 'postgresql://{}:{}@{}:{}/{}'.format(db['USER'], db['PSWD'], \
                                                           db['HOST'], db['PORT'], \
                                                           db['NAME'])
    return databaseUrl
