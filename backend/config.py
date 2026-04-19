import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from redis import Redis
import pymongo


# Database configuration
DATABASE_URL_POSTGRESQL = os.getenv('DATABASE_URL_POSTGRESQL', 'postgresql://user:password@localhost/dbname')
DATABASE_URL_MONGODB = os.getenv('DATABASE_URL_MONGODB', 'mongodb://localhost:27017/')

# Setup PostgreSQL
engine = create_engine(DATABASE_URL_POSTGRESQL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Setup MongoDB
mongo_client = pymongo.MongoClient(DATABASE_URL_MONGODB)

# Setup Redis
redis_client = Redis(host='localhost', port=6379, db=0)

# MinIO configuration
MINIO_URL = os.getenv('MINIO_URL', 'http://localhost:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'minio-access-key')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'minio-secret-key')

# Model configuration
FLUX_MODEL_PATH = os.getenv('FLUX_MODEL_PATH', '/path/to/flux/model')
STABLE_DIFFUSION_MODEL_PATH = os.getenv('STABLE_DIFFUSION_MODEL_PATH', '/path/to/stable/diffusion/model')

# Image processing tools configuration
REMBG_TOOL_PATH = os.getenv('REMBG_TOOL_PATH', '/path/to/rembg')
U2NET_TOOL_PATH = os.getenv('U2NET_TOOL_PATH', '/path/to/u2net')
OPENCV_TOOL_PATH = os.getenv('OPENCV_TOOL_PATH', '/path/to/opencv')
GMIC_TOOL_PATH = os.getenv('GMIC_TOOL_PATH', '/path/to/gmic')

# Advanced features for inpainting and style transfer
ENABLE_INPAINTING = True
ENABLE_STYLE_TRANSFER = True

# Rate limiting configuration
RATE_LIMIT_REQUESTS = os.getenv('RATE_LIMIT_REQUESTS', 100)  # example value
RATE_LIMIT_WINDOW = os.getenv('RATE_LIMIT_WINDOW', 60)  # in seconds

# Production settings
DEBUG = False
LOGGING_LEVEL = 'INFO'  # or other logging levels


if __name__ == '__main__':
    print('Backend configuration loaded successfully.')