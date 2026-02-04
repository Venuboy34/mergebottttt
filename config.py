import os


class Config(object):
    # Telegram API Configuration
    API_HASH = "d702614912f1ad370a0d18786002adbf"
    BOT_TOKEN = "8352604915:AAEjDWEeUnYt2HKdCLbznoevEHLda4TEnm0"
    TELEGRAM_API = "20288994"
    
    # Owner Configuration
    OWNER = "8498741978"
    OWNER_USERNAME = "@Mergerbot_Z_bot"
    PASSWORD = "12345"
    
    # Database Configuration
    DATABASE_URL = "mongodb+srv://Zerobothost:zero8907@cluster0.szwdcyb.mongodb.net/?appName=Cluster0"
    
    # Channel Configuration
    LOGCHANNEL = "-1003712131076"  # Add channel id as -100 + Actual ID
    
    # Google Drive Configuration
    GDRIVE_FOLDER_ID = "root"
    
    # User Session - Premium account session string to upload upto 4GB (requires "LOGCHANNEL")
    USER_SESSION_STRING = "BQE1leIAQ91QBxeeXOVyv4pFbVCZlK-lwgQCTge8tptNm8H8K3s1LedpPDYDOKhyqkNztGmXMOuBIfwezqN02GRf6NPEEtLI_78tNqvV9Amb_0Iw3FA-cJwYX-AnRYWG_dqTvfNWoA8lIa2GTz3SSsZdu2l8eb4rfQHxCGSsbAy5leT7yJbOWDzCWFA2_iLnEgPoovkmTMuliKmyvAe6feHfaPGCd-pLCpRKSE26S1UzsG0Tw0M1JJZVGqfOrx9_CiREP1oytxPMUVBTAzQNlJn6L1EeYwZ38qQ9kKqw8M3mBysKo6UhzwGbX1eV84Le5DiZAUezBw7CZnWbj1ZVTvBWut2kZQAAAAHjUB8sAA"
    
    # Premium Status
    IS_PREMIUM = False
    
    # Available Modes
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
    
    # Repository Configuration (tired of redeploying :()
    UPSTREAM_REPO = "https://github.com/yashoswalyo/MERGE-BOT"
    UPSTREAM_BRANCH = "master"
