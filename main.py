from selenium import webdriver

from scrap import scrap
import settings



if __name__ == "__main__":

    # ドライバー設定
    driver = webdriver.Chrome(r"chromedriver.exe", options=settings.chrome_options)
    #ログイン
    scrap.log_in_amazon(driver)
    # 注文履歴へ
    scrap.go_to_order_history(driver)
    # 
