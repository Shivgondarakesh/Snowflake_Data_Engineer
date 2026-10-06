from logger import logger

def save_output(df,path):
 logger.info(f"Writing {path}")
 df.to_csv(path,index=False)
